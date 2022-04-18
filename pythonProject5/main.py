# s = ''
# s1 = ''
# for x in range(1,256):
#     s = bin(x - 1)[2:].zfill(8)
#     s1 = bin(255 - int(s,2))
#     r = int(s1,2)
#     if r == 18:
#         print(x)

# for x in 1,0:
#     for y in 1,0:
#         for z in 1,0:
#             for w in 1,0:
#                 if ((x <= y)and(y <= w)) or (z == (x or y)) == 0:
#                     print(x,y,z,w)

# for i in range(1,1000):
#     n = bin(i)[2:]
#     n1 = str(n) + n[-1]
#     if n1.count('1')%2 == 0:
#         n2 = str(n1) + '0'
#     else:
#         n2 = str(n1) + '1'
#
#     if n2.count('1')%2 == 0:
#         n3 = str(n1) + '0'
#     else:
#         n3 = str(n1) + '1'
#     r = int(n3,2)
#     if r > 114:
#         print(r)
#         break

# for i in range(1,1000):
#     x = i
#     s = 5 * (x // 10)
#     n = 1
#     while s < 300:
#       s = s + 28
#       n = n * 3
#     if n == 243:
#         print(i)

# from itertools import permutations
# a = list()
# for i in permutations('mimikria',8):
#      x = ''.join(i)
#      a.append(x)
# a = set(a)
# print(len(a))
# s = 143 * '7'
# while '777' in s:
#      s = s.replace('777','22',1)
#      s = s.replace('222','7')
# print(s)

# s = 4**2014 + 2**2015 - 8
# print(bin(s).count('1'))


# temp = 0
# for a in range(1,1000):
#      f = 1
#      for x in range(1, 1000):
#           f *= (110 % a == 0) and ((x%80==0)and(x%75==0) ) <= (x%a==0)
#           if f == 0:
#                break
#      if f:
#           temp = a
#
# print(temp)

# def F(n):
#      if n == 0:
#           return 2
#      if 0 < n <= 15:
#           return F(n-1)
#      if 15<n<95:
#           return 1,6*F(n-3)
#      if n >= 95:
#           return 3,3*F(n-2)
# print(F(33))
# print(F(33))

# for i in range(1,1000):
#      x = i
#      a = 0; b = 10
#      while x > 0:
#        c = x % 10
#        a = a + c
#        if c < b:
#          b = c
#        x = x // 10
#      if a == 15 and b == 5:
#           print(i)

# def f( a, b ):
#     if a == b:
#         return 1
#     if a > b :
#         return 0
#     return f(a+3,b)+ f(a*2,b)
# print(f(12,96))

data = [int(x) for x in open('17-199.txt')]
def cond(x):
     return 100 <= x < 1000 and x % 10 == 5

ma = 0
count = 0
for i in range(2, len(data)):
     if (not cond(data[i - 2])) and cond(data[i - 1]) and \
             (not cond(data[i])):
          count += 1
          ma = max(ma, sum(data[i - 2:i + 1]))
print(count, ma)