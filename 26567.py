# for n in range(1,1000):
#     n1 = bin(n)[2:]
#     n2 = str(n1) + n1[-1]
#     if n1.count('1')%2 == 0:
#         n3 = str(n2)+'0'
#     else:
#         n3 = str(n2) + '1'
#
#     if n3.count('1')%2 == 0:
#         n4 = str(n3) +'0'
#     else:
#         n4 = str(n3) + '1'
#     if int(n4,2) > 130:
#         print(int(n4,2))
#         break
# for i in range(1,1000):
#     n = i
#     s = 350
#     while 2*s+n < 1100:
#       s = s - 5
#       n = n + 15
#     if s == 45:
#         print(i)

# from itertools import permutations
# c = 0
# for x in permutations('vaifu',4):
#     w = ''.join(x)
#     if w[0] != 'i' and w.find('vf') == -1 and w.find('fv') == -1:
#         print(w)
#         c+=1
# print(c)
#
# s = '1' + 51 * '2'
# while '12' in s or '1' in s:
#     if '12' in s:
#         s = s.replace('12','2221',1)
#     else:
#         s = s.replace('1','222222',1)
# print(s.count('2'))

# s = 9**5 + 3**25 - 20
# s3 = []
# while s:
#     s3.append(s%3)
#     s//=3
# print(sum(s3))

# def f(n):
#    if n <= 3:
#        return n
#    elif n % 2 == 0:
#        return n + f(n - 1)
#    else:
#        return n*n + f(n-2)
# cur = 1
# while(f(cur) < 1e8):
#    cur += 1
# print(cur - 1)

# a = [int(i) for i in open('17-9.txt')]
# c = 0
# s = []
# for i in range(len(a)-2):
#     dv1 = bin(a[i])[2:]
#     dv2 = bin(a[i+1])[2:]
#     dv3 = bin(a[i+2])[2:]
#     if ((dv1.count('1') >= 3 and dv2.count('1')>=3) and (dv1.count('0') >= 1 and dv2.count('0')>=1)) or ((dv1.count('1') >= 3 and dv3.count('1')>=3)and (dv1.count('0') >= 1 and dv3.count('0')>=1)) or((dv2.count('1') >= 3 and dv3.count('1')>=3)and (dv3.count('0') >= 1 and dv2.count('0')>=1)):
#         s.append(a[i])
#         s.append(a[i+1])
#         s.append(a[i+2])
#         c+=1
# print(max(s),c)
#
# print('++++19++++')
# def f(x,p):
#   if x >= 50 and p == 3:
#     return True
#   else:
#     if x< 50 and p == 3:
#       return False
#   return f(x+1,p+1) or f(x*2,p+1)
#
# for i in range(1,50):
#   if f(i,1):
#     print(i)
#     break
# for i in range(1,1000):
#     x = i
#     L = 0; M = 9
#     while x > 5:
#       L = L + 1
#       if M > (x % 10):
#         M = x % 10
#       x = x // 10
#     if L == 3 and M == 4:
#         print(i)

# def kolpr(a, b):
#   if b%2 == 1 or a > b:
#       return 0
#   if a == b:
#     return 1
#   return kolpr(a + 1, b) + kolpr(a * 1.5, b)
#
#
# print(kolpr(2,22))
# f = open('24-j5.txt', 'r')
# s = f.read().strip()
# m = 0
# k = 0
# i = 0
# while i < len(s)-5:
#     if s[i:i+5] == 'SOCKOS':
#         k += 1
#         if k > m:
#             m = k
#         i += 5
#     else:
#         k = 0
#         i += 1
# print(m)

# def fun():
#     for i in range(222987, 223021):
#         k = 1
#         d = 0
#         res = []
#         while k * k < i + 1:
#             if i % k == 0:
#                 if k != i // k:
#                     d += 2
#                     res.extend([k, i // k])
#                 else:
#                     d += 1
#             if d > 4:
#                 break
#             k += 1
#         if d == 4:
#             print(*sorted(res)[-2:])
#
#
# fun()

