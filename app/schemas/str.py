from pydantic import BaseModel
from typing import List

class StringListRequest(BaseModel):
    comments: str

class StringListResponse(BaseModel):
    response: str