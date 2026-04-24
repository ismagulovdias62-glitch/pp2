import random
IA = random.randint(1,100)
d = int(input("угадай брат "))
while IA != d:
    if d < IA:
        print("to less")
    elif d > IA:
        print("to high")
    d = int(input("попробуй еще раз сачок "))
print("CORRECT MY BOY")