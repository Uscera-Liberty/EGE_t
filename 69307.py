# def f(x):
#     L = sorted([int(x) for x in str(x)])
#     max_d = L[2] * 10 + L[1]
#     c = L.count(0)
#     if c == 0: min_d = L[0] * 10 + L[1]
#     if c == 1: min_d = L[1] * 10
#     if c == 2: min_d = max_d
#     return max_d - min_d
# for x in range(100,1000):
#     if f(x) == 63:print(x)

# from itertools import permutations
# c = 0
# for x in permutations('zdanie' , 6):
#     w = ''.join(x)
#     if w.find('ai') == -1 and w.find('ia') == -1 and w.find('ei') == -1 and w.find('ie') == -1 and w.find('ae') == -1 and w.find('ea') == -1:
#         print(w)
#         c+=1
#
# print(c)

# s = 86 * '4'
# while '4444' in s or '7777' in s :
#     if '4444' in s :
#         s = s.replace('4444','77',1)
#     else:
#         s = s.replace('7777','44',1)
# print(s)

# x = 7**2103 - 6*7**1270 + 3*7**57 - 98
# sumdig = 0
# while x:
#     sumdig = x%7 + sumdig
#     x//=7
#
# print(sumdig)

# def f(n):
#     if n < 1:
#         return n
#     if n>=1 and n%2 == 0:
#         return n + 3*f(n-3)
#     if n>=1 and n%2 == 1:
#         return 5*n + 2*f(n-5)
#
# print(f(30))

# f = open('17-243.txt')
# a = [int(i) for i in f]
# c = 0
# s = []
# w = []
# for i in range(len(a)-1):
#     if a[i]%119 == 0:
#         w.append(a[i])
# maxw = max(w)
#
# for i in range(len(a)-1):
#     a1_list = list(map(int, str(a[i])))
#     a2_list = list(map(int, str(a[i+1])))
#     if (a[i] > maxw or a[i+1] > maxw) and (a1_list[-2:] == 21 or a2_list[-2:] == 21):
#         c+=1
#         s += [a[i] + a[i+1]]
# # print(c)
# # print(min(s))
# print(maxw)
# print(a)

# print('++++19++++')
# def f(x,p):
#   if x >= 65 and p == 3:
#     return True
#   else:
#     if x< 65 and p == 3:
#       return False
#   return f(x+1,p+1) or f(x*3,p+1)
#
# for i in range(1,65):
#   if f(i,1):
#     print(i)
#     break
# print('++++20++++')
#
# def f(x,p):
#   if x >= 65 and p == 4:
#     return True
#   else:
#     if x< 65 and p == 4:
#       return False
#     else:
#       if x >= 65:
#         return False
#   if p % 2 == 1:
#     return f(x+1,p+1) or f(x*3,p+1)
#   else:
#     return f(x + 1,p + 1) and f(x * 3, p + 1)
#
# for i in range(1,65):
#   if f(i,1):
#     print(i)
#
# print('++++21++++')
#
# def f(x,p):
#   if x >= 65 and (p == 3 or p == 5):
#     return True
#   else:
#     if x < 65 and p == 5:
#       return False
#     else:
#       if x >= 65:
#         return False
#   if p % 2 == 0:
#     return f(x+1,p+1) or f(x*3,p+1)
#   else:
#     return f(x + 1, p + 1) and f(x * 3, p + 1)
#
# def f1(x,p):
#   if x >= 65 and p == 3:
#     return True
#   else:
#     if x < 65 and p == 3:
#       return False
#     else:
#       if x >= 65:
#         return False
#   if p % 2 == 0:
#     return f1(x+1,p+1) or f1(x*3,p+1)
#   else:
#     return f1(x + 1, p + 1) and f1(x * 3, p + 1)
#
# for i in range(1,65):
#   if f(i,1):
#     print(i)
# print("==========")
# for i in range(1,65):
#   if f1(i,1):
#     print(i)
# for i in range(1,1000):
#     x = i
#     x0 = x
#     N = 0
#     while x>0:
#       d = x % 2
#       N = 10*N + d
#       x = x // 2
#     N += x0
#     if N > 9999:
#         print(i)
#
# def kolpr( a, b ):
#     if a == b:
#         return 1
#     if a > b :
#         return 0
#     if a < b:
#         return kolpr(a+1,b)+ kolpr(a*2,b)
# print(kolpr(1,10) * kolpr(10,21))


class A:
  pass


class B(A):
  pass


class C:
  pass


class D(C):
  pass


class E(B, C, D):
  pass