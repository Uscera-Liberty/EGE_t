# c = 0
# for i in range(1,1000):
#     s = i
#     n = 10
#     while s - n < 1000:
#       s = s + n
#       n = n + 5
#     if n == 80:
#         c+= 1
# print(c)

from itertools import product
c = 0
for x in product('kaliy',repeat=6):
    w = ''.join(x)
    if w.count('y') == 1 and w[0] != 'y' and w[5] != 'y' and w.find('iy') == -1 and w.find('yi') == -1:
        c+=1
        print(w)
print(c)
# def f(n):
#     ed = n.count('1')
#     nul = n.count('0')
#     if ed == nul:
#         return str(n) + n[-1]
#     elif ed < nul:
#         return str(n) + '1'
#     else:
#         return str(n) + '0'
# for n in range(1,90):
#     n2 = bin(n)
#     n3 = f(n2)
#     n4 = f(n3)
#     n5 = f(n4)
#
#     n6 = int(n5,2)
#     if n6%4 == 0:
#         print(n)
#

# x = str((77 + 7**77)*7**77 + 77 + 7**7)
# print(x.count('1'))
# temp = 0
# for a in range(1,1000):
#     f = 1
#     for x in range(1,1000):
#         for y in range(1,1000):
#             f*=(5*y + 3*x != 110) or (x>a) or (2*y >a)
#         if f == 0:
#             break
#     if f:
#         temp = a
#
# print(temp)

# s = '>' + 15*'1'+ 20*'2'+ 25*'3'
#
# while '>1' in s or '>2' in s or '>3' in s:
#     if '>1' in s :
#         s = s.replace('>1','22>',1)
#     if '>2' in s:
#         s = s.replace('>2','2>1',1)
#     if '>3' in s:
#         s = s.replace('>3','1>',1)
#
# l = len(s)
# s  = s[:l-1]
# c = 0
# for i in s:
#     i = int(i)
#     if i != '>':
#         c+=i
#     else:
#         break
# print(c)
# def g(n):
#     if n == 1:
#         return 1
#     if n >1:
#         return f(n-1) + 2 * g(n-1) + n
# def f(n):
#     if n == 1:
#         return 1
#     if n >1:
#         return 2*f(n-1) + g(n-1) - 2*n
#
# print(f(14) + g(14))

# f=open('17-2.txt')
# a=[int(i) for i in f]
# c = max(a)
# s = 0
# for i in range(len(a)):
#     if a[i] == c:
#         s+=1
# print(s)
# print(a.index(c))
# temp = 0
# for i in range(10000,100000):
#     x = i
#     a = 0; b = 0
#     while x > 0:
#       y = x % 10
#       if y > 4: a = a + 1
#       if y < 6: b = b + 1
#       x = x // 10
#     if a ==5 and b == 4:
#         temp = i
# print(temp)

# def kolpr(a, b):
#   if a == b:
#     return 1
#   if a > b:
#     return 0
#   return kolpr(a + 1, b) + kolpr(a * 2, b) + kolpr(a**2,b)
#
#
# print(kolpr(2,38))
