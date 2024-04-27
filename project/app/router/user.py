from fastapi import APIRouter, Depends, HTTPException, status
from app.repository.user_repo import UserRepo
from app.services.service import Service
from app.schemas.user import UserSchema
from sqlalchemy.orm import Session
from app.dbs.postgres import get_db


from loguru import logger

user_router = APIRouter(prefix="/user", tags=["User"])

async def get_user_service():
    return Service(UserRepo())

@user_router.post("/create/")
async def create(user: UserSchema, db: Session = Depends(get_db), service: Service = Depends(get_user_service)):
    try:
        result = await service.create(obj=user, db=db)
        logger.debug(f"result = {result}")
    except Exception as e:
         logger.error(e)
         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e)