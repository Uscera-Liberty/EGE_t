# for i in range(1,1000):
#     x = bin(i)[2:]
#     if x[-1] == 0:
#         x1 = str(x) + '00'
#     else:
#         x1 = str(x) + '11'
#
#     if int(x1,2) > 115:
#         print(i)
# for i in range(1,1000):
#     s = i
#     n = 80
#     while s + n < 160:
#       s = s + 15
#       n = n - 10
#     if s < 100:
#         print(i)

# from itertools import permutations
# c = 0
# for x in permutations('ventily',7):
#     i = ''.join(x)
#     if i[-1] != 'y' and i.count('eyi') == 0 and i.count('iye') == 0:
#         c+=1
#         print(i)
# print(c)

# s = 143 * '687'
#
# while '68' in s or '777' in s:
#     s = s.replace('68','7',1)
#     s = s.replace('7777','7',1)
# print(s)



# for a in range(1,1000):
#     f = 1
#     for x in range(1,1000):
#         f *= (x%a==0)<=((x%14 == 0)and(x%21==0))
#     if f:
#         print(a)
#         break

# def F(n):
#   if n > 1:
#     return 2*n + \
#            F(n-2)+F(n-3)
#   else:
#     return n + 5
#
# print(F(6))

# f=open('17-3.txt')
# a=[int(i) for i in f]
# c=0
# s = []
# for i in range (len(a)-2):
#     if a[i] < a[i+1] and a[i+1] < a[i+2]:
#         c+=1
#         s.append(a[i+2] - a[i])
# print(c)
# print(min(s))
# for i in range(1,1000):
#     x = i
#     a = 0
#     b = 0
#     while x > 0:
#       a = a + 1
#       b = b + (x % 10)
#       x = x // 10
#     if a == 2 and b== 12:
#         print(i)

# def kolpr(a, b):
#   if a == b:
#     return 1
#   if a > b:
#     return 0
#   return kolpr(a + 1, b) + kolpr(a + 11, b)
#
#
# print(kolpr(3, 12)+kolpr(12,30))
# def p(n):
#     if n % 2 == 0:
#         return n == 2
#     d = 3
#     while d * d <= n and n % d != 0:
#        d += 2
#     return d * d > n
# s = []
# for x in range(2948,20194):
#     if p(x):
#         s.append(x)
# print(max(s))
