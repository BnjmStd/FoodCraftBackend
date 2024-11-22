# pip install fastapi uvicorn
# model = pickle.load(open('./model/model.pkl', 'rb'))

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle

app = FastAPI()

@app.get("/")
async def welcome():
    data = {
        "message": "Bienvenido a MetaFoodCraft",
        "status": "success",
        "items": ["🍌", "🍏", "🍉", "🥝"]
    }
    return data

@app.get("/new")
async def new_user():
    return {"message": "Datos recibidos", "data": '🍉'}

# Iniciar la aplicación con uvicorn:
# uvicorn main:app --reload
