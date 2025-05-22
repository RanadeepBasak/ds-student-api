from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load marks.json
with open(os.path.join(os.path.dirname(__file__), "marks.json")) as f:
    data = json.load(f)

# Convert to a dictionary for quick lookup
marks_dict = {student["name"]: student["marks"] for student in data}

@app.get("/api")
def get_marks(name: list[str] = Query([])):
    # Get marks for each name in order
    marks = [marks_dict.get(n, None) for n in name]
    return {"marks": marks}