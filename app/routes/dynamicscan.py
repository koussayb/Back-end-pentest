from fastapi import Depends,APIRouter,Request
from sqlalchemy.orm import Session
import app.crud.dynamicscan as dynamicscan, app.schemas as schemas ,app.tokens as tokens
from app.database import  SessionLocal

router = APIRouter(tags=['dynamicscans'])

db = Session()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()

@router.get("/dynamicscans")
def read_users( request : Request ,db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        dynamicscans = dynamicscan.get_all(db)
        return {"status" : 200 , "data" : dynamicscans }
    else:
        return{"status" : 403 , "message" :  "token expired."}
    



@router.post("/dynamicscans")
async def create_user(dynamic :schemas.Dynamicscan,request : Request , db: Session = Depends(get_db)):
    
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        dynamicscan.create(db,dynamic)
        return   {"status" : 200 , "message": "dynamicscan created."}
    else:
        return{"status" : 403,"message" :"token expired"}
    
    


@router.delete("/dynamicscans")
def delete_user(id :int ,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        dynamicscan.delete(db=db, id=id)
        return {"status" :  200 , "message" : "dynamicscan deleted"}
    else:
        return{"status" : 401 ,"message":"token expired"}
    



