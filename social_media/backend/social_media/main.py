from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from social_media.routers.post import router as post_router

origins = [
    "http://localhost",
    "http://127.0.0.1:5500",
]

app = FastAPI()

app.include_router(post_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

