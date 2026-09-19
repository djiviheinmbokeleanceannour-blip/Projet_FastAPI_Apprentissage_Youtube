from pydantic import BaseModel,Field
from enum import Enum

class Etat(str,Enum):
    AFAIRE="A faire"
    ENCORE="En cours"
    TERMINEE="Terminée"

class Tache(BaseModel):
    titre: str = Field(min_length=1) #field permet d'imposer à l'utilisateur des trucs sur la chaine
    description: str = Field(min_length=1)
    etat: Etat