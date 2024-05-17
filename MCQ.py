import json

with open("question.json","r") as f:
    data=json.load(f)
class Mcq:
    def __init__ (self,Question,choice,Answer):
        self.Question=Question
        self.choice=choice
        self.Answer=Answer
test=[]

for i in data["Questions"]:
    test.append(Mcq(i["Question"],i["choice"],i["Answer"]))
score=0
for j in test:

    print(j.Question)
    print(j.choice)
    ques=input("Enter your option[A,B,C,D]")
    if ques==j.Answer:
       score+=1
    else:
        score-=1
print("The score is",score)           



    

