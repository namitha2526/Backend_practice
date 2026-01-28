from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return{"hello":"world"}

@app.get("/item/{health}")
def read_item(health:int, q: Union[str,None]=None):
    return {"health":health,"q":q}
