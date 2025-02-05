# n = 0
# ans = []
# if n == 0:
#     ans.append(0)
#     new = ans[::-1]
# elif n == 1:
#     ans.append(1)
#     new = ans[::-1]
# elif n > 1:
#     while True:
#         if n == 2:
#             ans.append(0)
#             break
#         elif n % 2 == 0:
#             n //= 2
#             ans.append(0)
#         elif n % 2 != 0:
#             n //= 2
#             ans.append(1)
#     ans.append(1)
#     new = ans[::-1]
#
# print(new)


i = int(input("Enter a number: "))
done = []
ans = []
for n in range(0, i + 1):
    if n == 0:
        new = 0
    elif n == 1:
        ans.append(1)
        new = 1
    elif n > 1:
        while True:
            if n == 2:
                ans.append(0)
                break
            elif n == 1:
                break
            elif n % 2 == 0:
                n //= 2
                ans.append(0)
            elif n % 2 != 0:
                n //= 2
                ans.append(1)
        ans.append(1)
        new = sum(ans[::-1])
    done.append(new)
print(done)


