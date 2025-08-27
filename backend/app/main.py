from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import chat, products, health

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router)
app.include_router(products.router)
app.include_router(health.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Supermarket Assistant API"}