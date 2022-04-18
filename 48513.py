# for i in range(1,1000):
#     n = i
#     if n%2 == 0 :
#         n = n/2
#     else:
#         n = n-1
#     if n%5 == 0:
#         n = n/5
#     else:
#         n = n-1
#     if n%7 == 0:
#         n = n/7
#     else:
#         n = n-1
#     if n == 6:
#         print(i)

# for i in range(1,1000):
#     s = i
#     n = 2
#     while s < 64:
#         s = s + 8
#         n = n * 2
#     if n == 256:
#         print(i)

# from itertools import permutations
# c = 0
# for  x in permutations('nigrol'):
#     w = ''.join(x)
#     if w.find('oig') == -1 and w[0] != 'o':
#         c+=1
# print(c)

# s = '6' * 166
# while '2222' in s or '666' in s :
#     if '2222' in s :
#         s = s.replace('2222' , '6' , 1)
#     else:
#         s = s.replace('666' ,'2' , 1)
# print(s)

# s = 7 * 1296**57 - 8*216**30 + 35
# x = ''
# while s:
#     x = str(s%6) + x
#     s//=6
# print(x.count('5'))

# for a in range(1,1000):
#     f = 1
#     for x in range(1,100):
#         for y in range(1,100):
#             f *= (-5*y + 3*x < a) or (x > 15) or (y > 30)
#         if f == 0:
#             break
#     if f:
#         print(a)
#         break

# def F(n):
#   if n < 10:
#     return n
#   else:
#     m = F(n//10)
#     d = m%10
#     if m < d:
#       return d
#     else:
#       return m
# temp = 0
# for n in range(100,1001):
#     if F(n) > 7:
#         temp = n
# print(temp , F(temp))

# with open('17-1.txt') as f:
#     c = 0
#     s = []
#     a = [int(i) for i in f]
#     sred_zn = sum(a)/len(a)
#     for i in range(len(a) - 1):
#         if (a[i] > sred_zn or a[i+1] > sred_zn) and (a[i]%17 == 0 or a[i+1]%17 == 0):
#             s.append(a[i] + a[i+1])
#             c+=1
# print(max(s))
# print(c)

# for i in range(200,1000):
#     x = i
#     L = 2 * x - 30
#     M = 2 * x + 40
#     while L != M:
#         if L > M:
#             L = L - M
#         else:
#             M = M - L
#     if M == 70:
#         print(i)
#         break

# def kolpr(a, b):
#   if a == b:
#     return 1
#   if a > b:
#     return 0
#   return kolpr(a + 1, b) + kolpr(a * 2, b)
#
#
# print(kolpr(1,16))


# with open('24-4.txt', ) as f:
#     text = f.read()
#     maxx = ''
#     temp = text[0]
#     c = 0
#     for i in range(1, len(text)):
#         if ord(text[i]) < ord(text[i - 1]):
#             temp += text[i]
#             if len(temp) > len(maxx):
#                 maxx = temp
#                 c = i
#         else:
#             temp = text[i]
#
#     print(maxx)
#     print(c)
#
# a = []
# for i in range(2, 37000):
#     k = True
#     for j in range(2, i // 2 + 1):
#         if i % j == 0:
#             k = False
#             break
#     if k == True:
#         a.append(i)
#
# count = 0
# maximum = 0
# for i in range(236228 , 305283):
#     k = []
#     n = 1
#     for elem in a:  # берем каждый элемент из массива простых чисел("а")
#         if i % elem == 0:
#             k.append(elem)
#             n = n * elem
#             if len(k) > 3:
#                 break
#         if len(k) == 3:
#             if n == i:
#                 count += 1
#                 if i > maximum:
#                     maximum += i
#             break
# print(count, maximum/len(str(maximum)))

with open('27-56a.txt') as f:
    n = int(f.readline())
    text = f.read()
    a1 = text * 2
    a1 = [int(i) for i in a1]
    max = 0
    i = 0
    s = set()
    print(a1)
    for i in range(len(a1)):
        if sum(a1[i:4+i])%6 == 0 and max < sum(a1[i:4+i]):
            s.add(sum(a1[i:4+i]))
    print(s)