import random
from re import S

from pyrsistent import s
print("Welcome sARA  to Snake, Water, Gun game\n", end='^_^')
print("Rules are simple: \n Press alternate keys for Snake(S), Water(W) or Gun(G)")

def game(comp,you):
    if comp==you:
        return None
    elif comp=="s":
        if you=="w":
            return False
        else:
            return True
    elif comp=="w":
        if you=="g":
            return False
        else:
            return True
    elif comp=="g":
        if you=="s":
            return False
        else:
            return True


randnum= random.randint(1,3)
if randnum==1:
    comp="s"
elif randnum==2:
    comp="w"
elif randnum==3:
    comp="g"


print("Computer turn : Snake(S), Water(W) or Gun(G) ??")
you= input("Enter your choice: Snake(S), Water(W) or Gun(G) ??")

a = game(comp,you)

print(f"computer choose {comp}")
print((f"you choose {you}"))
if (a==None):
    print("This is a Tie!!")
elif a:
    print("**********Congratulation********\n (^_^) You Win ")
else:
    print(":( Better luck Next Time :(")    
