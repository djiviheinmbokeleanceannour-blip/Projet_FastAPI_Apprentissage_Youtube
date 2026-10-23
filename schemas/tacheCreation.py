from pydantic import BaseModel,Field
from enum import Enum
from datetime import date
class Etat(str,Enum):
    AFAIRE="A faire"
    ENCORE="En cours"
    TERMINEE="Terminée"

class TacheCreation(BaseModel):
    titre: str = Field(min_length=1) #field permet d'imposer à l'utilisateur des trucs sur la chaine
    description: str = Field(min_length=1)
    etat: Etat
    dateEch:date
    dateCre:date=date.today()
    dateMaj: date=date.today()