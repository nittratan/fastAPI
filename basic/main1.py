from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def index():
  return {"Hello": "World"}

@app.get("/about")
def aboutUs():
  return {"College": "NIT, Trichy"}

# method 1

# if __name__ == "__main__":
#   uvicorn.run("main1:app", host="localhost", port=8000 , reload=True)

# method 2

if __name__ == "__main__":
    uvicorn.run("main1:app", host="127.0.0.1", port=5000, reload=True)
