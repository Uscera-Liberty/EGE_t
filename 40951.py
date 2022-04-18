# for i in range(1,1000):
#   s = i
#   n = 6
#   while s <= 154:
#     s = s + 12
#     n = n + 3
#   if n == 42:
#     print(i)
# from itertools import product
#
# a = list(product('ABCDE', repeat=4))
# n = 0
# for el in a:
#   ell = list(el)
#   if ell == sorted(ell):
#     print(el)
#     n += 1
# print(n)

# for i in range(300,1000):
#   s = i * '8'
#   while '555' in s or '888' in s:
#     s = s.replace('555','8',1)
#     s = s.replace('888','55',1)
#   if s.count('8') < s.count('5'):
#     print(i)
#     break

# def f(n2):
#   sum = n2.count('1')
#   n2 = str(n2) + str(sum%2)
#   return n2
#
#
# for n in range(1,1000):
#   n2 = bin(n)[2:]
#   n3 = f(n2)
#   n4 = f(n3)
#   r = int(n4,2)
#   if r > 150:
#     print(n)

# x = (7**160 * 7**90) - (14**150 + 2**13)
# sum2 = 0
# while x:
#   if x % 7 != 6:
#     sum2 += x%7
#   else:
#     sum2 += 0
#   x//=7
#
# print(sum2)

# def f(n):
#   if n < 2:
#     return 1
#   elif n >= 2 and n%3 == 0:
#     return f(n/3) + 1
#   else:
#     return f(n-2) + 5
#
# for i in range(5,6000):
#   if f(i) == 73:
#     print(i)


f = open('17-8.txt')
a = [int(i) for i in f]
c = 0
s = []
for i in range(len(a)-1):
    dv1 = bin(a[i])[2:]
    dv2 = bin(a[i+1])[2:]
    dig1 = [int(x) for x in str(a[i])]
    dig2 = [int(x) for x in str(a[i+1])]
    if (dv1.count('1') > 5 and dv1.count('1')%2!=0) or (dv2.count('1') > 5 and dv2.count('1')%2!=0):
        c+=1
        s += [a[i] + a[i+1]]
print(c)
print(max(s))

# for i in range(10000 , 1000000):
#     x = i
#     a = 0
#     b = 0
#     while x > 0:
#       y = x % 10
#       if y > 3: a = a + 1
#       if y < 8: b = b + 1
#       x = x // 10
#     if a == 4 and b == 2:
#         print(i)

# def kolpr( a, b ):
#     if a == b:
#         return 1
#     if a > b or a == 8:
#         return 0
#     if a < b:
#         return kolpr(a+1,b)+ kolpr(a+2,b) + kolpr(a+3,b)
# print(kolpr(3,15))