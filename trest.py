# while True:
#     print("statements")
#     choice=input("do you want to continue(y/n) ? : ")
#     if choice=="y":
#         continue
#     else:
#         print("Thanks for using this application !")
#         break

# for i in range(2,10,2):
#     print("Harshan",end=" ")

# days={
#  "Mon":"Monday",
#  "Tue":"Tuesday",
#  "wed":"Wednesday",
#  "Thur":"Thursday",
#  "Fri":"Friday",
#  "Sat":"Saturday",
#  "Sun":"Sundaday",
# }
# for v in days.values():
#     # print(v)
#     if v=="Friday":
#         # print(v)
#         break 
#     print(v)
# print(len(days))
# for index in range(len(days)):
#      print(index)   
#      if index!=4:
#       print("The days withoud thur")
# print(index)      
# print(list(days.values())[index])     

# num=int(input("Enter the size:"))
# for i in range(num):
#     # print("*")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()    


#num=int(input("Enter the size of the pattern:"))
# for i in range(num,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print() nter the size:"))



# num=int(input("Enter the size:"))
# for i in range(num):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()   
# for l in range(num-1,0,-1):
#     for n in range(l):
#         print("*",end=" ")
#     print()    


# num=int(input("Enter the size of the pattern:"))
# for i in range(num):
#     for j in range(num-i-1):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print("*",end=" ") 
#     print()             


# num=int(input("Enter the size:"))
# for i in range(num):
#     for j in range(num-i-1):
#         print(" ",end=" ")
#     for k in range(j):
#         print("*",end=" ")
#     print()        


# num=int(input("Enter the size of the pattern:"))
# if num%2==0:
    
#     l=int(num/2)
#     s=2

# else:
#     l=(num//2)+1
#     s=1

# t=4

# for i in range(l):
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(s+t):
#         print("*",end=" ")
#     t-=2
#     print()   


print("Welcome to the try exception concept !")
try:
       num=int(input("Enter the first number:"))
       loan_period=float(input("Enter the duration of loan:"))
       print(num/loan_period)
except ValueError:
      print("Opps value error has been occured!")
      num=1
      loan_period=1.5
      print(num+loan_period)
except ZeroDivisionError:
        print("opps zero division error has been occured !")
        num=2
        loan_period=2.2
        print(num+loan_period)     
else:
       print("No exception has occured \nYou have done a great job!")      