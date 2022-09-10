# for n in range(100 , 999+1):
#     a = sorted([str(i) for i in str(n)])
#     if int(a[2] + a[1]) - int(a[0] + a[1]) == 50:
#         print(n)
#
# for i in range(1 , 1000):
#     s = i
#     n = 40
#     while s + n < 100:
#         s = s + 25
#         n = n - 5
#     if s == i:
#         print(i)
#         break
#
# s = 3*'2'+ 18*'5'
# while '222' in s or '888' in s:
#     while '555' in s:
#         s = s.replace('555' , '8' , 1)
#     if '222' in s:
#         s = s.replace('222' , '8' , 1)
#     else:
#          s = s.replace('888' , '2' , 1)
#
# print(s)

# def f(n):
#     s = ''
#     while n:
#         s = str(n%7) + s
#         n//=7
#     return s.count('6')
# print(f(49**12 - 7**10 + 7**8 - 49))
#
# for a in range(1 , 1000):
#     f = 1
#     for x in range(1 , 1000):
#         f*=(x&49 != 0) <= ((x&33 == 0) <= (x&a != 0))
#     if f:
#         print(a)
#         break

# def f(n):
#     if n < 1:
#         return n
#     elif n >= 1 and n%2 == 0:
#         return n+3*f(n-3)
#     elif n >= 1 and n%2 ==1:
#         return 5*n+2*f(n-5)
# print(f(30))
# c = 0
# s = []
# with open('17-9.txt') as f:
#     a = [int(i) for i in f]
#     for j in range(len(a) - 2):
#         if ((bin(a[j])[2:].count('1') >= 3 and bin(a[j+1])[2:].count('1') >= 3) and (bin(a[j])[2:].count('0') >= 1 and bin(a[j+1])[2:].count('0') >= 1)) or ((bin(a[j])[2:].count('1') >= 3 and bin(a[j+2])[2:].count('1') >= 3) and (bin(a[j])[2:].count('0') >= 1 and bin(a[j+2])[2:].count('0') >= 1)) or ((bin(a[j+2])[2:].count('1') >= 3 and bin(a[j+1])[2:].count('1') >= 3) and (bin(a[j+2])[2:].count('0') >= 1 and bin(a[j+1])[2:].count('0') >= 1)):
#             c+=1
#             s.append(max(a[j] , a[j+1] , a[j+2]))
# print(c)
# print(max(s))

# for i in range(1 , 1000):
#     x = i
#     L = 0
#     M = 9
#     while x > 5:
#         L = L + 1
#         if M > (x % 10):
#             M = x % 10
#         x = x // 10
#     if L == 3 and M == 4:
#         print(i)

# def kolpr( a, b ):
#     if a == b:
#         return 1
#     if a < b :
#         return 0
#     if a > b:
#         return kolpr(a-1,b) + kolpr(a//2,b)
# a = int('100001', 2)
# b = int('100', 2)
# print(kolpr(a,b))

# with open('24-j2.txt') as f:
#     s = ''
#     c = 0
#     max = 0
#     for i in f:
#         s += str(i)
#     for j in range(len(s) - 1):
#         if s[j] == s[j+1]:
#             c += 1
#         else:
#             if c > max:
#                 max = c
#             c = 0
# print(max)
# a = []
# for i in range(2, 50000):
#     k = True
#     for j in range(2, i // 2 + 1):
#         if i % j == 0:
#             k = False
#             break
#     if k == True:
#         a.append(i)
# count = 0
# maximum = 0
# k = []
# n = 1
# for i in range(105673, 220784):
#     for elem in a:
#         if i % elem == 0:
#             k.append(elem)
#             n = n * elem
#             if len(k) == 3:
#                 if n == i:
#                     count += 1
#                     if i > maximum:
#                         maximum = i
#                 break
#     k = []
#     n = 1
# print(count, maximum)