from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from proekt320ShakirjanovXasan import p1
from funcInoyatov import funcinoyatov 
from funcartur import artur
from pydantic import BaseModel
from functionkostya import konstantin
from funcSoliyev import func_soliyev
from funcIlyas import c2
import os

app = FastAPI( title="umft320 Shakirjanov",
version="1.0.0",
description="Shakirjanov-Платформа для покупки и продажи",
docs_url="/docs",
redoc_url="/redoc",)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montar archivos estáticos (CSS, JS)
current_dir = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(current_dir, "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/")
def read_root():
    return FileResponse(os.path.join(current_dir, "index.html"))
print("                         -----------------bu Shakirjanov reposi------------------")
print(p1(2,3))
print(funcinoyatov(4,4))
print(artur(6,3))
print ("fastapi+uvicorn")





class TwoNumbers(BaseModel):
  x: float
  y: float

@app.get("/c2")
def get_c2(x: float, y: float):
    return {"result": c2(x, y)}
@app.post("/c2")
def post_c2(data: TwoNumbers):
    return {"result": c2(data.x, data.y)}

@app.get("/p1")
def get_p1(x: float, y: float):
    return {"result": p1(x, y)}
@app.post("/p1")
def post_c2(data: TwoNumbers):
    return {"result": p1(data.x, data.y)}

@app.get("/inoyatov")
def get_inoyatov(x: float, y: float ):
    return {"result": funcinoyatov(x, y)}

@app.post("/inoyatov")
def post_inoyatov(data: TwoNumbers):
    return {"result": funcinoyatov(data.x, data.y)}

@app.get("/konstantin")
def get_konstantin(x: float, y: float):
    return {"result": konstantin(x, y)}

@app.post("/konstantin")
def post_konstantin(data: TwoNumbers):
    return {"result": konstantin(data.x, data.y)}

@app.get("/soliyev")
def get_soliyev(x: float, y: float):
    return {"result": func_soliyev(x,y)}

@app.post("/soliyev")
def post_soliyev(data: TwoNumbers):
    return {"result": func_soliyev(data.x, data.y)}