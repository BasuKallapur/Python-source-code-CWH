# snake,water and gun game
import random
def fn(user,comp):
    if (user==comp):
        return None
    elif user=="s":
        if comp=="w":
            return True
        elif comp=="g":
            return False
    elif user=="w":
        if comp=="s":
            return True
        elif comp=="g":
            return False
    elif user=="g":
        if comp=="s":
            return True
        if comp=="w":
            return False

print("Snake, Water and Gun game")
print("Computer's turn Snake(s), Water(w) and Gun(g): ")
randnum= random.randint(1,3)
if (randnum==1):
    comp="s"
elif (randnum==2):
    comp="w"
elif (randnum==3):
    comp="g"

you= input("User's turn snake(s), water(w) or Gun(g): ")
print(f"computer choice is: {comp}")
print(f"user's choice is: {you}")

a= fn(you,comp)
if a==None:
    print("it's a tie")
elif a:
    print("you win")
else:
    print("you loose")