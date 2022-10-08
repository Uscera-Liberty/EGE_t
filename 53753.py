# print('++++19++++')
# def f(x,y,p):
#   if x + y >= 75 and p == 3:
#     return True
#   else:
#     if x+ y < 75 and p == 3:
#       return False
#   return f(x+2, y ,p+1) or f(x*2,y ,p+1) or f(x, y+2 ,p+1) or f(x, y*2 ,p+1)
#
# for i in range(1,69):
#   if f(5 ,i,1):
#     print(i)
#     break
#
# print('++++20++++')
#
# def f(x,y,p):
#   if x + y >= 75 and p == 4:
#     return True
#   else:
#     if x+y < 75 and p == 4:
#       return False
#     else:
#       if x+y >= 75:
#           return False
#   if p%2 == 1:
#       return f(x+2, y,p+1) or f(x*2,y ,p+1) or f(x, y+2 ,p+1) or f(x, y*2 ,p+1)
#   else: return f(x+2,y,p+1) and f(x*2,y ,p+1) and f(x, y+2 ,p+1) or f(x, y*2,p+1)
#
# for i in range(1,69):
#   if f(5,i,1):
#     print(i)

# print('++++21++++')
#
# def f(x,y,p):
#   if x + y >= 75 and (p == 3 or p == 5):
#     return True
#   else:
#     if x+y < 75 and p == 3:
#       return False
#     else:
#       if x+y >= 75:
#           return False
#   if p%2 == 1:
#       return f(x+2, y ,p+1) or f(x*2,y ,p+1) or f(x, y+2 ,p+1) or f(x, y*2 ,p+1)
#   else: return f(x+2, y ,p+1) and f(x*2,y ,p+1) and f(x, y+2 ,p+1) or f(x, y*2 ,p+1)
#
# def f1(x,y,p):
#   if x + y >= 75 and p == 3:
#     return True
#   else:
#     if x+y < 75 and p == 3:
#       return False
#     else:
#       if x+y >= 75:
#           return False
#   if p%2 == 1:
#       return f(x+2, y ,p+1) or f(x*2,y ,p+1) or f(x, y+2 ,p+1) or f(x, y*2 ,p+1)
#   else: return f(x+2, y ,p+1) and f(x*2,y ,p+1) and f(x, y+2 ,p+1) or f(x, y*2 ,p+1)
#
# for i in range(1,69):
#   if f(5 , i,1):
#     print(i)
# print("==========")
# for i in range(1,69):
#   if f1(5 ,i,1):
#     print(i)

# from itertools import permutations
# count = 0
# def f(x):
#     f = 1
#     for i in range(len(x) - 1):
#         if x[i] == x[i+1]:
#             return 0
#         else: f*=1
#     return 1
# for x in permutations('tiktok',6):
#     w = ''.join(x)
#     if f(w) == 1:
#         print(w)
#         count+=1
# print(count)

# s = '1'*13 + '2'*13 + '3'*13
# while '11' in s:
#     s = s.replace('11' , '2' , 1)
#     s = s.replace('22' , '3' ,1)
#     s = s.replace('33' , '1' , 1)
#     print(s)
# print(s)

# def f(n):
#     if n == 1:
#         return 1
#     else:
#         if n>= 2 and n%2==0: return f(n/2) + 1
#         else: return f(n-1)+n
#
# count = 0
# for i in range(1 , 100000):
#     if f(i) == 16:
#         count+=1
# print(count)

# f = open('17-3.txt')
# a = [int(i) for i in f]
# s = []
# count = 0
# for i in range(len(a) - 2):
#     if (a[i]%12 == 0 or a[i+1]%12 == 0 or a[i+2]%12==0) and a[i]%3 == 0 and a[i+1]%3 == 0 and a[i+2]%3 == 0:
#         count += 1
#         s.append((a[i]+a[i+1]+a[i+2])/3)
# print(count, min(s))

# for i in range(10000, 100000):
#   x = i
#   a = 0; b = 0
#   while x > 0:
#     y = x % 10
#     if y > 4: a = a + 1
#     if y < 6: b = b + 1
#     x = x // 10
#   if a  == 3 and b == 4:
#     print(i)
#     break

# def kolpr( a, b ):
#     if a == b:
#         return 1
#     if a > b :
#         return 0
#     if a < b:
#         return kolpr(a+2,b)+ kolpr(a*2,b)
# print(kolpr(2 , 40))

# def div(x):
#   d = set()
#   for i in range(2 , int(x**0.5)+1):
#     if x%i == 0:
#       d.add(i )
#       d.add(x//i)
#   return sorted(d)
#
# for x in range(834567, 1143210):
#   d = div(x)
#   f = 1
#   for i in range(len(d)-1):
#         if int(d[i+1]) - int(d[i]) == 2:f *= 1
#         else:f*=0
#   if f and len(d)>1 :
#     print(x, max(d))

f = open('24-153.txt')
a = [str(i) for i in f.split()]
print(a)
# for x in range(len(a)):




