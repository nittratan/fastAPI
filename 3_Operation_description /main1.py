# tags in fastapi

from fastapi import FastAPI, HTTPException, status , Response

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get(
    "/blog/{blog_id}", 
    status_code=status.HTTP_200_OK , 
    tags=['blog'])
def get_blog(blog_id: int , response : Response):
    if blog_id>5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"blog id not found": blog_id}
        # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    else:
        response.status_code= status.HTTP_200_OK
        return {"blog": blog_id}
    
@app.get('/blog/comments/{comment_id}', tags=['comments'])
def get_comments(comment_id : int):
    return {"comment id": comment_id}