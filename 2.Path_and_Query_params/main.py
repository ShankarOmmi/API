from fastapi import FastAPI, Request, Path, HTTPException, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import json
import uvicorn




app = FastAPI()

def load_data():
    with open('students.json', 'r') as f:
        data = json.load(f)
        return data
    
@app.get('/')
def hello():
    return {'message': "Welcome"}

templates = Jinja2Templates(directory = 'Templates')


#HTML endpoint

@app.get("/about", response_class = HTMLResponse)
async def about(request:Request):
    context = {"request": request, "name": "User"}
    return templates.TemplateResponse("index.html", context)

#View all data

@app.get('/view')
def view():
    return load_data()
""" Return all the data"""


#Path parameter example
""" here the patient_id is the dynamic URL input """
@app.get('/students/{student_id}')
def view_student(student_id:str=Path(...,description='ID of the student in the DB', examples = 'S001')):
    data = load_data()

    if student_id in data:
        return data[student_id]
    raise HTTPException(status_code = 404, detail = "Student not found")


#query parameter example

@app.get('/sort')
def sort_students(
    sort_by:str=Query(..., description ="sort on the basis of age, marks, grade "),
    sort_order:str = Query('asc', description='Sort in asc or dsc order')
    ):

    valid_fields =['age', 'marks_obtained', 'grade']
    if sort_by not in valid_fields :
        raise HTTPException(status_code = 400, detail =f'Invalid field, select from {valid_fields}')
    if sort_order not in ['asc','desc']:
        raise HTTPException(status_code = 400, detail = f'Invalid sort order select between asc or desc')

    data = load_data()

    order = True if sort_order=='desc' else False

    sorted_data = sorted(data.values(), key = lambda x:x.get(sort_by,0), reverse=order)
    return sorted_data

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host = "127.0.0.1",
        port = 8000,
        reload = True
    )
    
    


