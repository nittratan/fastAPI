# summary & description
from fastapi import FastAPI

app = FastAPI()

@app.get(
    '/blog/all',
    tags=['blog'],
    summary='Get all blogs',
    description='this api call simulate fatching all blogs from the database',
    response_description='List of blogs'
    )
def get_all_blogs():
    return {"data": "all blogs"}
