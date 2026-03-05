from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fast_api.schemas import Message , Userschema , UserPublic , UserDB
from http import HTTPStatus
app = FastAPI()

database = []

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


@app.post('/usuario',status_code=201,response_model=UserPublic)
def criar_usuario(usuario: Userschema):
    usuario_id = UserDB(
        nome_de_usuario = usuario.nome_de_usuario,
        email = usuario.email,
        senha = usuario.senha,
        id = len(database)+1
    )
    database.append(usuario_id)
    return usuario_id
