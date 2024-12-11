from pydantic import BaseModel, PositiveInt, ValidationError

class User(BaseModel):
    name:str
    age:PositiveInt

# Create a user with an invalid value for the age
# Catch and display the error
try:
    user = User(name="Jack Black", age=-1)

    print(user)
except ValidationError as ex:
    print(ex)

print("")

 # Create the user again but a valid value for the age
try:
    user = User(name="Jack Black", age=45)
    
    print(user)
except ValidationError as ex:
    print(ex)