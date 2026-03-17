from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Student(BaseModel):

    name:Annotated[str, Field(max_length = 50, title="Name of the student", description = "Give the name of the student")]
    email : EmailStr
    linkedin_url : AnyUrl
    age : int = Field(gt=10, lt=100)
    standard : Annotated[float, Field(gt = 5, lt = 12)]
    failed : Annotated[bool, Field(default=None, description = "Did the student fail in any standard until now")]
    certificates : Annotated[Optional[list], Field(default = None, max_length = 10)]
    contact_details : Dict[str,str]

def updated_student_data(student:Student):
    print(student.name)
    print(student.age)
    print(student.certificates)
    print(student.failed)
    print('updated')

student_info = {'name' : 'Shankar', 'email': 'Shankar@gmail.com', 'linkedin_url': 'http://linkedin.com//shankarommi', 'age' : '21', 'standard' : '11', 'contact_details' : {'phone' : '9876543210' }}

    
student1 = Student(**student_info)
updated_student_data(student1)
print(student1)