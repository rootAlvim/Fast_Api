from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fast_api.schemas import Message
from http import HTTPStatus
app = FastAPI()

@app.get('/',status_code=HTTPStatus.OK,response_model=Message)
def read_root():
    return {'message': 'ola mundo'}

@app.get('/home',response_class=HTMLResponse)
def read_home():
    return '''
    <html>
<body>
<h1>Hello World</h1>
</body>
</html>

'''