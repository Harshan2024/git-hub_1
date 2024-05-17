# print("hello world")
# print("my name is harshan")
# print("I am 17 years old")
# print("I am living in thoothukudi")
# print("my hobby is searching new items")
# print("_________")
# print("/        /")
# print("/        /")
# print("/        /")
# #print("/        /")
# print("/________/")

# days={
# "Mon":"Monday",
# "Tue":"Tuesday",
# "wed":"Wednesday",
# "Thur":"Thursday",
# "Fri":"Friday",
# "Sat":"Saturday",
# "Sun":"Sundaday",
# }
# print(days["Sun"])
# print(days.get("Mon"))
# print(days.get("JAN"))
# print(days)
# print(days.get("Jan","Not a valid key"))
# print(days.keys())
# print(days.values())
# print(days.items())

# a=1
# while a<=11:
#     print(a)
#     a+=1
    
#     if a==10:
#         print(a)
    
# print("the loop is done ")


# variable=10
# while variable>=1:
#     print(variable)
#     variable-=1
# print("the loop is done ")


# variable=1
# while variable<=5:
#     if variable==3:
#         print("loop takes third time")
#     else:
#         print("Harshan")
#     variable+=1



print("The game begains")
print("it move forward, but won't backwards")
variable=1
while variable<=3:
    # print(variable)
    word=input("Enter the number:")
    if word=="pawns": 
       print("You won")
    #    exit()
       break
    else:
        print("wrong ans")   
    variable+=1
if variable==4:

   print("You lose")