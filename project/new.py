from fun import*

print("Welcome to the student Application!")
while True:
    print("You can do\n1.Create a student record\n2.View a student record\n3.Update a student record")
    print("4.Delete a student record")
    choice=input("Enter your choice[1,2,3,4]:")
    if choice=="1":
        print("You have chosen create a student record")
        create_student_record()
    elif choice=="2":
        print("You have choosen view a student record")
        view_record()
    elif choice=="3":
        print("You have choosen update a student record")
        update_record()
    elif choice=="4":
        print("You have choosen delete a student record")
        delete_record()
    else:
        print("Invalid choice")    
    store=input("Do you want to continue the program (yes/no):")
    if store=="yes":
        pass
    else:
        print("Thanks for using our application\nVisit again")
        break

