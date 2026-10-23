from sqlalchemy import create_engine #create engine permet de creer la connection avec la base de donnée
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Charger les variables du fichier .env
load_dotenv()

# Récupérer l'URL de la BDD depuis l'environnement
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()