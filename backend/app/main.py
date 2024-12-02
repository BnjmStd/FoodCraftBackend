# pip install fastapi uvicorn
# model = pickle.load(open('./model/model.pkl', 'rb'))

from fastapi import FastAPI, HTTPException
import pickle
from db.session import init_models, engine


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

if __name__ == "__main__":
    init_models()

# Iniciar la aplicación con uvicorn:
# uvicorn main:app --reload
