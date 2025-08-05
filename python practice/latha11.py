d={1:"Hai",2:"Hello",3:"Bai"}
d.keys()
print(d.keys())
print(d.values())






d={29:"Sreelatha",23:"Srimani",5:"Kishor"}
print(d)






d={
   29:['sreelatha','ramachandra'],
   23:['srimani','rangamma'],
   5:['kishor','rangamma']
  }
for i in d:
    print(d[i][0])







d={
   29:['sreelatha','ramachandra'],
   23:['srimani','rangamma'],
   5:['kishor','rangamma']
  }
for i in d:
    print(d[i][0])
    print(d[i][1])








d={
   29:['sreelatha','ramachandra'],
   23:['srimani','rangamma'],
   5:['kishor','rangamma']
  }
print(d.keys())
for i in d.keys():
    print(i,end=' ')
print()
print('=========')
for i in d.values():
    print(i)
print()
for i in d:
    print(i,'->',d[i])
print()
for i,j in d.items():
    print(i,'->',j)











d={
   295:['sree','9390434756','2005'],
   220:['sai','9881552358','2004']
  }
for i in d.keys():
    print(i,end=' ')
print()

for i in d.values():
    print(i)
for i in d:
    print(i,'->',d[i])








l=[2,3,2,1,4,4,1,3,2,1,]
d={}
for i in l:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
for i in d:    print(i,'->',d[i])
       














def name():
    print("My name is Sreelatha")
def rollno():
    print("My roll no is 224g1a0295")
def course():
    print("course       : B.Tech - EEE")
def validity():
    print("validity     :2022-2026")
def blood():
    print("blood group  :AB+")
def contact():
    print("contact      :9390434756")
def aadhar():
    print("aadhar      :333063622091")
name()
rollno()
course()
validity()
blood()
contact()
aadhar()






def name(NAME):
    print("My Name is",NAME)
def rollno(ROLLNO):
    print("My roll no is",ROLLNO)
NAME=input()
ROLLNO=input()
name(NAME)
rollno(ROLLNO)


    


def course(COURSE):
    print("course is",COURSE)
def validity(VALIDITY):
    print("validity is",VALIDITY)
def blood(BLOOD):
    print("Blood group is",BLOOD)
def contact(CONTACT):
    print("contact :",CONTACT)
def aadhar(AADHAR):
    print("aadhar  :",AADHAR)
COURSE=input()
VALIDITY=input()
BLOOD=input()
CONTACT=input()
AADHAR=input()
course(COURSE)
validity(VALIDITY)
blood(BLOOD)
contact(CONTACT)
aadhar(AADHAR)








def course(COURSE):
    print("course is",COURSE)
def validity(VALIDITY):
    print("validity is",VALIDITY)
def blood(BLOOD):
    print("Blood group is",BLOOD)
def contact(CONTACT):
    print("contact :",CONTACT)
def aadhar(AADHAR):
    print("aadhar  :",AADHAR)
COURSE=input("COURSE: ")
VALIDITY=input("VALIDITY: ")
BLOOD=input("BLOOD: ")
CONTACT=input("CONTACT: ")
AADHAR=input("AADHAR: ")
course(COURSE)
validity(VALIDITY)
blood(BLOOD)
contact(CONTACT)
aadhar(AADHAR)








