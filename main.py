
# import si_Calc as s
# from si_Calc import area_of_the_rectangle,perimeter_of_the_rectangle
# ln=int(input("Enter the value of length:"))
# bd=int(input("Enter the value of breadth:"))
# print("the product of the area and perimeter of the rectangle:",area_of_the_rectangle(ln,bd)*perimeter_of_the_rectangle(ln,bd))


from si_Calc import *
print("welcome to the calculation part")
while True:
        print("The following calculation parts are\n1.addition\n2.subtraction\n3.multiplication\n4.division\n5.simple intreast\n6.amount")
        option=input("Enter your choice[1,2,3,4,5,6]:")
        if option in["1","2","3","4"]:
                    num_1=int(input("Enter the first number:"))
                    num_2=int(input("Enter the second number:"))   
                    if option=="1":
                        print("The addition of ",num_1,"and", num_2,"is",add(num_1,num_2))
                    elif option=="2":
                        print(f"The subtraction of {num_1}and{num_2}is:{sub(num_1,num_2)}")
                    elif option=="3":
                        print(f"The multiplication of {num_1}and{num_2}is:{mul(num_1,num_2)}")
                    else:
                        print(f"The division of {num_1}and{num_2}is:{div(num_1,num_2)}")
        elif option=="5":
                    print("The simple intreast calutaion takes place")
                    p=int(input("Enter the principle amount:"))
                    n=float(input("Enter the years:"))
                    r=float(input("Enter the percentage of the intreast:"))
                    print(si(p,n,r))
        elif option=="6":
                    print("The amount to be calculated is:")
                    p=int(input("Enter the principle amount:"))
                    n=float(input("Enter the years:"))
                    r=float(input("Enter the percentage of the intreast:"))
                    sim=si(p,n,r)
                    amt=sim+p
                    print("The principle amount is:",p)
                    print("The simple intrest is:",sim)
                    print("The amount is:",amt)
        print("statements")
        variable=input("Do you want to continue the program(yes/no) ? : ")
        if variable=="yes":   
               continue             
        else:
          print("Thanks for using this application !")
        break        

        
        

    


