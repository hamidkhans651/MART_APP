from fastapi import Depends,HTTPException, FastAPI
import uvicorn
from fastapi.security import HTTPBasic,HTTPBasicCredentials

app = FastAPI()

# basic = HTTPBasic()

# @app.get("/")
# def get_user(
#     creds: HTTPBasicCredentials = Depends(basic)):
#     return {"username":creds.username, "password":creds.password }



# authenticate with fake username and password

fake_user : str = "hamid"
fake_password: str = "hammi2293"

basic = HTTPException = HTTPBasic()

@app.get("/who")
def get_user(creds:HTTPBasicCredentials = Depends(basic)):
    if (creds.username == fake_user and creds.password == fake_password):
        return {"username":creds.username
                ,"password":creds.password
                }
    else:
        return {"error":"invalid username or password"}
    raise HTTPException(status_code=401,detail="hellow welcome to the todo app")
