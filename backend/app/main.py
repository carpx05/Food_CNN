from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
from core.logging import setup_logging
from fastapi_cache import FastAPICache

setup_logging()


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

setup_logging()

app.include_router(classify.router, prefix="/api/v1/classify", tags=["classify"])
# app.include_router(quantify.router, prefix="/api/v1/quantify", tags=["quantify"])
app.router.redirect_slashes = False


@app.on_event("startup")
async def startup_event():
    FastAPICache.init()


@app.get("/", tags=["root"])
async def read_root():
    return {"message": "Welcome to Food Calorie Estimation!"}


@app.get("/health", tags=["health"])
async def health():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)