from fastapi import Depends,APIRouter,Request
from sqlalchemy.orm import Session
import app.crud.connector as connector, app.schemas as schemas ,app.tokens as tokens
from app.database import  SessionLocal

router = APIRouter(tags=['connectors'])

db = Session()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()

@router.get("/connectors")
def read_users( request : Request ,db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        connectors = connector.get_all(db)
        return {"status" : 200 , "data" : connectors }
    else:
        return{"status" : 403 , "message" :  "token expired."}
    



@router.post("/connectors")
async def create_user(conn :schemas.Connectors,request : Request , db: Session = Depends(get_db)):
    
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        connector.create(db,conn)
        return   {"status" : 200 , "message": "connector created."}
    else:
        return{"status" : 403,"message" :"token expired"}
    
    


@router.delete("/connectors")
def delete_user(id :int ,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        connector.delete(db=db, id=id)
        return {"status" :  200 , "message" : "connector deleted"}
    else:
        return{"status" : 401 ,"message":"token expired"}
    



