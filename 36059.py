# for i in range(1 , 1000):
#     n = bin(i)[2:]
#     if i%2 == 0:
#         n+='01'
#     else:
#         n+='10'
#     if int(n , 2) > 130:
#         print(int(n , 2))
#         break
# c = 0
# for i in range(1 , 1000):
#     s = i
#     n = 1
#     while s < 54:
#         s = s + 7
#         n = n * 3
#     if n == 243:
#         c+=1
# print(c)

# from itertools import permutations
# c = 0
# for x in permutations('aport' , 5):
#     w = ''.join(x)
#     if w.count('ao') == 0 and w.count('oa') == 0:
#         c+=1
# print(c)
#
# x = 4*25**4 - 5**4 + 14
# s = ''
# while x:
#     s = str(x%5) + s
#     x//=5
# print(sum([int(i) for i in s]))

# for a in range(1 , 1000):
#     f = 1
#     for x in range(1 , 1000):
#         f *= (x%a == 0) <= ((x%34 == 0) * (x%51==0))
#     if f:
#         print(a)
# #         break
# c = 0
# def f(n):
#     if n < 3:
#         return n+1
#     elif n >= 3 and n%2 == 0:
#         return f(n-2) + n - 2
#     elif n >= 3 and n%2 == 1:
#         return f(n+2) + n +2
#
# for i in range(200, 1000 , 2):
#     if f(i) > 9999:
#         c+=1
#     else:
#         continue
# print(c)
f = open('17-243.txt')
a = [int(e) for e in f]
b = []
c = []
for i in range(len(a)):
    if a[i] % 107 == 0:
        b.append(a[i])
cymma = max(b)
for i in range(len(a) - 1):
    s = ''
    v = a[i]
    while v != 0:
        s = str(a[i] % 7) + s
        v = v // 7
    s1 = ''
    v1 = a[i + 1]
    while v1 != 0:
        s1 = str(a[i + 1] % 7) + s1
        v1 = v1 // 7

    if ((a[i] > cymma) or (a[i + 1] > cymma)) and (s.count('36') > 0 or s1.count('36') > 0):
        c.append(a[i] + a[i + 1])
print(len(c), min(c))
# for i in range(1 , 1000):
#     x = i
#     a = 0; b = 10
#     while x > 0:
#       d = x % 7
#       if d > a: a = d
#       if d < b: b = d
#       x = x // 7
#     if a+b == 11:
#         print(i)
#         break

# def kolpr(a , b):
#     if a > b:
#         return 0
#     if a == b:
#         return 1
#     if a < b:
#         return kolpr(a+1 , b) + kolpr(a*2 ,b )+ kolpr(a*3 , b)
# print(kolpr(1,18))


# file = open('k7a-3.txt')
# data = file.read()
# a = [str(i) for i in file]
# dl = 0
# max_dl = []
# for i in a:
#     if i == 'A' or i == 'B' or i=='E' or i == 'F':
#         dl += 1
#     else:
#         max_dl.append(dl)
#         dl = 0
#
# print(max_dl)
