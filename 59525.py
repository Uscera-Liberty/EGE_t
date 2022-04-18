# for i in range(1,1000):
#     n = bin(i)[2:]
#     n = n + n[-1]
#     if n.count('1')%2 == 0:
#         n += '1'
#     else:
#         n+='0'
#     if n.count('1')%2 == 0:
#         n += '1'
#     else:
#         n+='0'
#
#     if int(n,2) > 114:
#         print(int(n,2))

# for i in range(1,1000):
#     s = i
#     n = 1
#     while n < 21:
#       s = s - 1
#       n = n + 2
#     if s > 600:
#         print(i)

# s1 = []
#
# for i in range(1000, 10000):
#     s1 = str(i)
#
#     while '900' in s1 or '8' in s1 or '70' in s1:
#
#         if '900' in s1:
#             s1 = s1.replace('900', '8000', 1)
#             if len(s1) == 71:
#                 print(i)
#                 break
#
#         if '70' in s1:
#             s1 = s1.replace('70', '900', 1)
#             if len(s1) == 71:
#                 print(i)
#                 break
#
#         if '8' in s1:
#             s1 = s1.replace('8', '70', 1)
#             if len(s1) == 71:
#                 print(i)
#                 break

# s = 2*9**10 - 3**5 + 5
# strw = ''
# while s:
#     strw = str(s % 3) + strw
#     s//=3
# print(strw.count('2'))


# for a in range(1,1000):
#     f = 1
#     for x in range(1,1000):
#         f*= ((x//50>3) or (not(x//13>3)) or (x//a>6))
#     if f:
#         print(a)
#         break
# print('17')
# s = []
# with open('17-1.txt') as f:
#     a = [int(i) for i in f ]
#     sr = sum(a)/len(a)
#     c = 0
#     for n in range(len(a)-2):
#         if (a[n] > sr and a[n+1]>sr) or (a[n] > sr and a[n+2]>sr) or (a[n+1] > sr and a[n+2]>sr):
#             c+=1
#             s.append(a[n]+a[n+1]+a[n+2])
#     print(c)
#     print(max(s))
#
# print('22')
# for i in range(1,1000):
#     x = i
#     L = 0; M = 0
#     while x > 0:
#       L = L + 1
#       if x % 2 == 0:
#         M = M + (x % 10) // 2
#       x = x // 10
#     if L==3 and  M == 7:
#         print(i)
# print('23')
def kolpr(a, b):
  if a == b:
    return 1
  if a > b:
    return 0
  return kolpr(a + 1, b) + kolpr(a * 2, b) + kolpr(a*3,b)


print(kolpr(2,12) * kolpr(12,28))
# print('24')
# f = open('24-j5.txt', 'r')
# s = f.read()
# k = 0
# for i in range(len(s)-6):
#   if s[i:i+6] == "SOCKOS":
#     k += 1
# print(k)
# print('25')
# def m(n):
#   if n % 2 == 0:
#     return n == 2
#   d = 3
#   while d * d <= n and n % d != 0:
#     d += 2
#   return d * d > n
# c = 0
# for i in range(2,20000):
#   if m(i):
#     c+=1
# print(c)
#
