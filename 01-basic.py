from pydantic import BaseModel, PositiveInt, ValidationError

class User(BaseModel):
    name:str
    age:PositiveInt

user = User(name="Jack Black", age=45)

print(user)