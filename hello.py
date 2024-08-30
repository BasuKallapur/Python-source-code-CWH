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

# from wsgiref.simple_server import software_version


# n= 4
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

# # mapping combined example
# hex_map = "0123456789ABCDEF"

# # Accessing an element using index
# remainder = 15
# hex_char = hex_map[remainder]
# print(f"Character at index {remainder} is {hex_char}")  # Output: 'F'

# # Finding the index of an element
# char = 'C'
# index = hex_map.index(char)
# print(f"Index of character '{char}' is {index}")  # Output: 12



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
#     @staticmethod   #Sometimes we need a function that does not use the self-parameter. We can define a static method like this:
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


# #2. Multilevel inheritance
# class employe1:
#     company= "Microsoft"
#     def __init__(self):
#         print("constructor of employee1")
# class employe2(employe1):
#     post= "manager"
#     salary= 120000
#     def __init__(self):
#         # super().__init__() 
#         print("constructor of employee2")
# class child(employe2):
    
#     def __init__(self):
#         # super().__init__()   #used to make to run constructor of this previous parent also , which is employee2 or super() method is used to access the methods of a super class in the derived class. 
#         print("constructor of child")
# a= child()
# print(a.company,a.post,a.salary)

# #class methods
# class student:
#     college= "BMS College of Engineering"
#     # @classmethod  # with this output will be "my name is basu kallapur studying in BMS College of Engineering." and without this the college name will be change do RVCE Bengaluru
#     def show(cls):
#         print(f"my name is basu kallapur studying in {cls.college}.")
# a= student()
# a.college= "RVCE Bengaluru"
# a.college= "RVCE dfs"
# a.show()


# #Property decorators  #abstraction and incapsulation
# class student:
#     college= "BMS College of Engineering"
#     @classmethod 
#     def show(cls):
#         print(f"my name is basu kallapur studying in {cls.college}.")
#     @property
#     def name(self):
#         return f"{self.fname} {self.lname}"
#     @name.setter
#     def name(self,value):
#         self.fname= value.split(" ")[0]
#         self.lname= value.split(" ")[1]

# a= student()
# a.college= "RVCE Bengaluru"
# a.name= "basu kallapur"  #after this we wan't our property to be set
# print(a.name)
# a.show()


# # #operator overloading
# class Number:
#     def __init__(self,n):
#         self.n= n
#     def __add__(self,num):
#         return self.n * num.n
# n= Number(2)
# m= Number(2)
# print(n+m)


# # ADVANCE PYTHON-1
# # walrus operator
# if (n := len([1, 2, 3, 4, 5])) > 3: 
#     print(f"List is too long ({n} elements, expected <= 3)") 
# # Output: List is too long (5 elements, expected <= 3) 

# # types defination
# # Variable type hint 
# age: int = 25 

# # Function type hints 
# def greeting(name: str) -> str: 
#     return f"Hello, {name}!" 
# # Usage 
# print(greeting("Alice"))  # Outpu t: Hello, Alice! 


# # Advanced type hints
# from typing import List,Tuple,Union,Dict
# student: Dict[str,int]= {"Basavaraj C Kallapur", 2}
# print(student)

# # Match case
# def http_status(status): 
#     match status: 
#         case 200: 
#             return "OK" 
#         case 404: 
#             return "Not Found" 
#         case 500:       
#             return "Internal Server Error" 
#         case _: 
#             return "Unknown status" 
# # Usage 
# print(http_status(200))  # Output: OK 
# print(http_status(404))  # Output: Not Found 
# print(http_status(500))  # Output: Internal Server Error 
# print(http_status(403))  # Output: Unknown status 

# Excepti0n handling
# try:
#     a= int(input("whats your age:"))
#     print(a)
# except Exception as e:
#     print(e)
# print("thank you.")

# # raise exception
# a= int(input("enter num1: "))
# b= int(input("enter num2: "))
# if(b==0):
#     raise ZeroDivisionError("You are not supposed devide any number by zero")
# else:
#     print(a/b)

# # Try with else clause
# try: 
#     a= int(input("enter num1: "))
# except Exception as e:
#     print(e)
# else: 
#     print("this is inside else")
# # This else is executed only if the try was successful 

# # Try with finally (usecase in function)
# def main():
#     try: 
#         a= int(input("enter num1: "))
#         return print(a)
#     except Exception as e:
#         print(e)
#         return print("exception block has run")
#     finally: 
#         print("this is inside finally")
# main()

# #GLOBAL KEYWORD
# #‘global’ keyword is used to modify the variable outside of the current scope.

# # enumerate function
# l= [1,2,3,4,5]
# # index= 0 #conventional method
# # for item in l:
# #     print(f"the numbers at index {index} of the list are {item}")    
# #     index+=1
# for index,item in enumerate (l):  #easy method
#     print(f"the numbers at index {index} of the list are {item}")    

# # list comprehensions
# myList= [1,2,3,4,5]
# # squaredList= [] #conventional method
# # for item in myList:
# #     squaredList.append(item**2)
# # print(squaredList)
# squaredList= [i**2 for i in myList] #easy method
# print(squaredList)

# # chapter 12 practice set
# # 1. 
# try:
#     with open("1.txt","r") as f:
#         print(f.read())
# except Exception as e:
#     print(e)
# try:
#     with open("2.txt","r") as f:
#         print(f.read())
# except Exception as e:
#     print(e)    
# try:
#     with open("3.txt","r") as f:
#         print(f.read())
# except Exception as e:
#     print(e)
# print("thank you.") #to show programme has not crashed

# # 2.
# l= [1,2,3,4,5,6,7,8,9]
# ind=0
# for ind,item in enumerate (l):
#     if ind== 2 or ind==4 or ind==6:
#         print(f"item at index {ind} of list is {item}")

# # 3.
# n= int(input("enter n: "))
# table= [n*i for i in range (1,11)]
# print(table)

# # 4.
# try:
#     a= int(input("enter a: "))
#     b= int(input("enter b: "))
#     print(a/b)
# except ZeroDivisionError as v:
#     print("infinite")

# # 5.
# n= int(input("enter n: "))
# table= [n*i for i in range (1,11)]
# with open("tabels.txt","a") as f:
#     f.write(f"the table of {n} is: {str(table)} \n")


# # ADVANCE PYTHON-2
# refer video and notes for venv related concepts

# #lambda
# square = lambda x:x*x 
# a= square(6)  # returns 36 
# print(a)
# sum = lambda a,b,c:a+b+c 
# b= sum(1,2,3)
# print(b)

# # join method
# a= ["basu","c","kallapur"]
# final= "_".join(a)
# print(final)

# # format (used in older version , now replaced by f string method)
# a="{} is a good {}".format("basu","boy")  #by default the indexing is 0 and 1
# print(a)
# a="{1} is a good {0}".format("basu","boy")
# print(a)

# # map, filter and reduce
# # 1. Map
# l= [1,2,3,4,5]
# square= lambda x: x*x
# sqlist= map(square,l)
# print(list(sqlist))

# # 2. Filter
# l= [0,1,2,3,4,5,6,7,8,9,10]
# def even(n):
#     if (n%2==0):
#         return True
#     else:
#         False
# onlyEven= filter(even,l)
# print(list(onlyEven))

# 3. Reduce
from functools import reduce
l= [1,2,3,4,5]
def sum(a,b):
    return a+b
print(reduce(sum,l))



