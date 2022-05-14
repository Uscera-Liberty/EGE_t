# f = open('17-1.txt')
# a = [int(i) for i in f]
# k = 0
# t = []
# for i in range(len(a) - 1):
#     if (a[i] % 9 == 0 and a[i + 1] % 8 == 3 and a[i + 1] % 9 != 0) or (
#             a[i] % 8 == 3 and a[i + 1] % 9 == 0 and a[i] % 9 != 0):
#         k = k + 1
#         t.append(a[i])
#         t.append(a[i + 1])
# print(k, max(t))
# for i in range(100 , 1000):
#     x = i
#     L = x - 21
#     M = x + 12
#     while L != M:
#       if L > M:
#         L = L - M
#       else:
#         M = M - L
#     if M == 11:
#         print(i)
#         break
# def kolpr(a, b):
#   if a == b:
#     return 1
#   if a > b:
#     return 0
#   return kolpr(a + 1, b) + kolpr(a * 3, b)
#
# print(kolpr(1, 22)+kolpr(22,77))


# f = open('24-s1.txt', 'r')
# s = f.read().strip()
# k = 0
# i = 0
# while i < len(s)-3:
#     if s[i] == 'Z' and s[i+2] == 'R' and s[i+3] == 'O':
#         k += 1
#         i += 3
#     else:
#         i += 1
# print(k)

# def prnum(n):
#     res = {2}
#     prime = [True] * (n + 1)
#     for j in range(4, n + 1, 2):
#         prime[j] = False
#     for i in range(3, n + 1, 2):
#         if not prime[i]:
#             continue
#         res.add(i)
#         for j in range(i * i, n + 1, i):
#             prime[j] = False
#     return sorted(list(res))
#
#
# def isPrime(n):
#     d = 2
#     if n % 2:
#         d = 3
#         while d * d <= n and n % d != 0:
#             d += 2
#     return d * d > n
#
#
# if __name__ in '__main__':
#     p = int(315675 ** 0.5)
#     pr = prnum(p)
#     cnt = 0
#     max_diff = 0
#     for i in range(326359, 421986):
#         for k in pr:
#             if not i % k and isPrime(i // k):
#                 cnt += 1
#                 max_diff = max(max_diff, i // k - k)
#                 # print(k, i//k)
#     print(cnt)
#     print(max_diff)

# def f(x,y,p):
#     if x + y >= 64 and p == 3:
#         return True
#     else:
#         if x + y < 64 and p == 3:
#             return False
#     return f(x+1,y, p+1) or f(x+y,y, p+1) or f(x,y+1, p+1) or f(x,y+x, p+1)
#
# for i in range(1,64):
#     if f(6,i,1):
#         print(i)
# print('+++++')
#
# def f(x,y,p):
#     if x + y >= 64 and p == 4:
#         return True
#     else:
#         if x + y < 64 and p == 4:
#             return False
#         else:
#             if x + y >= 64:
#                 return False
#     if p%2 == 1:
#         return f(x+1,y, p+1) or f(x+y,y, p+1) or f(x,y+1, p+1) or f(x,y+x, p+1)
#     else:
#         return f(x + 1, y, p + 1) and f(x +y, y, p + 1) and f(x, y + 1, p + 1) and f(x, y +x, p + 1)
#
# for i in range(1,64):
#     if f(6,i,1):
#         print(i)
# print("+++++")
# def f(x,y,p):
#     if x + y >= 64 and (p == 3 or p == 5):
#         return True
#     else:
#         if x + y < 64 and p == 5:
#             return False
#         else:
#             if x + y >= 64:
#                 return False
#     if p%2 == 0:
#         return f(x+1,y, p+1) or f(x+y,y, p+1) or f(x,y+1, p+1) or f(x,y+x, p+1)
#     else:
#         return f(x + 1, y, p + 1) and f(x +y, y, p + 1) and f(x, y + 1, p + 1) and f(x, y +x, p + 1)
#
# def f1(x,y,p):
#     if x + y >= 64 and p == 3:
#         return True
#     else:
#         if x + y < 64 and p == 3:
#             return False
#         else:
#             if x + y >= 64:
#                 return False
#     if p%2 == 0:
#         return f(x+1,y, p+1) or f(x+y,y, p+1) or f(x,y+1, p+1) or f(x,y+x, p+1)
#     else:
#         return f(x + 1, y, p + 1) and f(x +y, y, p + 1) and f(x, y + 1, p + 1) and f(x, y +x, p + 1)
#
# for i in range(1,64):
#     if f(6,i,1):
#         print(i)
#
# print("++++++")
#
# for i in range(1,64):
#     if f1(6,i,1):
#         print(i)
#
