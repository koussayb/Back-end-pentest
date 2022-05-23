from fastapi import Depends,APIRouter,Request
from sqlalchemy.orm import Session
import app.crud.infrastructure as infrastructure, app.schemas as schemas ,app.tokens as tokens
from app.database import  SessionLocal

router = APIRouter(tags=['infrastructures'])

db = Session()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()

@router.get("/infrastructures")
def read_users( request : Request ,db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        infrastructures = infrastructure.get_all(db)
        return {"status" : 200 , "data" : infrastructures }
    else:
        return{"status" : 403 , "message" :  "token expired."}
    



@router.post("/infrastructures")
async def create_user(infra :schemas.Infrastructure,request : Request , db: Session = Depends(get_db)):
    
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        infrastructure.create(db,infra)
        return   {"status" : 200 , "message": "infrastructure created."}
    else:
        return{"status" : 403,"message" :"token expired"}
    
    


@router.delete("/infrastructures")
def delete_user(id :int ,request : Request , db: Session = Depends(get_db)):
    token = request.headers.get('Authorization')
    if (tokens.verify_token(token)):
        infrastructure.delete(db=db, id=id)
        return {"status" :  200 , "message" : "infrastructure deleted"}
    else:
        return{"status" : 401 ,"message":"token expired"}
    



