

# for a in 1,0:
#     for b in 1,0:
#         for c in 1,0:
#             for d in 1,0:
#                 if ((a and b) == (not(c))) and ( b <= d):
#                     print(a,b,c,d)

# c=0
# for i in range(10000,100000):
#     s = str(i)
#     a=[int(s[0]) + int(s[2]) + int(s[4]), int(s[1]) + int(s[3])]
#     a.sort()
#     if a[0] == 7 and a[1] == 23:
#         print(i)
# for i in range(1,1000):
#     s = i
#     n = 1
#     while s < 28:
#       s = s + 5
#       n = n * 3
#     if n == 81:
#         print(i)

# from itertools import permutations
# g = 'oa'
# s = 'nd'
# c = 0
# for x in permutations('noda',4):
#     i = ''.join(x)
#     for j in range(1,3):
#         if (i[j] not in g and i[j-1] not in g) or (i[j] not in s and i[j-1] not in s):
#             c+=1
# print(c)
from functools import reduce
from operator import add

# for i in range(1,1000):
#     s = 8*'2' + i *'3'
#     while '32' in s:
#         s = s.replace('32','6',1)
#
#     sum = 0
#     for i in range(0, len(s)):
#         sum = sum + int(s[i])
#     if sum == 94 :
#         print(i)

# for i in range(3,20):
#     x = 86
#     s = ''
#     while x:
#         s = str(x%i) + s
#         x//=i
#     print(s)

# for a in range(61,1000):
#     f = 1
#     for x in range(1,1000):
#         f *= ((x%a == 0)<= ((x%54==0) or (x%130==0))) and (a > 60)
#     if f:
#         print(a)
#         break
# for i in range(1,1000):
#   x = i
#   L = 0; M = 0
#   while x > 0:
#     L = L + 1
#     if x % 2 == 1:
#       M = M + (x % 10) // 2
#     x = x // 10
#   if L == 3 and M == 7:
#     print(i)

# def f( n ):
#   global c
#   c+=1 #print('*')
#   if n >= 1:
#     c+=1 #print('*')
#     f(n-1)
#     f(n-3)
#     c+=1
# c=0
# f(40)
# print(c)

# def kolpr(a, b):
#   if a == b:
#     return 1
#   if a > b:
#     return 0
#   return kolpr(a + 1, b) + kolpr(a + 3, b)
#
#
# print(kolpr(3, 12)+kolpr(12,30)) #?????????????

# f=open('17-3.txt')
# a=[int(i) for i in f]
# k=0
# for i in range (len(a)-1):
#     sr = ((a[i]+a[i+1])/2)
#     if ((a[i] * a[i+1])%2 == 1) and (sr% 7 == 0):
#         k=k+1
#         print(sr)
# print(k)
# for i in range(1,1000):
#     x = i
#     L = 0; M = 0
#     while x > 0:
#         L = L + 1
#         if x % 2 == 0:
#             M = M + (x % 10)
#         x = x // 10
#     if L == 3 and M == 8:
#         print(i)
#
# def s(a, *vs, b=10):
#    res = a + b
#    for v in vs:
#        res += v
#    return res
#
# print(s(11, b=20))
# print(s(0, 0, 31))
# print(s(5, 5, 5, 5, 1))
# print(s(21))
#
# print(s(11, 10, b=10))
# print(s(11, 10, 10))
#
# print(s(11, 10))
x, y = 1, 2

def foo():
    global y
    if y == 2:
        x = 2
        y = 1

foo()
print(x)
if y == 1:
    x = 3
print(x)