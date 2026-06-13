

spatial_words = [
  "about", "above", "across", "air", "after", "against", "ahead", "all", "along", "among", "amount", "amounts",
  "angle", "angles", "anterior", "anywhere", "apart", "arc", "arcs", "area", "around", "aside", "at", "atlas",
  "attribute", "atop", "avenue", "away", "axes", "axis", "back", "backward", "barrier", "basemap", "before",
  "behind", "below", "bend", "bending", "bends", "bendy", "beneath", "bent", "beside", "between", "beyond",
  "big", "bigger", "biggest", "bit", "bits", "border", "both", "bottom", "bottomless", "breadth", "brink",
  "broad", "broader", "broadest", "buffer", "bumfuck", "bump", "bumped", "bumps", "bumpy", "by", "capacit",
  "ceiling", "center", "central", "centre", "centimeter", "centimeters", "circle", "circles", "circular", "city",
  "close", "closed", "closely", "closer", "closest", "column", "cone", "cones", "conical", "connection", "contain",
  "coordinates", "corner", "corners", "counties", "countr", "county", "coverage", "cube", "cubes", "curve", "curved",
  "curves", "curvy", "cylinder", "cylinders", "cylindric", "cylindrical", "data", "decrease", "decreased",
  "decreases", "decreasing", "deep", "deeper", "deepest", "deeply", "dense", "densit", "depth", "design", "designs",
  "diagonal", "diamond", "diamonds", "dimension", "direct", "direction", "directly", "dissolve", "distal", "distan",
  "district", "door", "down", "downer", "downhill", "downstairs", "downtown", "downward", "earth", "east", "edge",
  "eight", "eights", "ellipse", "ellipses", "elliptical", "elsewhere", "emptier", "emptiest", "emptiness", "empty",
  "emtpie", "enclos", "encompass", "enorm", "enough", "entrance", "environment", "equal", "everywhere", "exit",
  "expand", "exterior", "far", "farer", "farest", "farther", "farthest", "fat", "fatter", "fattest", "feet", "fifth",
  "fifths", "fill", "first", "fit", "flat", "flatter", "flattest", "flip", "flipped", "flipping", "flips", "floor",
  "foot", "forward", "forwarded", "forwarding", "forwards", "foundation", "fraction", "fractions", "fragment",
  "fragments", "from", "front", "full", "fuller", "fullest", "fullness", "fully", "further", "furthering", "gap",
  "gate", "giant", "gigantic", "ginormous", "GIS", "global", "globe", "globes", "ground", "half", "hall", "halves",
  "head", "headed", "heading", "heads", "height", "here", "hexagon", "hexagons", "high", "higher", "highest", "hole",
  "horizontal", "huge", "hugely", "huger", "hugest", "in", "inch", "increase", "increased", "increases", "increasing",
  "indirect", "inferior", "inner", "inside", "insides", "interior", "internal", "internally", "internation",
  "intersect", "intertwine", "intertwined", "into", "itsy-bitsy", "itty-bitty", "join", "joined", "kilometer", "km",
  "land", "large", "largely", "larger", "largest", "last", "lateral", "latitude", "layer", "ledge", "left", "leftward",
  "lengthwise", "length", "lengths", "less", "level", "levels", "lil", "lil'", "line", "linear", "lines", "link",
  "little", "littler", "littlest", "local", "locale", "localis", "localit", "localiz", "locally", "locals", "locat",
  "long", "longer", "longest", "longitud", "lot", "low", "lower", "lowered", "lowering", "lowers", "lowest", "lowli",
  "lowly", "lump", "lumps", "lumpy", "map", "mapped", "mapping", "maps", "mass", "massive", "measure", "measurements",
  "measures", "medial", "meter", "metre", "mid", "middle", "mile", "mixed", "model", "more", "much", "narrow",
  "narrowed", "narrower", "narrowest", "narrowing", "narrowly", "narrowness", "narrows", "nation", "national",
  "nationality", "nationally", "nationals", "nations", "near", "nearby", "neared", "nearer", "nearest", "nearing",
  "nears", "neighbor", "neighbour", "next", "ninth", "ninths", "none", "north", "nowhere", "octagon", "octagons", "off",
  "on", "onto", "open", "opened", "opening", "opens", "opposite", "order", "orders", "orientation", "orientations",
  "out", "outer", "outside", "outsides", "outward", "oval", "ovals", "over", "overflow", "overlap", "parallel",
  "parallelogram", "parallelograms", "part", "parts", "past", "path", "paths", "pattern", "patterns", "pentagon",
  "pentagons", "perpedicular", "perpendicular", "piece", "pieces", "place", "placed", "placement", "places", "placing",
  "plane", "planes", "platform", "point", "pointed", "points", "pointy", "polygon", "portion", "portions", "position",
  "posterior", "provinc", "proxima", "proximity", "pyramid", "pyramids", "quadrilateral", "quadrilaterals", "quarter",
  "quarters", "rectangle", "rectangles", "rectangular", "region", "remote", "repeat", "repeated", "repeating",
  "repeats", "repetition", "reverse", "rhombus", "rhombuses", "right", "rightward", "rise", "road", "room", "roomate",
  "roomed", "roomie", "rooming", "roommate", "rooms", "rotate", "rotated", "rotates", "rotating", "rotation",
  "rotations", "round", "rounded", "rounder", "roundest", "route", "row", "rows", "same", "section", "sections",
  "sector", "segment", "semicircle", "semicircles", "separat", "sequence", "sequences", "seventh", "sevenths",
  "shallow", "shallower", "shallowest", "shape", "shaping", "short", "shorter", "shortest", "shortly", "shut", "side",
  "sided", "sides", "sideways", "siding", "sit", "site", "sites", "sits", "sitting", "sixth", "sixths", "size",
  "sizes", "skinnier", "skinniest", "skinny", "sky", "small", "smaller", "smallest", "some", "somewhere", "south",
  "space", "spaced", "spaces", "spaci", "span", "spann", "spatial", "sphere", "spheres", "spheric", "spherical",
  "split", "sprawl", "square", "squares", "stair", "stay", "stayed", "staying", "stays", "straight", "straighter",
  "straightest", "street", "stretch", "stuck", "superior", "surfac", "surround", "symmetric", "symmetrical", "symmetry",
  "tall", "taller", "tallest", "teeny", "tenth", "tenths", "territor", "there", "thick", "thin", "thinly", "thinned",
  "thinner", "thinnest", "third", "thirds", "through", "throughout", "tinier", "tiniest", "tiny", "to", "together",
  "top", "toward", "town", "triangle", "triangles", "triangular", "turn", "turned", "turning", "turns", "under",
  "underneath", "undersid", "universe", "up", "upon", "upper", "uppermost", "upright", "upstairs", "upto", "upward",
  "vast", "vastly", "vastness", "verg", "vertical", "via", "volume", "volumes", "wall", "walls", "warehous", "wave",
  "waves", "wavey", "way", "west", "where", "where'd", "where's", "wheres", "wherever", "whole", "wholes", "wide",
  "widely", "wider", "widest", "width", "with", "within", "world"
]

