from sqlmodel import Field, Session, SQLModel, create_engine, select
from dotenv import load_dotenv
import os

# variables de entorno
load_dotenv()

# Leer la URL 
DATABASE_URL = os.getenv("DATABASE_URL")
print(f"DATABASE_URL: {DATABASE_URL}")  

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the environment variables")

# Crear el motor
try:
    engine = create_engine(DATABASE_URL)
    print("Engine created successfully.")  
except Exception as e:
    print(f"Error creating engine: {e}")
    raise

# Probar la conexión con la base de datos
try:
    with Session(engine) as session:
        print("Database connection successful!")
except Exception as e:
    print(f"Error connecting to the database: {e}")
    raise


def init_models():
    SQLModel.metadata.create_all(engine)
    print("Database tables created")
