print("Now we are going to identify the numbers")
try:
    num=input("Enter the number:")
    num=int(num)
except ValueError:
    num=float(num)
if num<0:
    print("The number is below 0")    
    
elif num<=100:
    print("The number is between 0 to 100")
elif num<=1000:
    print("The number is between 101 to 1000")
elif num<=2000:
    print("The number is between 1001 to 2000")    
else:
    print("Invalid")                

