from fastapi import FastAPI

# Import routers with full package paths
from bol_backend.auth.routes import router as auth_router
from bol_backend.routes.detect import router as detect_router
from bol_backend.routes.content import router as content_router

app = FastAPI()

# Register all routers
app.include_router(auth_router)
app.include_router(detect_router)
app.include_router(content_router)

@app.get("/")
def root():
    return {"message": "jai shri ram"}
