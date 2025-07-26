from fastapi import APIRouter, File, UploadFile, Query
import uuid
import shutil
from pathlib import Path
import torch
from bol_backend.routes.content import translate  # Import from your own translate route
from bol_backend.db import db

router = APIRouter()

# Load YOLOv5 model once
model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5s.pt', force_reload=True)

def detect_objects(image_path):
    results = model(image_path)
    detections = results.pandas().xyxy[0]
    return detections['name'].tolist()

@router.post("/detect")
async def detect(file: UploadFile = File(...), language: str = Query("hi", description="Translation language")):
    # Save uploaded file temporarily
    temp_file = f"temp_{uuid.uuid4().hex}.jpg"
    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Run detection
    detected_objects = detect_objects(temp_file)

    # Clean up
    Path(temp_file).unlink()

    if not detected_objects:
        return {"detected": [], "translation": None, "cultural_content": None}

    # Use only the first detected object
    detected = detected_objects[0]

    # Call translate function
    translation_result = translate(word=detected, language=language)

    # Lookup cultural content from MongoDB
    content = db.stories.find_one({"title": detected})
    cultural_info = {
        "title": content.get("title") if content else None,
        "language": content.get("language") if content else None,
        "content": content.get("content") if content else None
    }

    return {
        "detected": detected,
        "translation": translation_result,
        "cultural_content": cultural_info
    }
