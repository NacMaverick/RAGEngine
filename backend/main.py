from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Connect to DB, Redis, Typesense
    print("Starting up RAGEngine API...")
    yield
    # Shutdown: Close connections
    print("Shutting down...")

app = FastAPI(
    title="RAGEngine API",
    description="Multi-tenant RAG Platform API",
    version="0.1.0",
    lifespan=lifespan
)

# CORS Configuration
origins = ["*"]  # In production, specific domains only

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "api-gateway"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
