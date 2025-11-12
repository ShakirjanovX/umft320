from fastapi import FastAPI
import proekt320ShakirjanovXasan as p1
import funcktiaInoyatov as p2
from funcartur import artur

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

print(p1.func1(2,3))
print(p2.funk2Inoyatov(4,4))
print(artur(6,3))
print ("fastapi+uvicorn")
