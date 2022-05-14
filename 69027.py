# print("x y w z")
# for x in 1 ,0:
#     for y in 1 ,0:
#         for w in 1 ,0:
#             for z in 1 ,0:
#                 if ((y<=x) or ((not(z))and w)) == (w==x):
#                     print(x , y , w , z)

# for j in range(1 , 257):
#     n = j
#     n1 = bin(n)[2:]
#     n2 = '0'*(8-len(n1)) + n1
#     s = ''
#     for i in n2:
#         if i == '1':
#             s += '0'
#         else:
#             s += '1'
#     res = int(s,2)
#     print(res ,  j)
# c = 0
# for i in range(1 , 1000):
#     s = i
#     n = 1
#     while s < 54:
#       s = s + 7
#       n = n * 3
#     if n == 243:
#         c+=1
# print(c)

# from itertools import product
#
# s = map(lambda x: ''.join(x), product('0123456789ABCDEF', repeat=5))
# L = [x for x in s if x[0] != '0' and all(x[k] <= x[k + 1] for k in range(len(x) - 1))]
# print(len(L))

#
# s = 2018 * '1' + 2050*'3'
# while '111' in s:
#      s = s.replace("111" , '2' , 1)
#      s = s.replace('222' , '3' , 1)
#      s = s.replace('333' , '1' , 1)
# print(s)


# s = 8**2341 - 4**342 + 2**620 - 81
# print(bin(s).count('1'))

# for a in range(1 , 1000):
#     f = 1
#     for x in range(1 , 1000):
#         f*= (a%3 == 0) and ((220%x == 0) <= ((a%x!= 0 )<= (550%x!=0)))
#     if f:
#         print(a)
#         break

# def F(n):
#   if n>0:
#     return n%10*F(n//10)
#   else:
#     return 1
#
# for n in range(1 , 1000):
#     if F(n) > 320:
#         print(F(n) , n)
# s = []
# c = 0
# with open('17-3.txt') as f:
#     a = [int(i) for i in f]
#     for i in range(len(a) - 1):
#         if (a[i]*a[i+1])%2 == 1 and ((a[i]+a[i+1])/2) % 7 == 0:
#             s.append((a[i]+a[i+1])/2)
#             c+=1
# print(min(s),c)

# def f(x,y,p):
#     if x + y >= 49 and p == 3:
#         return True
#     else:
#         if x + y < 49 and p == 3:
#             return False
#     return f(x+1,y, p+1) or f(x*3,y, p+1) or f(x,y+1, p+1) or f(x,y*3, p+1)
#
# for i in range(1,53):
#     if f(5,i,1):
#         print(i)
#         break
#
#
# def f(x,y,p):
#     if x + y >= 49 and p == 4:
#         return True
#     else:
#         if x + y < 49 and p == 4:
#             return False
#         else:
#             if x + y >= 49:
#                 return False
#     if p%2 == 1:
#         return f(x+1,y, p+1) or f(x*3,y, p+1) or f(x,y+1, p+1) or f(x,y*3, p+1)
#     else:
#         return f(x + 1, y, p + 1) and f(x * 3, y, p + 1) and f(x, y + 1, p + 1) and f(x, y * 3, p + 1)
#
# for i in range(1,49):
#     if f(5,i,1):
#         print(i)
#
# def f(x,y,p):
#     if x + y >= 49 and (p == 3 or p == 5):
#         return True
#     else:
#         if x + y < 49 and p == 5:
#             return False
#         else:
#             if x + y >= 49:
#                 return False
#     if p%2 == 0:
#         return f(x+1,y, p+1) or f(x*3,y, p+1) or f(x,y+1, p+1) or f(x,y*3, p+1)
#     else:
#         return f(x + 1, y, p + 1) and f(x * 2, y, p + 1) and f(x, y + 1, p + 1) and f(x, y * 2, p + 1)
#
# def f1(x,y,p):
#     if x + y >= 49 and p == 3:
#         return True
#     else:
#         if x + y < 49 and p == 3:
#             return False
#         else:
#             if x + y >= 49:
#                 return False
#     if p%2 == 0:
#         return f(x+1,y, p+1) or f(x*2,y, p+1) or f(x,y+1, p+1) or f(x,y*2, p+1)
#     else:
#         return f(x + 1, y, p + 1) and f(x * 3, y, p + 1) and f(x, y + 1, p + 1) and f(x, y * 3, p + 1)
#
# for i in range(1,49):
#     if f(5,i,1):
#         print(i)
#
# print("++++++")
#
# for i in range(1,49):
#     if f1(5,i,1):
#         print(i)

# for i in range(100 , 1000):
#     x = i
#     L = x - 15
#     M = x + 20
#     while L != M:
#       if L > M:
#         L = L - M
#       else:
#         M = M - L
#     if M == 35:
#         print(i)


# def kolpr(a, b):
#   if a == b:
#     return 1
#   if a > b:
#     return 0
#   return kolpr(a + 1, b) + kolpr(a + 2, b)
#
# print(kolpr(5 ,10) + kolpr(10 ,15))

# with open('24-4.txt', 'r') as f:
#   text = f.read()
#
# maxx = ''
# temp = text[0]
# for i in range(1, len(text)):
#   if ord(text[i]) < ord(text[i - 1]):
#     temp += text[i]
#     if len(temp) > len(maxx):
#       maxx = temp
#   else:
#     temp = text[i]
#
# print(maxx)

# def f(n):
#   result = []
#   i = 1
#   while i*i <= n:
#     if n%i == 0:
#       result.append(i)
#       if n//i != i:
#         result.append(n//i)
#     i+=1
#   return result
#
# temp = 0
# ch = 0
# for n in range(394441, 394506):
#   if len(f(n)) > temp:
#     ch = n
#     temp = len(f(n))
#
# print(ch , temp)