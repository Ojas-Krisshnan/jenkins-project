from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from datetime import datetime

class HealthCheckResponse(BaseModel):
    status: str = Field(..., example="healthy")
    timestamp: str = Field(..., example="2026-08-12T13:00:00Z")
    version: str = Field(..., example="1.0.0")
    environment: str = Field(..., example="development")

class ItemBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, example="DevOps Task")
    description: Optional[str] = Field(None, example="Automated pipeline configuration")
    category: str = Field(default="general", example="infrastructure")

class ItemCreate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: int = Field(..., example=1)
    created_at: str = Field(..., example="2026-08-12T13:00:00Z")

class MetricsResponse(BaseModel):
    app_name: str
    uptime_status: str
    total_items: int
    system_info: Dict[str, str]
