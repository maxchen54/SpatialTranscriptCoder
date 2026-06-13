from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from openai import OpenAI
from pathlib import Path
from typing import List
import os
import json
import csv
import io
from rubrics import spatial_words, rubric3

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
MODEL = "gpt-4o-mini"

system_prompt = f"""
You are a linguist specialized in discerning the meaning of words in context, with a focus on spatial language.

**Your Task:**

1. **Identify Spatial Words from the Dictionary:**
   - Carefully examine the given utterance.
   - **Check every word** in the utterance against the **spatial dictionary** provided.
   - **List all words** from the utterance that appear in the dictionary.

2. **Assess Usage According to the Rubric:**
   - For each word identified from the dictionary, **determine if it is used in a spatial context** as defined in the rubric and its appendix.
   - Refer to the rubric to understand how spatial words should be used to be considered spatial language.

3. **Identify Additional Spatial Words According to the Rubric:**
   - If no words from the dictionary are found, or if you suspect other words might be spatial, **carefully analyze the utterance for any other spatial words or phrases** according to the rubric.
   - **Consider synonyms or contextually spatial terms** that may not be in the dictionary but fit the rubric's criteria.

4. **Critically Review Your Analysis:**
   - **Double-check** your findings to ensure you have not **missed any spatial words**.
   - **Ensure accuracy** by confirming that all identified words truly meet the spatial criteria without misidentifying non-spatial words.

**Instructions for Your Response:**
- **Provide a detailed reasoning** for your decisions, referencing both the dictionary and the rubric.
- **Conclude with a clear 'yes' or 'no' decision** on whether the utterance contains spatial language.
- **List all spatial words identified**, if any.
- **Use the 'provide_judgment' function** to deliver your response.

**Resources Provided:**
- **Rubric:** {rubric3}
- **Spatial Dictionary:** {spatial_words}
"""

judger_tools = [
    {
        "type": "function",
        "function": {
            "name": "provide_judgment",
            "description": "Provides reasoning and a yes/no decision on whether the utterance contains spatial language.",
            "parameters": {
                "type": "object",
                "properties": {
                    "reasoning": {"type": "string"},
                    "decision": {"type": "string", "enum": ["yes", "no"]},
                    "spatial_words": {
                        "type": "array",
                        "items": {"type": "string"}
                    }
                },
                "required": ["reasoning", "decision", "spatial_words"],
                "additionalProperties": False
            }
        }
    }
]

def is_reasoning_model(model: str) -> bool:
    return model.startswith("gpt-5.5")

def handle_baseline_agent(utterance: str) -> dict:
    if is_reasoning_model(MODEL)
    resp = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Utterance: {utterance}"}
        ],
        temperature=0,
        tools=judger_tools,
        tool_choice={"type": "function", "function": {"name": "provide_judgment"}},
        seed=1234,
    )

    tool_calls = resp.choices[0].message.tool_calls or []
    for tc in tool_calls:
        if tc.function.name == "provide_judgment":
            out = json.loads(tc.function.arguments)
            decision_bin = 1 if out.get("decision", "").lower() == "yes" else 0
            return {
                "spatial": decision_bin,
                "spatial_words_detected": out.get("spatial_words", []) if decision_bin else [],
                "rationale": out.get("reasoning", "")
            }

    return {"spatial": 0, "spatial_words_detected": [], "rationale": ""}


def parse_txt(text: str):
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    return [{"lineNo": i + 1, "speaker": "", "utterance": ln} for i, ln in enumerate(lines)]


def parse_cha(text: str):
    out = []
    current = None
    line_no = 0

    for raw in text.splitlines():
        line = raw.strip("\ufeff")
        if not line.strip():
            continue
        if line.startswith("@"):
            continue

        import re
        m = re.match(r"^\*([A-Za-z0-9_]+):\s*(.*)$", line)
        if m:
            if current:
                out.append(current)
            line_no += 1
            current = {"lineNo": line_no, "speaker": m[1], "utterance": m[2].strip()}
            continue

        if raw.startswith(" ") and current:
            current["utterance"] += " " + line.strip()

    if current:
        out.append(current)
    return out

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/analyze")
async def analyze(files: List[UploadFile] = File(...)):
    rows = []

    for f in files:
        text = (await f.read()).decode("utf-8", errors="ignore")
        name = f.filename.lower()

        parsed = parse_cha(text) if name.endswith(".cha") else parse_txt(text)

        for row in parsed:
            result = handle_baseline_agent(row["utterance"])
            rows.append({
                "file": f.filename,
                "lineNo": row["lineNo"],
                "speaker": row["speaker"],
                "utterance": row["utterance"],
                "spatial": result["spatial"],
                "spatialWordsDetected": result["spatial_words_detected"],
                "rationale": result["rationale"],
            })

    return JSONResponse({"rows": rows})