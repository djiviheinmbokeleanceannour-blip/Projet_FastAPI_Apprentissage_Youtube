from fastapi import FastAPI
from schemas.tache import Tache

app=FastAPI(title="API de gestion des taches")

@app.get("/taches/", summary="Recuperer toutes les taches", description="toutes les taches de la BDD se retrouvent dans un JSON", response_description="Liste de toutes les taches en format JSON")
def tache_racine():
    return{"message":"Fonctions qui va recuperer toutes les tâches"}

@app.get("/taches/{tache_id}")
def getTache(tache_id : int):
    return {"message": f"recuperation des infos de la tache {tache_id}"}

@app.post("/taches/")
def createTache(t : Tache):
    return {"message": "Tache reçue", "tache": t}

@app.put("/taches/{tache_id}")
def updateTache(tache_id : int, t:Tache):
      return{"message": f"Modification de la tache {tache_id}", "nouvelleValeur":t}

@app.delete("/taches/{tache_id}")
def deleteTache(tache_id : int):
      return{"message": f"Suppression de la tache {tache_id}"}