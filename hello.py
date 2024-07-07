# l1= ["Harry","Soham","Sachin","Rahul","sachi ma'am"]
# # for i in range (len(l1)):
# #     if str(l1[i][0])=="S":
# #         print(f"Good morning {l1[i]}")

# for i in l1:
#     if i.startswith("S"):
#         print(f"Hello {i}")

# i=1
# m= int(input("enter a number: "))
# while i<11:
#     print(f"{m}X{i}={m*i}")
#     i+=1

# a= int(input("enter a prime number: "))
# prime= True
# for i in range (2,a):
#     if (a%i==0):
#         prime= False
#         break
# if(prime):
#     print("it is a prime number")
# else:
#     print("it is not a prime number")

# inp= int(input("Enter a number: "))
# i=0
# while (i<inp):
#     print(str(i)," " ,end='')
#     i+=1

# #factorial question
# inp= int(input("Enter a number: "))
# fact=1
# for i in range(inp,0,-1):
#     fact*=i
# print(f"factoraial of  {inp} is: {fact}")

from wsgiref.simple_server import software_version


n= 4
# for i in range (n):
#     print("*"*(i+1))

# for i in range (0,n):
#     for j in range (0,n):
#         if (j<=i):
#             print("*",end="") 
#     print("\n")


# for i in range (4):
#     print(" " *  (n-i-1),end="")
#     print("*" *  (2*i+1),end="")
#     print(" " *  (n-i-1),)

# n= 4
# for i in range (0,n):
#     for j in range (0,n):
#         if (i==0 or j==0 or i==n-1 or j==n-1):
#             print("*",end='')
#         else:
#             print(" ",end='')
#     print("\n")

# def percentage1(marks):
#     p= sum(marks)/4
#     return p
# marks1= [86,89,99,80]
# marks2= [76,86,59,80]
# percentage= percentage1(marks1)
# print(percentage)  

# def greet(name):
#     print("Good day,"+ name)
# greet("basu")  

# def fn(num):
#     fact=1
#     for i in range (1,num+1):
#         fact*=i   
#     return fact
# print(fn(0))

# def fn(n):
#     if n==1 or n==0:
#         return 1
#     return n*fn(n-1)
# i= int(input("enter number: "))
# print(fn(i))

# def fn(a,b,c):
#     if (a>b and a>c):
#         return a
#     elif (b>a and b>c):
#         return b
#     else:
#         return c
    

# a=5
# b=4  # f"{fn(a,b,c)} is greater"
# c=8
# print(fn(a,b,c))

# def fn(cel):
#     far= (9/5*cel)+32 
#     return far
# cel= 0
# print(fn(cel))

# def fn(n):
#     if (n==1):
#         return 1
#     return n+fn(n-1)

# a= int(input("enter n: "))
# print(fn(a))

# n= 3
# for i in range(n):
#     print("*"*(n-i))

# def fn(string,word):
#     nstr= string.replace(word,"Nesar")
#     return nstr.strip()
# str= "   I am basu kallapur from bmsce   "
# print(str)
# print(fn(str,"basu"))

# # snake,water and gun game
# import random
# def fn(user,comp):
#     if (user==comp):
#         return None
#     elif user=="s":
#         if comp=="w":
#             return True
#         elif comp=="g":
#             return False
#     elif user=="w":
#         if comp=="s":
#             return True
#         elif comp=="g":
#             return False
#     elif user=="g":
#         if comp=="s":
#             return True
#         if comp=="w":
#             return False

# print("Snake, Water and Gun game")
# print("Computer's turn Snake(s), Water(w) and Gun(g): ")
# randnum= random.randint(1,3)
# if (randnum==1):
#     comp="s"
# elif (randnum==2):
#     comp="w"
# elif (randnum==3):
#     comp="g"

# you= input("User's turn snake(s), water(w) or Gun(g): ")
# print(f"computer choice is: {comp}")
# print(f"user's choice is: {you}")

# a= fn(you,comp)
# if a==None:
#     print("it's a tie")
# elif a:
#     print("you win")
# else:
#     print("you loose")

# # file I/O
# writing file
# f= open("this.txt")
# data= f.read()
# print(data)
# f.close()

# # reading file
# f= open("newFile.txt",'r')
# line= f.readline()
# while(line!=""):
#     print(line)
#     line=f.readline()
# f.close()

# # appending
# string= "\n This is the new appended line."
# f= open("newFile.txt","a")
# appendd= f.write(string)
# appendd= f.write(string)
# f.close()

# # with statement , it is used to do the the same work without close
# with open("newFile.txt") as f:
#     print(f.read())

# # practice set question
# with open("file.txt",'r') as f:
#     lines= f.read()
#     if ("twinkle" in lines):
#         print("it's present")
#     else:
#         print("not there")

# f= open("file.txt",'r')
# lines= f.read()
# if ("basu" in lines):
#     print("its there")
# else:
#     print("not there")

# import random
# def game():
#     print("welcome to the game")
#     score= random.randint(1,100)
#     #fetch highscore
#     print(f"your score is: {score}")
#     with open("highScore.txt",'r') as f:
#         highscore= f.read()
#         if(highscore!=""):
#             highscore= int(highscore)
#         else:
#             highscore=0
#     if(score>highscore):
#         with open("highScore.txt",'w') as f:
#             f.write(str(score))
#     return score
# game()

# # tables genearator
# def tableGenearator(n):
#     table= ""
#     for i in range(1,11):
#         table+= f"{n}X{i}={n*i} \n"
#     with open(f"tables/table{n}.txt","w") as f:
#         f.write(table)

