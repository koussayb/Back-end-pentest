from unicodedata import name
from sqlalchemy.orm import Session
import app.models as models, app.schemas as schemas

def get_by_id(db: Session, id: int):
    return db.query(models.Connectors).filter(models.Connectors.id == id).first()

def get_all(db: Session):
    Connectorss = db.query(models.Connectors).all()    
    return Connectorss    


def delete(db: Session, id: int):
    Connectors =db.query(models.Connectors).filter(models.Connectors.id == id).first()
    db.delete(Connectors)
    db.commit()

def create(db: Session, Connectors:schemas.Connectors):
    Connectors = models.Connectors(date =Connectors.date,status=Connectors.status,name =Connectors.name)
    db.add(Connectors)
    db.commit()
    



