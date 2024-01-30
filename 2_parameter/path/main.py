# path parameter in FastAPI

# Path parameters are variable parts of a URL path. 
# They are typically used to point to a specific resource within a collection, such as a user identified by ID.

# Path parameters are always defined in path operation decorator paths,


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}

# path parameter
@app.get("/about")
def about(about):
    return {"message": about}

# url http://127.0.0.1:8000/about

# path parameter with type validation
# fastapi uses pydantic for type validation

@app.get("/blog/all")
def get_all_blogs():
    return {"blogs": "all blogs"}

@app.get("/blog/{id}")
def blog(id: int):
    return {"blog no": id}

# url http://127.0.0.1:8000/blog/5

# @app.get("/blog/all")
# def get_all_blogs():
#     return {"blogs": "all blogs"}

# it will give error because fastapi will consider all as int
# to resolve this issue we can place this path parameter above => blog/{id}

#### *** Here order of operation is important

# path parameter with type validation and default value
@app.get("/blog/{id}/comments")
def comments(id: int, limit: int = 10):
    return {"blog no": id, "comments": limit}



