from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import os
import json

app = FastAPI()

# Enable CORS (GET requests from any origin)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load marks.json
with open(os.path.join(os.path.dirname(__file__), "marks.json")) as f:
    data = json.load(f)

# Convert to dict for fast lookup
marks_dict = {entry["name"]: entry["marks"] for entry in data}

@app.get("/api")
def get_marks(name: list[str] = []):
    result = [marks_dict.get(n, None) for n in name]
    return {"marks": result}
