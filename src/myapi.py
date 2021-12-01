from fastapi import FastAPI
from pydantic import BaseModel
import git

class Subject(BaseModel):
    subject: str
    title: str
    author: str
    des: str
    url: str

subject_db = [
    {
        'subject':'Math',
        'title': 'Math01',
        'author': 'Idiot',
        'des': 'Yeah',
        'url': 'https://youtu.be/1OO5LnnGPtg',
    },
    {
        'subject': 'Introduction',
        'title': 'PR staff',
        'author': 'Yeah?',
        'des': 'hEllo Yo man',
        'url': 'https://youtu.be/1OO5LnnGPtg',
    },
]

app = FastAPI()

@app.get("/")
async def root():
    return subject_db