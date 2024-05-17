# print("Welcome to the world of the Python!")
# print("Now we are going to  do list")
# num_1=[0,1,1,1,1,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
# print("The List  with duplicate elements\n",num_1)
# # num_2=[0,1,2,3,4,5,6,7,8,9]
# table=[]   
# for i in num_1:
#     # c=num_1.count(i)
#     # for j in range(c-1):
#     #  num_1.remove(i)
#     if i not in table:
#         table.append(i)
    
    
# print("The list without dupilicate elements\n",table)
# import json

# print("Now we are going to handle python with list")
# list_1=json.loads(input("Enter the list with many elements:"))
# list_2=[]
# list_2.append(list_1)
# print(list_2)
# print(type(list_2))


# test="['test','test23']"
# new=list(test)
# print(new)

num=int(input("No of elements in list :"))
num_1=[]
for i in range(num):
    tmp_list=[int(input("Enter first number: ")),int(input("Enter second number: ")),int(input("Enter third number: "))]
    num_1.append(tmp_list)
print(num_1)
index=1
c=int(input("Enter the index number you want to remove:"))
num_1.remove(num_1[c-1])
print(num_1)
d=int(input("Enter the index number you want to delete in all list:"))
num_1[d-1].remove(num_1[d-1][d-1])
print(num_1)