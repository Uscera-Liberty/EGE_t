# def alg(n):
#     return (255^n) - n
# #==============================================================================
# for n in range(256):
#     if alg(n) == 99:
#         print(n)

# for i in range(1 , 1000):
#     s = i
#     n = 50
#     while s > 0:
#         s = s // 2
#         n = n - 3
#     if n == 23:
#         print(i)
#         break

# from itertools import permutations
# a = set()
# for x in permutations('mimikriy'):
#     w = ''.join(x)
#     a.add(w)
# print(a)
# print(len(a))
#
# for n in range(200 , 1000):
#     s = "8"*n
#     while '555' in s or '888' in s:
#         s = s.replace("555" , '8' , 1)
#         s = s.replace("888" , '55' , 1)
#     if s.count('8') > s.count('5'):
#         print(n)
#         break

# x = 9**17 + 3**16 - 27
# s = ''
# while x:
#     s = str(x%3) + s
#     x//=3
# print(s.count('0') , s.count('1') , s.count('2'))

# for a in range(1 , 1000):
#     f = 1
#     for x in range(1 , 1000):
#         for y in range(1 , 1000):
#             f*=(x**2 - 3*x + 2 > 0) or (y > x**2+7) or (x*y < a)
#     if f:
#         print(a)
#         break

# def f(n):
#     if n == 1:
#         return 2
#     elif n > 1:
#         return f(n-1) + 5*n**2
# print(f(39))

# s = "1001001001001001001001"
# print(s[-1:-5:-1])
# def put(n):
#     s = ''
#     while n:
#         s = str(n%5) + s
#         n//=5
#     return s
# with open('17-4.txt') as f:
#     a = [int(i) for i in f]
#     s = []
#     for i in a:
#         if bin(i)[-1:-5:-1] == '1001' and put(i)[-1:-3:-1] == '11':
#             s.append(i)
# print(max(s) , sum(s))

# def kolpr(a, b):
#   if a == b:
#     return 1
#   if a > b:
#     return 0
#   return kolpr(a + 1, b) + kolpr(a * 2, b) + kolpr(a * 3 ,b)
#
# print(kolpr(2 ,7) + kolpr(7 ,28))
#
# with open(r'24.txt', 'r') as f:
#     text = f.read()
#
# maxx = ''
# temp = text[0]
# for i in range(1, len(text)):
#     if ord(text[i]) < ord(text[i - 1]):
#         temp += text[i]
#         if len(temp) > len(maxx):
#             maxx = temp
#     else:
#         temp = text[i]
#
# print(maxx)