n = 2
ans = []
while True:
    if n == 2:
        ans.append(0)
        break
    elif n % 2 == 0:
        n //= 2
        ans.append(0)
    elif n % 2 != 0:
        n //= 2
        ans.append(1)
ans.append(1)
new = ans[::-1]
print(new)


k = 2
ans = []
num = 0
for n in range(k + 2):
    while n >= 1:
        if n == 2:
            n //= 2
            break
        elif n % 2 == 1:
            n //= 2
            num += 1
    ans.append(num)
print(ans)