# query parameter in FastAPI
# A query parameter is a set of key-value pairs that are attached to the end of a URL. 
# They are used to provide additional information to a web server when making requests.

# http://localhost:8000/blog/all?page=2&page_size=10

# here page and page_size are query parameters

# any function parameter that is not part of the path will be interpreted as a query parameter

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello World"}

@app.get("/blog/all")
def get_all_blogs(page,page_size):
    return {"massage": f'all blogs on page {page} with page size {page_size}'}