from fastapi import FastAPI
#from fastapi.responses import HTMLResponse
from fast_api.schemas import Message
from http import HTTPStatus
app = FastAPI()

@app.get('/',status_code=HTTPStatus.OK,response_model=Message)
def read_root():
    return {'message': 'ola mundo'}