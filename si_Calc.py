#SI Calculator

#p,n,r --> principle, time in years,roi

#SI=p*n*r/100
# A= SI+p

#output
# Amound borrowed : 1000
# Total amount to tbe repaid : 1100
# Total Interest to be repaid : 100

# principle=int(input("Amount borrowed :"))
# time_in_years=int(input("Total duration of loan in years :"))
# rate_of_intrest=int(input("Enter your rate of intreast :"))
# si=principle*time_in_years*rate_of_intrest/100
# print(si)
# a=si+principle
# print(a)
# print("amount borrowed",principle)
# print("total amount to be repaid",a)
# print("total intreast to be repaid"+str(si))

#volume of sphere

# radius=int(input("the radius of sphere:"))
# volume=4/3*3.14*radius*radius*radius
# print(round(volume,2)) 

# list=[[1,2],[3,4],[2,3]]
# print(list[1])

# side=int(input("Enter the sides of the square:"))
# area_of_the_square=pow(side,2)
# print(area_of_the_square)
# perimeter_of_the_square=4*side
# print(perimeter_of_the_square)


# def area_of_the_rectangle(l,b):
#     return l*b
# def perimeter_of_the_rectangle(l,b):
#     return 2*(l+b)

# def area_of_the_circle(r):
#     return 3.14*pow(r,2)
# def area_of_the_sphere(r):
#     return 4/3*3.14*pow(r,3)
# radius=int(input("Enter the value of the radius:"))
# print("Area of the circle:",area_of_the_circle(radius))
# print("Area of the sphere :",area_of_the_sphere(round(radius,2)))

# num_1,num_2,num_3=0,0,-1
# if num_1>num_2 and num_1>num_3:
#     print(num_1,"is greater")
# elif num_1>num_2 or num_1>num_3:
#     print(num_1,"is greater")    
# elif num_2>num_1 and num_2>num_3:
#     print(num_2,"is greater")
# elif num_3>num_1 and num_3>num_2:
#     print(num_3,"is greater")
# elif num_1==num_3 or num_1==num_2: 
#     print(num_1,"is greater")     
# else:
#     print("All are equal")      

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def si(p,n,r):
    return p*n*r/100
def amount(p,si):
    return p+si

# name=input("enter the name:") 
# def vowel(a,e,i,o,u):
#  if name==vowel:
#    print(name)
#  else:
#    vowel="t"
#    print(vowel)  


name=input("Enter your name:")
output=" "
for i in name:
    if i in["a","e","i","o","u"]:
        output+="t"
    elif i in["A","E","I","O","U"]:
        output+="T"
    else:
        output+=i
print("The converted name:",output)                
