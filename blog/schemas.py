from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class Blog(BaseModel):
    title: str
    body: str