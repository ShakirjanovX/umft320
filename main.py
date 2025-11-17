from fastapi import FastAPI
import proekt320ShakirjanovXasan as p1
import funcktiaInoyatov as p2
from funcartur import artur
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

print(p1.func1(2,3))
print(p2.funk2Inoyatov(4,4))
print(artur(6,3))
print ("fastapi+uvicorn")


app = FastAPI( title="MMM",
version="1.0.0",
description="Платформа для покупки и продажи",
docs_url="/docs",
redoc_url="/redoc",)

class TwoNumbers(BaseModel):
  x: float
  y: float

@app.get("/c2")
def get_c2(x: float, y: float):
 return {"result": p1.func1(x,y)}

@app.post("/c2")
def post_c2(data: TwoNumbers):
 return {"result": p1.func1(data.x, data.y)}