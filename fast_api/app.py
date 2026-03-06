from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse 
from fast_api.schemas import Message , Userschema , UserPublic , UserDB , UserList
from http import HTTPStatus 
app = FastAPI()

database = []
'''
@app.get('/',status_code=HTTPStatus.OK,response_model=Message)
def read_root():
    return {'message': 'ola mundo'}

@app.get('/home',response_class=HTMLResponse)
def read_home():
    return 
    <html>
<body>
<h1>Hello World</h1>
</body>
</html>

'''

@app.post('/usuario',status_code=201,response_model=UserPublic) #Create
def criar_usuario(usuario: Userschema):
    usuario_id = UserDB(
        nome_de_usuario = usuario.nome_de_usuario,
        email = usuario.email,
        senha = usuario.senha,
        id = len(database)+1
    )
    database.append(usuario_id)
    return usuario_id

@app.get('/users', response_model=UserList) #Read
def read_users():
    return {'users': database}



@app.put('/users/{user_id}', status_code=200,response_model=UserPublic) #Update
def update_user(user_id: int , user:Userschema):
    usuario_id = UserDB(
        nome_de_usuario = user.nome_de_usuario,
        email = user.email,
        senha = user.senha,
        id = user_id
    )
    if user_id > len(database) or user_id < 1 :
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail = "Usuario não encontrado"
        )
    database[user_id - 1] = usuario_id
    return usuario_id

@app.delete('/users/{user_id}', status_code=200,response_model=UserPublic) #Delete
#response_model=UserPublic
def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1 :
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail = "Usuario não encontrado"
        )
    return database.pop(user_id - 1)
    
