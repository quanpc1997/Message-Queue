from abc import ABC
from typing import TypeVar, List

T = TypeVar("T")

class BaseRepository(ABC):
    
    async def create(self, obj: T):
        raise NotImplementedError
    
    async def get(self, columns: List[str], flag: bool):
        """
            flag: 
                - True: including
                - False: excluding
        """
        raise NotImplementedError

    async def update(self, columns: List[str], flag: bool):
        """
            flag: 
                - True: including
                - False: excluding
        """
        raise NotImplementedError
    
    async def remove(self, id: str):
        raise NotImplementedError