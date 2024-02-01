# status code in fastapi 
# 200: OK
# 201: Created
# 202: Accepted
# 400: Bad Request
# 401: Unauthorized
# 403: Forbidden
# 404: Not Found

# 500: Internal Server Error
# 503: Service Unavailable
# 504: Gateway Timeout

from fastapi import FastAPI, HTTPException, status , Response

app = FastAPI()

@app.get("/")
def home():
    return {"Data": "Test"}

@app.get("/items/{item_id}", status_code=404)
def get_item(item_id: int):
    if item_id>5:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return {"item": item_id}

# in the above code we have used status_code=404 in the path operation decorator if we pass item id = 3
# it return also 404
# if we pass item id = 6 it return 404 with message "Item not found"

@app.get("/blog/{blog_id}", status_code=status.HTTP_200_OK)
def get_blog(blog_id: int , response : Response):
    if blog_id>5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"blog id not found": blog_id}
        # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    else:
        response.status_code= status.HTTP_200_OK
        return {"blog": blog_id}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)