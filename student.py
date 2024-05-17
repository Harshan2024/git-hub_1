class Student:
    def __init__ (self,name,roll_no,age,gpa):
        self.name=name
        self.roll_no=roll_no
        self.age=age
        self.gpa=gpa

    def ishonour(self):
        if self.gpa>"9":
            print( self.name,"is honour student")
        else:
            print(self.name,"is not a honour student")  
        
                  
s1=Student("Harshan","13","17","8.7")
s2=Student("Mahesh","24","18","9.1")
s2.ishonour()
print(s1.gpa)  
print(s2.name)
     
    
       