from app.repository.abstract import BaseRepository
from typing import TypeVar, List
from sqlalchemy.orm import Session

T = TypeVar("T")

class Service:
    def __init__(self, repo: BaseRepository):
        self.repo = repo

    async def create(self, obj: T, db: Session):
        return await self.repo.create(obj, db)
    
    async def get(self, columns: List[str], flag: bool):
        return await self.repo.get(columns, flag)
    
    async def update(self, columns: List[str], flag: bool):
        return await self.repo.update(columns, flag)
    
    async def remove(self, id: str):
        return await self.repo.remove(id)
