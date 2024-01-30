from fastapi import FastAPI # import the FastAPI class from the fastapi module

app = FastAPI() # create an instance of the FastAPI class

@app.get("/") # decorator / endpoint
def home(): # function
    return {"message": "Hello World"}

# to run the server
# uvicorn main:app --reload

# Features of FastAPI
# automatic documentation of API

# swagger UI
# redoc UI

# http://localhost:8000/docs
# http://localhost:8000/redoc