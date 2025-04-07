from fastapi import FastAPI, Request
from pydantic import BaseModel
#from yolov8_model import process_image
import os

app = FastAPI()

class ImagePath(BaseModel):
    image_path: str

@app.post("/detect/")
async def detect_image(data: ImagePath):
    image_path = data.image_path
    output_path = process_image(image_path)
    return {"output_image_path": output_path}

@app.get("/test/")
async def detect_image(data: ImagePath):
    return {"Output": "Hello World"}