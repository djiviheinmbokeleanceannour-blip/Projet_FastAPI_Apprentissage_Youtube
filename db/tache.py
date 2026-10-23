from schemas.tacheCreation import TacheCreation
from models.tache import Tache
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

def createTache(t: TacheCreation, session: Session):
    try:
        db_tache=Tache(
            titre=t.titre,
            description=t.description,
            etat=t.etat.value,
            dateEch=t.dateEch,
            dateCre=t.dateCre,
            dateMaj=t.dateMaj
        )
        session.add(db_tache)
        session.commit()
        session.refresh(db_tache)
        return db_tache
    except SQLAlchemyError as e:
        session.rollback()
        raise
def updateTache(db: Session):
    pass

def getTaches(db: Session):
    pass

def getTache(db: Session):
    pass

def deleteTache(db: Session):
    pass