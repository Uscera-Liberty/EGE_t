# def f(n):
#     if n == 0 :
#         return 1
#     if n == 1:
#         return 3
#     if n > 1:
#         return f(n-1) - f(n-2)+3*n
# print(f(40))
# #126

# f = open('17-4.txt')
# a = [int(i) for i in f]
# f.close()
# s =[]
# for j in a:
#     list_int = sum([int(i) for i in str(j)])
#     if list_int%9 != 0 and list_int%5 == 0:
#         s.append(j)
# print(len(s))

# def f(x,p):
#     if x >= 25 and p == 3:
#         return True
#     else:
#         if x < 25 and p == 3:
#             return False
#     return f(x+1, p+1) or f(x*2,p+1)
#
# for i in range(1,24):
#     if f(i,1):
#         print(i)
#         break
#
#
#
# def f(x,p):
#   if x  >= 25 and p == 4:
#     return True
#   else:
#     if x < 25 and p == 4:
#       return False
#     else:
#       if x  >= 25:
#         return False
#   if p % 2 == 1:
#     return f(x + 1, p + 1) or f(x * 2, p + 1)
#   else:
#     return f(x+1, p+1) and f(x*2, p+1)
#
# for i in range(1,53):
#   if f(i,1):
#     print(i)
#
#
# def f(x,p):
#   if x  >= 25 and (p == 3 or p == 5):
#     return True
#   else:
#     if x < 25 and p == 5:
#       return False
#     else:
#       if x  >= 25:
#         return False
#   if p % 2 == 0:
#     return f(x + 1, p + 1) or f(x * 2, p + 1)
#   else:
#     return f(x+1, p+1) and f(x*2, p+1)
#
#
# def f1(x,p):
#   if x  >= 25 and p == 3:
#     return True
#   else:
#     if x < 25 and p == 3:
#       return False
#     else:
#       if x  >= 25:
#         return False
#   if p % 2 == 0:
#     return f(x + 1, p + 1) or f(x * 2, p + 1)
#   else:
#     return f(x+1, p+1) and f(x*2, p+1)
#
#
# for i in range(1,65):
#   if f(i,1):
#     print(i)
# print("==========")
# for i in range(1,65):
#   if f1(i , 1):
#     print(i)

# with open('24.txt', ) as f:
#     text = f.read()
#     maxx = ''
#     temp = text[0]
#     c = 0
#     for i in range(1, len(text)):
#         if ord(text[i]) > ord(text[i - 1]):
#             temp += text[i]
#             if len(temp) > len(maxx):
#                 maxx = temp
#         else:
#             temp = text[i]
#
#     print(maxx)
# #     print(c)
# for i in range(1,1000):
#     x = i
#     a = 0; b = 1
#     while x > 0:
#       a = a + 1
#       b = b*(x%10)
#       x = x//10
#     if a == 2 and b == 24:
#         print(i)

# def kolpr(a, b):
#   if a == b:
#     return 1
#   if a > b:
#     return 0
#   return kolpr(a + 1, b) + kolpr(a + 3, b) + kolpr(a*2 , b)
#
#
# print(kolpr(3,15))
#
# s = []
# c = 0
# i = 2095133040
# for j in range( 1 , i):
#     if i%j == 0 :
#       s.append(j)
# if c == 1600:
#     print(s)

# f = open("27-29b.txt")
# n = int(f.readline())
#
# def get():
#     a = list(map(int , f.readline().split()))
#     return (a[0] + a[1] , a[1] + a[2] , a[0] + a[2])
#
# s = get()
#
# for i in range(n-1):
#     para = get()
#     cmb = [a+b for a in s for b in para]
#     s1 = [0] * 5
#     for x in cmb :
#         if x > s1[x%5] : s1[x%5] = x
#     s = [x for x in s1 if x != 0 ]
# print(max(s[1:]))

# f = open('26-k2.txt')
# n = list(map(int, f.readline().split()))
# a = list(map(int, f.read().split()))
# print(a)
# a1 = sorted(a)
# a_new = a1[n[1] + 1:n[0] - n[1]]
# print(a_new)
# print(max(a_new))
# print(sum(a_new) / len(a_new))