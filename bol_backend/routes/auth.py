# routes/auth.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/auth/test")
def test_auth():
    return {"message": "Auth route is working"}
