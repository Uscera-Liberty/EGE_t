# temp = 0
# for i in range(1,1000):
#     n = bin(i)[2:]
#     n += str(n.count('1')%2)
#     n += str(n.count('1') % 2)
#     if int(n,2) < 50:
#         temp = int(n,2)
# print(temp)

# s = 33
# n = 1
# while s > 0:
#   s = s - 7
#   n = n * 3
# print(n)

#
# s = 282 * '6'
#
# while '222' in s or '6666' in s:
#     if '222' in s:
#         s = s.replace('222' , '6' , 1)
#     else:
#         s = s.replace('6666' , '2' , 1)
# print(s)

# for  a in range(1,1000):
#     f = 1
#     for x in range(1,1000):
#         f *= (( (x & 13 != 0) or (x & a == 0)) <= (x & 13 != 0)) or (x & a != 0) or (x & 39 == 0)
#     if f:
#         print(a)
#         break

# def F(n):
#   print(n)
#   if n < 5:
#     F(n + 1)
#     F(n + 3)
# print(F(1))

# with open('17-1.txt') as f:
#     a = [int(i) for i in f]
#     sr_ch = sum(a)/len(a)
#     c = 0
#     max_sum = []
#     for i in range(len(a)-2):
#         if ((a[i] < sr_ch and a[i+1] < sr_ch) or (a[i] < sr_ch and  a[i+2] < sr_ch) or (a[i+1] < sr_ch and a[i+2] < sr_ch)) and ((str(a[i])[-2:] == '14' or str(a[i+1])[-2:] == '14'or str(a[i+2])[-2:] == '14')):
#             c+=1
#             max_sum.append(a[i]+a[i+1]+a[i+2])
# print(c)
# print(max(max_sum))

# def f(x,y,p):
#     if x + y >= 61 and p == 3:
#         return True
#     else:
#         if x + y < 61 and p == 3:
#             return False
#     return f(x+1,y, p+1) or f(x*2,y, p+1) or f(x,y+1, p+1) or f(x,y*2, p+1)
#
# for i in range(1,53):
#     if f(7,i,1):
#         print(i)



# def f(x , y ,p):
#   if x + y >= 61 and p == 4:
#     return True
#   else:
#     if x + y < 61 and p == 4:
#       return False
#     else:
#       if x + y >= 61:
#         return False
#   if p % 2 == 1:
#     return f(x + 1, y, p + 1) or f(x * 2, y, p + 1) or f(x, y + 1, p + 1) or f(x, y * 2, p + 1)
#   else:
#     return f(x+1,y, p+1) and f(x*2,y, p+1) and f(x,y+1, p+1) and f(x,y*2, p+1)
#
# for i in range(1,53):
#   if f(7,i,1):
#     print(i)

#211111

# L = [20]
# for k in range(6):
#   n = len(L)
#   for i in range(n):
#     L.append(L[0]+1)
#     L.append(L[0]+2)
#     L.append(L[0]*2)
#     L.remove(L[0])
# print(len(set(L)))

# for i in range(1,1000):
#   x = i
#   L = 0
#   M = 0
#   while x > 0 :
#     L = L+1
#     if M < (x % 10):
#       M = x % 10
#     x = x // 10
#   if L == 3 and M == 7:
#     print(i)


# def f(x , y ,p):
#   if x + y >= 61 and (p == 3 or p == 5):
#     return True
#   else:
#     if x + y < 61 and p == 5:
#       return False
#     else:
#       if x + y >= 61:
#         return False
#   if p % 2 == 0:
#     return f(x + 1, y, p + 1) or f(x * 2, y, p + 1) or f(x, y + 1, p + 1) or f(x, y * 2, p + 1)
#   else:
#     return f(x+1,y, p+1) and f(x*2,y, p+1) and f(x,y+1, p+1) and f(x,y*2, p+1)
#
# def f1(x , y ,p):
#   if x + y >= 61 and p == 3 :
#     return True
#   else:
#     if x + y < 61 and p == 3:
#       return False
#     else:
#       if x + y >= 61:
#         return False
#   if p % 2 == 0:
#     return f(x + 1, y, p + 1) or f(x * 2, y, p + 1) or f(x, y + 1, p + 1) or f(x, y * 2, p + 1)
#   else:
#     return f(x+1,y, p+1) and f(x*2,y, p+1) and f(x,y+1, p+1) and f(x,y*2, p+1)
#
# for i in range(1,65):
#   if f(7 , i,1):
#     print(i)
# print("==========")
# for i in range(1,65):
#   if f1(7 , i,1):
#     print(i)

# with open('24-178.txt') as f :
#   a = [str(i) for i in f]
#   for i in range():


# num = 650000
# cnt = 4
# while cnt:
#   tmp = 0
#   num += 1
#   if num % 2 == 0:
#     tmp = num // 2 - 2
#     d1 = 2
#
#     #######
#     # print(num)
#     # print(2, num//2)
#     # print((num//2-2)/13)
#     #######
#
#   else:
#     for i in range(3, int(num ** 0.5) + 1, 2):
#       if num % i == 0:
#         tmp = num // i - i
#         d1 = i
#
#         #######
#         # print(num)
#         # print(i, num//i)
#         # print((num//i-i)/13)
#         #######
#
#         break
#   if tmp and tmp % 37 == 23:
#     print(num, tmp)
#     # print(num, '->', d1, '*', num//d1)
#     cnt -= 1
#
#   #######
#   # print()
#   #######


# with open('24-178.txt') as f:
#   temp = ''
#   count = 0
#   con = f.readline()
#   string = con + con
#   x = string[0]
#   for i in range(0,len(string)):
#     if ord(x) <= ord(string[i]):
#       temp += string[i]
#       print(temp)
#       if count < len(temp):
#         count = len(temp)
#     else:
#       temp = string[i]
#
#     x = string[i]
#
# print(count)