import json

def read_json():
    with open("student.json") as f:
        data=json.load(f)
    return data  

def write_json(data):
    with open("student.json","w") as f:
        json.dump(data,f,indent=3)
   

 
        
