from fastapi import FastAPI,Depends,HTTPException
from schemas.tacheCreation import TacheCreation
from sqlalchemy.orm import Session
from crud.database import SessionLocal
import db.tache

def get_db():
     db=SessionLocal()
     try:
          yield db
     finally:
          db.close()
 
app=FastAPI(title="API de gestion des taches")

@app.get("/taches/", 
         summary="Recuperer toutes les taches", 
         description="toutes les taches de la BDD se retrouvent dans un JSON", 
         response_description="Liste de toutes les taches en format JSON")
def getAllTache(session:Session=Depends(get_db)):
    try:
        db_tache=db.tache.getTaches(session)
    except Exception:
        raise HTTPException(status_code=500, detail="Erreur interne")
    return db_tache
@app.get("/taches/{tache_id}")
def getTache(tache_id : int, session:Session=Depends(get_db)):
    try:
        db_tache=db.tache.getTache(tache_id,session)
    except Exception:
        raise HTTPException(status_code=500, detail="Erreur interne")
    if not db_tache:
        raise HTTPException(status_code=404, detail="Tâche non trouvée")
    return db_tache

@app.post("/taches/")
def createTache(t : TacheCreation, session:Session=Depends(get_db)):
 try:
    db_tache=db.tache.createTache(t, session)
    return db_tache
 except Exception:
     raise HTTPException(status_code=500, detail="Erreur interne")
 return db_tache
     

@app.put("/taches/{tache_id}")
def updateTache(tache_id : int, t:TacheCreation, session:Session=Depends(get_db)):
      try:
          db_tache=db.tache.updateTache(tache_id,t,session)
      except Exception:
          raise HTTPException(status_code=500, detail="Erreur interne")
      if not db_tache:
          raise HTTPException(status_code=404, detail="Tâche non trouvée")
      return db_tache

@app.delete("/taches/{tache_id}")
def deleteTache(tache_id : int, session : Session = Depends(get_db)):
    try:
        deleted = db.tache.deleteTache(tache_id, db)
    except Exception:
        raise HTTPException(status_code=500, detail="Erreur interne")
    if not deleted:
        raise HTTPException(status_code=404, detail="Tâche non trouvée")
    return {"message": "La tache a été supprimée avec succès", "id": tache_id}