import json

from fastapi import FastAPI, Path, Query, HTTPException

app = FastAPI()

def loadData():
    with open('patients.json') as f:
        data = json.load(f)

    return data

@app.get('/')
def hello():
    return {"message" : "Hello world"}


@app.get('/about')
def about():
    return {"message" : "about"}

@app.get('/view')
def view():
    data = loadData()
    return {"response": data}

@app.get('/patient/{patient_id}')
def viewPatient(patient_id: str = Path(..., description = "This is the patient Id params")):
    data = loadData()
    print("patient_id", patient_id)
    if patient_id in data:
        return data[patient_id]

    raise HTTPException(status_code = 404, detail = "Patient not found")

@app.get('/sort')
def sortPatient(
    sort_by: str = Query(..., description = "Provide height, weight, bmi"),
    order: str = Query("asc", description='sort in asc or desc order')
    ):
    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field select from {valid_fields}')
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order select between asc and desc')
    
    data = loadData()

    sort_order = True if order=='desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data