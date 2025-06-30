# if

temp = int(input("Enter a temperature : "))

if temp < 0:
    print("Sovuq kun, issiqroq kiying!")
elif -20 < temp < 0:
    print("Ob-havo yaxshi, lekin sal sovuq.")
elif temp > 20:
    print("Juda yaxshi ob-havo, zavqlaning!")


age = int(input("enter age : "))
goals = int(input("enter goals : "))

if age < 18:
    if goals > 1:
        print("Yosh iste’dod!")
    else:
        print("Mashq qilish kerak.")
elif 18 < age < 35:
    if goals > 3:
        print("Yulduz futbolchi!")
    else:
        print("Oddiy futbolchi.")
elif age > 35:
    if goals > 1:
        print("Mag‘lubiyatsiz veteran!")
    else:
        print("Tajribali murabbiy.")

# for

sonlar = [1, 2, 7, 10, 8]
maxx = float("-inf")
for i in sonlar:
    if maxx < i:
        maxx = i
print(maxx)

minn = float("inf")
for i in sonlar:
    if minn > i:
        minn = i
print(minn)

summ = 0
for i in sonlar:
    summ += i
print(summ)

mull = 1
for i in sonlar:
    mull *= i
print(mull)


for i in range(1, 10):
    print()
    for j in range(1, 10):
        print(f"{j} * {i} = {i * j}", end="\t")
        print(end="\t")
print()

# while
import random

a = random.randint(1, 20)
att = 0
while True:
    att += 1
    ans = int(input("enter a num : "))
    if ans == a:
        print("Tabriklaymiz!")
        print(f"{att} - urunush soni")
        break
    else:
        if ans < a:
            print("your ans is less")
        else:
            print("your ans is greater")
