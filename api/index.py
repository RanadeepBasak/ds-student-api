from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json
import os

app = FastAPI()

# Enable CORS to allow GET requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load student marks from JSON file
with open(os.path.join(os.path.dirname(__file__), "marks.json")) as f:
    data = json.load(f)

# Convert to dictionary for faster lookup
marks_dict = {student["name"]: student["marks"] for student in data}

@app.get("/")
async def get_marks(name: List[str] = []):
    result = [marks_dict.get(n, None) for n in name]
    return {"marks": result}
