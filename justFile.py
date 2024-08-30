# # list comprehensions
# myList= [1,2,3,4,5]
# # squaredList= [] #conventional method
# # for item in myList:
# #     squaredList.append(item**2)
# # print(squaredList)
# squaredList= [i**2 for i in myList] #easy method
# print(squaredList)


# raise exception
a= int(input("enter num1: "))
b= int(input("enter num2: "))
if(b==0):
    raise ZeroDivisionError("You are not supposed devide any number by zero")
else:
    print(a/b)