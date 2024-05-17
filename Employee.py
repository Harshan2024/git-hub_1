class Employee:
    def __init__(self,empname,id_no,salary,experience,dob):
       self.empname=empname
       self.id_no=id_no
       self.salary=salary
       self.experience=experience
       self.dob=dob

    def bonous(self):
        self.salary*=(10/100)
        print("The bonous of",self.empname,"is",self.salary)

    def increament(self):
        self.salary*=(10/100)
        print("The increament of the",self.empname,"is",self.salary)

    def Experience_bonous(self):
        if self.experience>=5:
           self.salary*=(20/100)
           print("The experience bonous of the",self.empname,"is",self.salary)
        else:
            print(self.empname,"has no experience bonous")   
num=int(input("Enter the number:"))
Emp1=Employee("Harshan","001",10000,8,"05/01/2007")
Emp2=Employee("Pooja","002",3000,4,"01/03/2006")           
Emp1.bonous()
Emp1.increament()
Emp1.Experience_bonous()    
Emp2.bonous()
Emp2.increament()
Emp2.Experience_bonous()    

