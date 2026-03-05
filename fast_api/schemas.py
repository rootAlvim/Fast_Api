from pydantic import BaseModel, EmailStr

class Message(BaseModel):
    message: str

class UserPublic(BaseModel):
    nome_de_usuario: str 
    email: EmailStr
    id: int
    
class Userschema(UserPublic):
    senha: str

class UserDB(Userschema):
    id: int
