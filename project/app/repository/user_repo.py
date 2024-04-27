from sqlalchemy.orm import Session
from .abstract import BaseRepository
from app.schemas.user import UserSchema
from app.models.user import User
from loguru import logger


class UserRepo(BaseRepository):

    async def create(self, user_schema: UserSchema, db: Session):
        logger.info(f"db = {db}")
        new_user = User(
            username=user_schema.username,
            password=user_schema.password,
            email=user_schema.email
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user.dict()