# for i in range(25):
#     tableGenearator(i)

# word= "donkey"
# with open("file.txt","r") as f:
#     content= f.read()
# newContent= content.replace(word,"basu")
# with open("file.txt","w") as f :
#     f.write(newContent)

# words= ["donkey", "ganda", "gandu", "kachda"]
# with open("file.txt","r") as f:
#     content= f.read()
# for word in words:
#     content= content.replace(word,"#"*len(word))
# with open("file.txt","w") as f :
#     f.write(content)

# with open("log.txt",'r') as f:
#     content= f.read()
# if ("python" in content):
#     print("python is present")
# else:
#     print("it is not present")

# with open("log.txt","r") as f:
#     line= f.readlines()
# lineno=1
# for lines in line:
#     if("python" in lines):
#         print(f"yes, python is present {lineno}")
#         break
#     lineno+=1
# else: 
#     print("python is not present")

# with open("file.txt","r") as f1:
#     content= f1.read()
# with open("newfile.txt","w") as f2:
#     f2.write(content)

# with open("file.txt","r") as f1:
#     content1= f1.read()
# with open("newfile.txt","r") as f2:
#     content2= f2.read()
# if(content1==content2):
#     print("both are same")
# else:
#     print("they aren't same ")

# with open("file.txt","r") as f1:
#     content1= f1.read()
# content2= content1.replace(content1,"")
# with open("newfile.txt","w") as f2:
#     f2.write(content2)



# # OOPS
# class students:
#     college= "bmsce"
#     year= 1
#     def information (self):
#         print(f"I am {self.name}, college name is {self.college} and studing in {self.year}st year")

#     # dunder method, which is automatically called
#     def __init__(self,name,college,year):
#         self.name= name
#         self.college= college
#         self.year= year
#         print("printed using dunder method")
#     @staticmethod
#     def greet ():
#         print(f"good morning")
# basu= students("basuck","bmsce",1)
# print(basu.name,basu.college,basu.year)


# class programmer:
#     company= "Microsoft"
#     def __init__(self,name,salary,pin):
#         self.name= name
#         self.salary= salary
#         self.pin= pin

# b= programmer("Basu kallapur",150000,560019)
# print(b.name,b.salary,b.pin) 
# m= programmer("mahaan",150000,560019)
# print(m.name,m.salary,m.pin) 
# c= programmer("chidvan",150000,560019)
# print(c.name,c.salary,c.pin) 

# class calculator():
#     def __init__(self,n):
#         self.n= n
#     @staticmethod
#     def greet():
#         print("Good Morining!!")
#     def square(self):
#         print(f"square of this number is: {self.n*self.n}")
#     def cube(self):
#         print(f"cube of this number is: {self.n*self.n*self.n}")
#     def squareroot(self):
#         print(f"squareroot of this number is: {self.n**0.5}")

# a= calculator(4)
# a.greet()
# a.square()
# a.cube()
# a.squareroot()


# class p1:
#     name1= "basu"

# print(p1().name1)
# newName= p1()
# newName.name1= "mahan"
# print(newName.name1)   #class attribute doesn't change but new instance is created


# from random import randint  
# class train:
#     def __init__(self,trainNO):
#         self.trainNo= trainNO
#     def book(self,fro,to):
#         print(f"your train {self.trainNo} is booked from {fro} to {to}")
#     def getStatus(self,fro,to):
#         print(f"your train {self.trainNo} is running on time")
#     def getFare(self,fro,to):
#         print(f"your ticket fare for the train {self.trainNo} from {fro} to {to} is {randint(300,2000)}")

# t= train(14341)
# t.book("hubli","bengaluru")
# t.getStatus("hubli","bengaluru")
# t.getFare("hubli","bengaluru")



# # inheritance

# #1. multiple inheritance (parent1 and parent2 to child)
# class student:
#     college= "BMS College of Engineering"
#     def __init__(self,name,year):
#         self.name= name
#         self.year= year
#     def show(self):
#         print(f"The name of the student is {self.name} and studying in {self.year} year")
# class student1:
#     language= "kannada"
#     def __init__(self,name,year):
#         self.name= name
#         self.year= year
#     def show(self):
#         print(f"and also {self.name} has completed his his MBA from IIM and his in {self.year} yeara and bdday is on {self.bdday}")
# class child(student,student1):
#     def show(self):
#         print(f"I am {self.name} studying in {self.college} and I love {self.language} language")
# c= child("Krishna","1st")
# c.show()


# # #2. Multilevel inheritance
# class employe1:
#     company= "Microsoft"
#     def __init__(self):
#         print("constructor of employee1")
        
# class employe2(employe1):
#     post= "manager"
#     def __init__(self):
#         # super().__init__() 
#         print("constructor of employee2")

# class child(employe2):
#     salary= 120000
#     def __init__(self):
#         super().__init__()   #used to make to run constructor of this previous parent also , which is employee2 or super() method is used to access the methods of a super class in the derived class. 
#         print("constructor of child")

# a= child()
# print(a.company,a.post,a.salary)

# # #class methods
# class student:
#     college= "BMS College of Engineering"
#     @classmethod  # with this output will be "my name is basu kallapur studying in BMS College of Engineering." and without this the college name will be change do RVCE Bengaluru
#     def show(cls):
#         print(f"my name is basu kallapur studying in {cls.college}.")

# a= student()
# a.college= "RVCE Bengaluru"
# a.show()


# #Property decorators



# #operator overloading
class Number:
    def __init__(self,n):
        self.n= n
    def __add__(self,num):
        return self.n + num.n
n= Number(1)
m= Number(2)
print(n+m)

