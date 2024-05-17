from read import*
from tabulate import tabulate

def create_student_record():
    data=read_json()
    s_no=len(data["students"])+1
    Name=input("Enter your name:")
    Addres=input("Enter your addres:")
    Course=input("Enter your course name:")
    Course_duration=input("Enter the duration of the course:")
    temp_dict={
        "s_no":s_no,
        "name":Name,
        "address":Addres,
        "course":Course,
        "duration":Course_duration
    }
    data["students"].append(temp_dict)
    print("The student record is created succesfully!")
    write_json(data)
    
def view_record():
    data=read_json()
    table=[]
    row=["sno","name","address","course","duration"]
    for i in data["students"]:
        row_2=[i["s_no"],i["name"],i["address"],i["course"],i["duration"]]
        table.append(row_2)
    print(tabulate(table,headers=row,tablefmt="grid"))
    print("The student record is viewed succesfully!")

def update_record():
    data=read_json()
    view_record()
    print("The data is now going to be updated")
    update=input("Enter the key to be updated [name,address,course,duration]:")
    var=int(input("Enter the s.no of the student:"))
    if update=="name":
        new_name=input("Enter the new name:")
        data["students"][var-1]["name"]=new_name   
        print("The name is updated succesfully!")

    elif update=="address":
        print("The address is being updated") 
        new_address=input("Enter the new address:")
        data["students"][var-1]["address"]=new_address
        print("The address is updated succesfully!")

    elif update=="course":
        print("The course is being updated")
        new_course=input("Enter the new course:")
        data["students"][var-1]["course"]=new_course
        print("The course is updated  succesfully!")
        
    elif update=="duration":
        print("The duration is being updated")   
        new_duration=input("Enter the new course_duration:")
        data["students"][var-1]["duration"]=new_duration
        print("The duration is updated succesfully!")
    write_json(data)     

def delete_record():
    view_record()
    data=read_json()
    print("Deleting the student record on the basis of the s.no")
    delete=int(input("Enter the s.no of the student:"))
    s_no=1
    for i in data["students"]:
        if i["s_no"]==delete:
            data["students"].remove(i)
    for i in data["students"]:
        i["s_no"]=s_no
        s_no+=1
    print(data) 
    print("The delete record is takes place succesfully")          
    write_json(data)        
