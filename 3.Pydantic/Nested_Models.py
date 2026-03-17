from pydantic import BaseModel

class Address(BaseModel):

    city : str
    state : str
    pin : str

class Student(BaseModel):

    name : str
    standard : str
    age : int
    address : Address

address_dict = { 'city' : 'Tanuku', 'state' : 'AP', 'pin' : '534211'}

address1 = Address(**address_dict)

student_dict = {'name' : 'Shankar', 'standard' : '12', 'age' : 21, 'address' : address1}

student1 = Student(**student_dict)

temp = student1.model_dump()

print(type(temp))
print(temp)