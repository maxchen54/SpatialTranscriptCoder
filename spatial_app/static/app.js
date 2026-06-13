const folder = document.getElementById("folder");
const run = document.getElementById("run");
const status = document.getElementById("status");
const temperature = document.getElementById("temperature");
const temperatureValue = document.getElementById("temperatureValue");
const model = document.getElementById("model");
const reasoningEffort = document.getElementById("reasoningEffort");
const clear = document.getElementById("clear");
const agentMode = document.getElementById("agentMode");

temperature.addEventListener("input", () => {
  temperatureValue.textContent = temperature.value;
});

function setStatus(msg) {
  status.textContent += msg + "\n";
}

function updateReasoningVisibility() {
  const isReasoning =
    model.value.startsWith("gpt-5.5");

  reasoningEffort.disabled = !isReasoning;

  reasoningEffort.parentElement.style.opacity =
    isReasoning ? "1" : "0.5";
}

model.addEventListener("change", updateReasoningVisibility);

updateReasoningVisibility();

run.addEventListener("click", async () => {
  console.log("Run button clicked");
  console.log("window location:", window.location.href);

  const files = Array.from(folder.files || []).filter(f =>
    [".txt", ".cha", ".csv", ".xlsx"].some(ext => f.name.toLowerCase().endsWith(ext))
  );

  console.log("Filtered files:", files);

  if (!files.length) {
    setStatus("No .txt, .cha, .csv, or .xlsx files selected.");
    return;
  }

  const form = new FormData();
  for (const f of files) {
    form.append("files", f);
  }
  form.append("temperature", temperature.value);
  form.append("model", model.value);
  form.append("reasoning_effort", reasoningEffort.value);
  form.append("agent_mode", agentMode.value);

  console.log("About to call fetch /analyze-xlsx");
  setStatus(`Uploading ${files.length} files...`);
  setStatus(`Model: ${model.value}`);
  setStatus(`Reasoning effort: ${reasoningEffort.value}`);  
  setStatus(`Temperature: ${temperature.value}`);

  try {
    const res = await fetch("/analyze-xlsx", {
      method: "POST",
      body: form
    });

    console.log("Fetch returned:", res.status, res.statusText);
    setStatus(`Server responded: ${res.status}`);

    if (!res.ok) {
      const errText = await res.text();

      console.error("Response not OK:", errText);

      setStatus("Analyze failed.");
      setStatus(errText);

      return;
    }

    console.log("About to read blob...");
    setStatus("Reading XLSX blob...");

    const blob = await res.blob();

    console.log("Blob received:", blob);
    console.log("Blob size:", blob.size);

    setStatus(`Blob received (${blob.size} bytes)`);

    const url = URL.createObjectURL(blob);

    console.log("Created download URL.");

    const a = document.createElement("a");

    a.href = url;
    a.download = "spatial_results.xlsx";

    document.body.appendChild(a);

    console.log("Triggering download...");
    a.click();

    a.remove();

    URL.revokeObjectURL(url);

    console.log("Download completed.");

    setStatus("Done. XLSX downloaded.");

  } catch (err) {
    console.error("Request/download failed:", err);

    setStatus(
      "Request/download failed: " +
      (err?.message || String(err))
    );
  }
});

clear.addEventListener("click", () => {
  folder.value = "";
  status.textContent = "";
});