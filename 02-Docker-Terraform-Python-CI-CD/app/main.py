from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timezone
from typing import List, Dict

from app.config import settings
from app.models import HealthCheckResponse, ItemBase, ItemCreate, ItemResponse, MetricsResponse

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="DevOps Assignment 3 - Production-ready FastAPI REST API with Docker, Terraform, and CI/CD"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage for demonstration purposes
items_db: Dict[int, dict] = {
    1: {
        "id": 1,
        "name": "Initial DevOps Workflow",
        "description": "FastAPI + Docker + Terraform + CI/CD Setup",
        "category": "devops",
        "created_at": datetime.now(timezone.utc).isoformat()
    }
}
item_id_counter = 2


@app.get("/", tags=["Root"])
def read_root():
    return {
        "message": f"Welcome to {settings.APP_NAME}",
        "version": settings.APP_VERSION,
        "docs_url": "/docs",
        "health_url": "/health"
    }


@app.get("/health", response_model=HealthCheckResponse, tags=["Health"])
def health_check():
    return HealthCheckResponse(
        status="healthy",
        timestamp=datetime.now(timezone.utc).isoformat(),
        version=settings.APP_VERSION,
        environment=settings.ENV
    )


@app.get("/api/v1/items", response_model=List[ItemResponse], tags=["Items"])
def get_items():
    return list(items_db.values())


@app.get("/api/v1/items/{item_id}", response_model=ItemResponse, tags=["Items"])
def get_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {item_id} not found"
        )
    return items_db[item_id]


@app.post("/api/v1/items", response_model=ItemResponse, status_code=status.HTTP_201_CREATED, tags=["Items"])
def create_item(item: ItemCreate):
    global item_id_counter
    new_item = {
        "id": item_id_counter,
        "name": item.name,
        "description": item.description,
        "category": item.category,
        "created_at": datetime.now(timezone.utc).isoformat()
    }
    items_db[item_id_counter] = new_item
    item_id_counter += 1
    return new_item


@app.delete("/api/v1/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Items"])
def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {item_id} not found"
        )
    del items_db[item_id]
    return None


@app.get("/api/v1/metrics", response_model=MetricsResponse, tags=["Metrics"])
def get_metrics():
    return MetricsResponse(
        app_name=settings.APP_NAME,
        uptime_status="UP",
        total_items=len(items_db),
        system_info={
            "environment": settings.ENV,
            "python_framework": "FastAPI",
            "server": "Uvicorn"
        }
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host=settings.HOST, port=settings.PORT, reload=settings.DEBUG)
