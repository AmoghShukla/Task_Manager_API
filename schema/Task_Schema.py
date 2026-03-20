from pydantic import BaseModel
from typing import Optional

class TaskCreate(BaseModel):
    title : str
    description : str

class TaskResponse(BaseModel):
    id : int
    title : str
    description : Optional[str]
    completed : bool


class TaskUpdate(BaseModel):
    id : Optional[int]
    title : Optional[str]
    description : Optional[str]
