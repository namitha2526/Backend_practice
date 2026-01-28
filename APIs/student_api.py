from typing import Union
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return{"hello":"word"}

@app.get("/student/{id}")
def read_name(id:int):
    return{"student_id" :id}

@app.get("/student/{id}/marks")
def root_name(id: int,subject:Union[str,None]=None):
    return{"student_id":id,"subject":subject}
