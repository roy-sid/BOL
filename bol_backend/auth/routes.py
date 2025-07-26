from fastapi import APIRouter, HTTPException
from bol_backend.db import db
from bol_backend.models.user import User, UserLogin
from bol_backend.auth.hash import hash_password, verify_password
from bol_backend.auth.jwt_handler import create_access_token

router = APIRouter()

@router.post("/signup")
def signup(user: User):
    if db.users.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already exists")
    
    hashed_pw = hash_password(user.password)
    db.users.insert_one({"email": user.email, "password": hashed_pw})
    return {"message": "User created successfully"}

@router.post("/login")
def login(user: UserLogin):
    db_user = db.users.find_one({"email": user.email})
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
