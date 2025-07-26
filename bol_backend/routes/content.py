# bol_backend/routes/content.py

from fastapi import APIRouter, Query
from pydantic import BaseModel
from bol_backend.db import db


router = APIRouter()

# Cultural content route
@router.get("/get-cultural-content")
def get_cultural_content():
    return {"story": "Once upon a time...", "food": "Litti Chokha", "song": "Chalte Chalte"}

# Translate route
@router.get("/translate")
def translate(word: str = Query(..., description="Word to translate"), language: str = "hi"):
    translations = {
        "apple": {"hi": "सेब", "bn": "আপেল"},
        "banana": {"hi": "केला", "bn": "কলা"},
        "car": {"hi": "गाड़ी", "bn": "গাড়ি"},
    }

    if word.lower() in translations and language in translations[word.lower()]:
        return {
            "word": word,
            "translation": translations[word.lower()][language],
            "example": f"This is a {translations[word.lower()][language]}"
        }
    else:
        return {"error": "Translation not found"}

# Pydantic model for /submit-story
class Story(BaseModel):
    title: str
    language: str
    content: str

# Submit story route
@router.post("/submit-story")
def submit_story(story: Story):
    story_dict = story.dict()
    result = db.stories.insert_one(story_dict)

    print("Story inserted with ID:", result.inserted_id)

    return {
        "message": "Story saved successfully",
        "id": str(result.inserted_id)
    }
