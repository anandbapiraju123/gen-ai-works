from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .router import router



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Authorization"],
)

# --- Routers ---
app.include_router(router)
