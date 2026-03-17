from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator, field_validator
from typing import List, Dict, Optional, Annotated

class Student(BaseModel):

    name : str
    email : EmailStr
    age : int
    standard : int
    failed : bool
    certificates : List[str]
    tutor_list : Dict[str, str]
    contact_details : Dict[str, str]


    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domain = ['gmail.com', 'hotmail.com', 'outlook.com' ]
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domain:
            raise ValueError('Not a valid Domain')
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    @field_validator('age', mode = 'after') # this mode = after make sure that this age value is entering into the function after type conversion
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        raise ValueError("Age must be between 0 and 100")
    
    @model_validator(mode = 'after')
    def validate_extra_tutor(self):
        if self.failed and 'extra_tutor' not in self.tutor_list:
            raise ValueError('Student must have an extra tutor')
        return self

    
def updated_student_data(student : Student):
    print(student.name)
    print(student.age)
    print(student.certificates)
    print(student.failed)
    print('Updated')

student_info = {'name' : 'Shankar', 'email':'abc@gmail.com', 'age' : '21', 'standard' : '12', 'failed' : False, 'certificates' : ['DL', 'ML', 'RL'], 'tutor_list' : {'Normal_tutor' : 'Sravan'}, 'contact_details': { 'phone_number' : '9876543210'}}
student1 = Student(**student_info)
updated_student_data(student1)

print(student1)
