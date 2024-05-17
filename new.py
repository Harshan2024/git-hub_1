# f=open("python.txt")
# print(f.read())
# f.close()


# with open("python.txt") as f:
#     print(f.read())


# f=open("python.txt","w")
# f.write("hello")
# f.close()

# with open("python.txt","a") as f:
#     f.write("\nGood Morning")


# with open("main.py") as f:
#     print(f.read())

# with open("main.txt","w") as f:
#     f.write("hello")   

# for line in ("python.txt"):
#     print(line)

# with open("python.txt") as f:
#     li=f.readlines()
#     li.sort()
#     for l in li:
#         print(l)

# with open("python.txt","a") as f:
#     f.write("")        

# import json
# with open("new.json") as f:
#     data=json.load(f)
# print(data)  

# data["emp_details"][2]["emp_name"]="finlay"
# print(data)
# with open("new.json","w") as f:
#      json.dump(data,f,indent=3)

# import json
# with open("new.json") as f:
#     data=json.load(f)

# city_list={"Kj":"Tuticorin",
#            "finlay":"Madurai",
#            "Harshan":"Chennai"}
# i=0
# for key,val in city_list.items():
#     for emp in data["emp_details"]:
#         if emp["emp_name"]==key:
#             emp["emp_add"]=val

#print(data)
# import json
# with open("new.json") as f:
#     data=json.load(f)
# data["emp_details"].remove["emp_add"]
# print(data)  
# data["emp_details"][1]["emp_age"]=18   
# print(data)  


# import json
# with open("new.json") as f:
#     data=json.load(f)
# #data.remove("emp_name")

# # data["emp_details"][0]["emp_name"]=""
# # print(data)
# # for key in data["emp_details"]:
# #     key["emp_name"]=""
# # print(data)    
# data["emp_details"][0]["emp_age"]="20"
# print(data)
# with open("new.json","w") as f:
#     json.dump(data,f,indent=3)

# import json
# with open("new.json") as f:
#     data=json.load(f)
# city_list=["Chennai","kochi","indore"]
# i=0
# for key in city_list:
#     for data in key:
#         for data in["emp_details"]:
#           print(data)
#     i+=1    

# import json
# with open("new.json") as f:
#      data=json.load(f)
# data["emp_details"][1]["emp_age"]="9"
# print(data)


# import json 
# with open("new.json","r") as f:
#     data=json.load(f)
# data["emp_details"][1]["emp_age"]="9" 
# print(data)
# with open("new.json","w") as f:
#     json.dump(data,f,indent=4)    

import json
with open("new.json") as f:
    data=json.load(f)
new_data={
          "emp_name":"jack",
          "emp_add":"Mumbai",
          "emp_age":"17,"
         }  

data["emp_details"][1]=new_data
with open("new.json","w") as f:
    json.dump(data,f,indent=4)
print(data)

    



