from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List
from uuid import UUID

from app.core.db import get_db
from app.models.core import Tenant, App, Document
from app.schemas import TenantCreate, TenantResponse, AppCreate, AppResponse

router = APIRouter()

@router.post("/tenants/", response_model=TenantResponse)
async def create_tenant(tenant: TenantCreate, db: AsyncSession = Depends(get_db)):
    new_tenant = Tenant(name=tenant.name)
    db.add(new_tenant)
    await db.commit()
    await db.refresh(new_tenant)
    return new_tenant

@router.get("/tenants/", response_model=List[TenantResponse])
async def list_tenants(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Tenant))
    return result.scalars().all()

@router.post("/tenants/{tenant_id}/apps/", response_model=AppResponse)
async def create_app(tenant_id: UUID, app: AppCreate, db: AsyncSession = Depends(get_db)):
    # Verify tenant exists
    tenant = await db.get(Tenant, tenant_id)
    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")
        
    new_app = App(name=app.name, tenant_id=tenant_id, config=app.config)
    db.add(new_app)
    await db.commit()
    await db.refresh(new_app)
    return new_app
