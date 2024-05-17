print("Welcome to the world of Python !")
print("Now we are going to create new files")

files=int(input("Enter the number of files to be created:"))

for i in range(files):

    # print(f"{i+1}.txt")
    with open(f"{i+1}.txt","w") as f:
        print("The files is creating!")
    # try:
    #     with open("main.txt") as f:
    #         f.read()
    # except FileNotFoundError:
        # with open("main.txt","w") as f:
        #     f.write("good morning")       

        