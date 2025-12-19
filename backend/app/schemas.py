from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime
from typing import Optional, Dict, Any

class TenantCreate(BaseModel):
    name: str

class TenantResponse(BaseModel):
    id: UUID
    name: str
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

class AppCreate(BaseModel):
    name: str
    config: Optional[Dict[str, Any]] = {}

class AppResponse(BaseModel):
    id: UUID
    name: str
    tenant_id: UUID
    config: Dict[str, Any]
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

class DocumentResponse(BaseModel):
    id: UUID
    filename: str
    status: str
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)
