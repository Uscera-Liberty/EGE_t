# # def move(x):
# #     return x+1,x+2, x+3,x*2
# #
# # def wiv(x):
# #     return x > 37
# #
# # pos = [0] * 37*2
# # for i in range(1 , 37):
# #     if any(wiv(h) for h in move(i)):
# #         pos[i] = 1
# #
# # print('s p')
# # print(*[(s , p) for s, p in enumerate(pos)])
#
# # def f(x):
# #     d = set()
# #     for i in range(2 , int(x**0.5)+1):
# #         if x%i == 0:
# #             d.add(x//i)
# #             d.add(i)
# #     return sorted(d)
# #
# # for x in range(550000 , 551000):
# #     a = [i for i in f(x) if i%10 == 7]
# #     if len(a) == 3:
# #         print(x, a[-1])
#
# def f(x):
#     d = set()
#     for i in range(2 , int(x**0.5)+1):
#         if x%i == 0:
#             d.add(x//i)
#             d.add(i)
#     return sorted(d)
#
# def isPrime(n):
#     if n % 2 == 0:
#         return n == 2
#     d = 3
#     while d * d <= n and n % d != 0:
#         d += 2
#     return d * d > n
#
# for x in range(125697 , 125721):
#     a = [i for i in f(x) if isPrime(i)]
#     if len(a) == 2 and a[0]*a[1] == x:
#         print(a[0], a[1])

# for a in range(1 , 1000):
#     f = 1
#     for x in range(1 , 1000):
#         f*=((x%15== 0) and (x%21!=0)) <= ((x%a != 0) or (x%15!= 0))
#     if f:
#         print(a)
#         break
# for x in range(1 , 1000):
#     n = bin(x)[2:]
#     if x%2 == 0: n1 = str(n)+'01'
#     else: n1 = str(n)+'10'
#     if int(n1 , 2) > 97:
#         print(x)
# for x in range(1 , 1000):
#     d = x
#     n = 0
#     s = 0
#     while s <= 365:
#       s = s + d
#       n = n + 5
#     if n == 55:
#         print(x)


# def f(x):
#     global t
#     t += x**2
#     if x > 1:
#         t +=2*x+1
#         f(x-2)
#         f(x//3)
#
# for x in range(100  ,200+1):
#     t = 0
#     if t > 3200000:
#         print(x , t)




# def kolpr(a, b):
#   if a == b:
#     return 1
#   if a > b:
#     return 0
#   return kolpr(a + 2, b) + kolpr(a + 3, b) + kolpr(a+5 , b)
#
#
# print(kolpr(20, 35))

# def f(x):
#     d = set()
#     for i in range(1 , int(x**0.5)+1):
#         if x%i == 0:
#             d.add(x//i)
#             d.add(i)
#     return sorted(d)
#
# for x in range(194455 , 194500):
#     a = [i for i in f(x)]
#     if len(a) == 4:
#         print(a[-2] , a[-1])

#
# with open(r'24-4.txt', 'r') as f:
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
# print(len(maxx) , maxx)

# def f(s1,s2,c,m):
#     if s1+s2>=62: return c%2==m%2
#     if c==m: return 0
#     h=[f(s1+2,s2,c+1,m),f(s1,s2+2,c+1,m),\
#        f(s1*2,s2,c+1,m),f(s1,s2*2,c+1,m)]
#     if (c+1)%2==m%2:
#         return any(h)
#     else:
#         return all(h)

# for s2 in range (1,55):
#     for m in range (1,5):
#         if f(7,s2,0,m)==1:
#             print(s2,m)

# def prime(x):
#     return x>1 and all(x%i!=0 for i in range(2 , int(x**0.5)+1))
#
# for x in range(55_000_000 , 60_000_001):
#     t = x
#     while t%2 == 0: t = t//2
#     if int(x**0.25)**4 == t and prime(int(t**0.25)):
#         print(x , t)

# def f(s1,s2,c,m):
#     if s1+s2>=62: return c%2==m%2
#     if c==m: return 0
#     h=[f(s1+2,s2,c+1,m),f(s1,s2+2,c+1,m),f(s1*2,s2,c+1,m),f(s1,s2*2,c+1,m)]
#     if (c+1)%2==m%2:
#         return any(h)
#     else:
#         return any(h)
#
# for s2 in range (1,55):
#     for m in range (1,5):
#         if f(7,s2,0,m)==1:
#             print(s2,m)
#
# def f(s , c , m):
#     if 43 <= s <= 52: return c%2 == m%2
#     elif c > 52 :return c%2 != m%2
#     if c==m: return 0
#
#     h = [f() , f() ]
#     return any(h) if (c+1)%2 == m%2 else all(h)

#код нельзя повторять предыдущий ход данного противника
#p0- ход предыдущего игрока
#p1- наш предыдущий ход

# def f(s , p0 , p1 , c, m):
#     if s >= 38:return c%2 == m%2
#     if c == m : return 0
#
#     h = []
#     if p1 != '+1': h += [f(s+1, '+1', p0, c+1, m)]
#     if p1 != '+2': h += [f(s + 1, '+2', p0, c + 1, m)]
#     if p1 != '*2': h += [f(s + 1, '*2', p0, c + 1, m)]

#
# def prime(x):
#     return x>1 and all(x%i!=0 for i in range(2 , int(x**0.5)+1))
# t = 0
# for x in range(113_000_000  , 114_000_000):
#     if x%2 == 0 and x%4!=0:
#         t += x//2
#     if int(x**0.5)**2 == t and prime(int(t**0.5)):
#         print(x , 2*int(t**0.5))

# import math
# def f(s1 , s2 , c , m):
#     if s1+s2 <= 19:return c%2 == m%2
#     if c==m: return 0
#     h = [f(s1-1 ,s2 , c+1 , m) ,f(math.floor(s1/2) ,s2 , c+1 , m) , f(s1 , s2-1, c+1 , m) , f(s1 , math.floor(s2/2), c+1 , m)]
#     return any(h) if (c+1)%2 == m%2 else all(h)
#
# for s1 in range(5 , 19):
#     s2 = s1
#     if s1+s2 >= 19:
#         for m in range(1 , 5):
#             if f(s1 , s2 , 0 , m):
#                 if m == 2 and s1 == s2:
#                     print(s1 , s2)
#     else: continue
#
#
#     def f(s, p, c, m):
#         if s >= 140:  return c % 2 == m % 2
#
#         if c == m: return 0
#         h = []
#         if p != '+1': h += [f(s + 1, '+1', c + 1, m)]
#         if p != '+2': h += [f(s + 2, '+2', c + 1, m)]
#         if p != '*3': h += [f(s * 3, '*3', c + 1, m)]
#         return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
#
#     for s in range(1, 140):
#         for m in range(1, 5):
#             if f(s, '', 0, m) == 1:
#                 print(s, m)
#                 breakd

