# for n in range(50,1000):
#     n2 = bin(n)[2:]
#     n3 = str(n2) + n2[-2]
#     n4 = str(n3) + n2[2]
#     r = int(n3,2)
#     if r > 170:
#         print(n)
#
# for i in range(1,1000):
#     s = i
#     n = 4
#     while s < 37:
#         s = s + 3
#         n = n * 2
#     if n == 128 :
#         print(i)
#         break

# from itertools import permutations
# a = list()
# for i in permutations('tartar',6):
#      x = ''.join(i)
#      a.append(x)
# a = set(a)
# print(len(a))


# s = 130 * '1'
# while '111' in s:
#      s = s.replace('111','2',1)
#      s = s.replace('222','3',1)
#      s = s.replace('333','1',1)
# print(s)
#
# for i in range(2,11):
#      a = [ ]
#      x = 611
#      while x:
#          a.append(x % i)
#          x = x // i
#      if len(a) %2 != 0:
#           print(i)



# for a in range(1,1000):
#      f = 1
#      for x in range(1,1000):
#           f *= (x & 107 == 0) <= ((x&55!=0)<=(x&a!=0))
#      if f:
#           print(a)
#           break
# def g(n):
#      if n == 1:
#           return 1
#      if n > 1:
#           return 3*g(n-1) + f(n-1) - 3*n
#
# def f(n):
#      if n == 1:
#           return 1
#      if n > 1:
#           return 3*f(n-1) + g(n-1) - n + 5
#
# print(f(14)+g(14))


# f=open('17-3.txt')
# # a=[int(i) for i in f]
# # c = 0
# # s = []
# # for i in range (len(a)-1):
# #     dv1 = bin(a[i])[2:]
# #     dv2 = bin(a[i+1])[2:]
# #     if (dv1.count('1') > 5 and dv1.count('1')%2!=0) or (dv2.count('1') > 5 and dv2.count('1')%2!=0):
# #         c+=1
# #         s.append(max(dv1.count('1'),dv2.count('1')))
# # print(c)
# # print(max(s))
# for i in range(1,1000):
#     x = i
#     a = 0; b = 1
#     while x > 0:
#       a = a + 1
#       b = b * (x % 100)
#       x = x // 100
#     if a == 2 and b == 5:
#         print(i)

# def kolpr( a, b ):
#     if a == b:
#         return 1
#     if a > b or a == 15:
#         return 0
#     if a < b:
#         return kolpr(a+1,b)+ kolpr(a*2,b)
# print(kolpr(1,10) + kolpr(10,30))
#КОТ
f = open('24-j1.txt', 'r')
s = f.read().strip()
m = 0
k = 0
i = 0
while i < len(s)-2:
    if s[i:i+3] == 'КОТ':
        k += 1
        if k > m:
            m = k
        i += 3
    else:
        k = 0
        i += 1
print(m)