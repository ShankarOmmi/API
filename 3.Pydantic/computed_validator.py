from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Student(BaseModel):

    name: str
    email: EmailStr
    age: int
    standard: int # class
    grade : str # A+, A, B, C, D
    failed: bool
    certificates : List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def fee(self) -> float:
        fee = 5000 + (self.standard * 500) + (2000 if self.failed else 0) - (len(self.certificates)*1000)
        return fee



def update_student_data(student: Student):

    print(student.name)
    print(student.age)
    print(student.certificates)
    print(student.failed)
    print('FEE', student.fee)
    print('updated')

student_info = {'name':'shankar', 'email':'abc@icici.com', 'age': '22', 'standard': 12, 'grade': 'A', 'failed': True, 'certificates': ['DL', 'RL'], 'contact_details':{'phone':'2353462', 'emergency':'235236'}}

student1 = Student(**student_info) 

update_student_data(student1)