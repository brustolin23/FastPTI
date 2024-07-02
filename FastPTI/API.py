from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn as uv

class Inputs(BaseModel):
    i1: int
    i2: str




app = FastAPI()

@app.get("/exemplo")
def example () -> str:
    return "Olá Mundo"
@app.post("/exemplo2")
def example2 (inputs: Inputs) -> str:
    return inputs.i2

if __name__ == "__main__":
    uv.run(app, port=5971)