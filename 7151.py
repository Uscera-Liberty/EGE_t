
# for k in range(1,256):
#     N = k
#     s = "{:08b}".format(N)
#     p = s.rfind('1')
#     sR = s[p:]
#     for i in range(p - 1, -1, -1):
#         sR = ('1' if s[i] == '0' else '0') + sR
#     if int(sR , 2) == 11:
#         print(k)

# for i in range(1,1000):
#     s = i
#     n = 1
#     while s < 51:
#         s = s + 5
#         n = n * 2
#     if n == 64:
#         print(i)

# s = 7**2 + 49**4 - 21
# x = ''
# while s:
#     if s%14 == 10:
#         x = 'A' + x
#     elif s%14 == 11:
#         x = 'B' + x
#     elif s%14 == 12:
#         x = 'C' + x
#     elif s%14 == 13:
#         x = 'd' + x
#     else:
#         x = str(s%14) + x
#     s//=14
# print(x.count("0"))
# print(x.count('A'))

# def f(n):
#     if n < 5:
#         return 1 + 2*n
#     elif n >= 5 and n%3 == 0:
#         return 2*(n+1) * f(n-2)
#     elif n >= 5 and n%3 != 0:
#         return 2*n + 1 + f(n-1) + 2 * f(n - 2)
# print(f(15))