rubric3 = [
    {
        "guideline_name": "Guideline for Identifying Characteristics of Conversational Language Indicative of Spatial Thinking",
        "categories": [
            {
                "guideline_title": "Use of Spatial Prepositions and Vocabulary",
                "characteristics": [
                    "Frequent use of spatial prepositions such as 'above,' 'below,' 'next to,' 'under,' 'between,' 'behind,' and 'in front of.'",
                    "More specific vocabulary when describing positions or relationships, including words like 'adjacent,' 'parallel,' 'perpendicular,' 'overlap,' or 'rotate.'",
                    "Dynamic spatial terms: Words that indicate movement in space, such as 'toward,' 'away from,' 'across,' or 'diagonally.'"
                ]
            },
            {
                "guideline_title": "Describing Relative Positions and Orientations",
                "characteristics": [
                    "Describing the relative positions of objects, e.g., 'The book is to the left of the lamp.'",
                    "Mentioning angles, orientations, or rotations, e.g., 'Rotate the chair 90 degrees clockwise.'",
                    "Describing how objects relate to each other in a given context, e.g., 'The car is parked behind the house, next to the tree.'"
                ]
            },
            {
                "guideline_title": "Ability to Express Mental Manipulation of Objects",
                "characteristics": [
                    "Language reflecting mental rotation or manipulation, such as 'If you turn the object upside down…' or 'Imagine moving the box to the left.'",
                    "Ability to explain changes in position or perspective, e.g., 'When you flip the piece, the curved side will face down.'"
                ]
            },
            {
                "guideline_title": "Directional Language",
                "characteristics": [
                    "Use of directions to describe movement or locations: 'Go north, then take a right,' or 'Move forward until you reach the corner.'",
                    "Inclusion of reference points or landmarks when describing directions: 'The store is next to the park, behind the tall building.'"
                ]
            },
            {
                "guideline_title": "Detail in Describing Shapes, Sizes, and Dimensions",
                "characteristics": [
                    "Precise descriptions of shapes and their properties, such as 'The object is a square with equal sides' or 'The triangle is an equilateral triangle.'",
                    "Descriptions involving dimensions: 'The room is 10 feet long and 8 feet wide.'",
                    "Observations on proportions: 'The smaller circle fits inside the larger one.'"
                ]
            },
            {
                "guideline_title": "Spatial Reasoning in Problem-Solving Language",
                "characteristics": [
                    "Problem-solving using spatial terms, such as 'If we move this piece here, we’ll have more space for the rest.'",
                    "Using spatial reasoning to plan or predict outcomes, e.g., 'If we stack the boxes this way, they’ll fit better.'",
                    "Describing how changes in arrangement will affect spatial outcomes: 'If you place the object on top, it will be easier to reach.'"
                ]
            },
            {
                "guideline_title": "Use of Comparisons to Explain Spatial Relationships",
                "characteristics": [
                    "Making comparisons between objects to explain spatial relationships: 'The chair is taller than the table, but not as wide.'",
                    "Using analogies to describe spatial relationships, such as, 'It’s like how puzzle pieces fit together.'"
                ]
            },
            {
                "guideline_title": "Engagement with Visual or Gestural Aids",
                "characteristics": [
                    "Frequently using gestures or pointing to emphasize spatial relationships during conversation: 'It’s over here' (while pointing), or 'Turn it this way' (while rotating hands).",
                    "Drawing diagrams or sketching to supplement spatial explanations: 'Let me draw it out to show you how the parts fit.'"
                ]
            },
            {
                "guideline_title": "Perspective-Taking Language",
                "characteristics": [
                    "Adopting different points of view when discussing objects or spaces: 'If you look from above, you’ll see the whole layout,' or 'From the side, it looks much longer.'",
                    "Describing what things look like from various perspectives: 'Imagine seeing it from the back—what changes?'"
                ]
            },
            {
                "guideline_title": "Use of Temporal-Spatial Reasoning",
                "characteristics": [
                    "Combining spatial and temporal concepts in descriptions: 'When you move forward 10 steps, you’ll be halfway there.'",
                    "Describing events in space with reference to time: 'We’ll pass the first building after 5 minutes of walking.'"
                ]
            }
        ]
    }
]