#a = [int(x) for x in open('17-10.txt')]
#
# def f(x):
#     x7 = ''
#     while x:
#         s = x % 7
#         x7 = str(s) + x7
#         x //= 7
#     return x7
#
#
# def p(s):
#     if len(s) > 1:
#         rev = s[::-1]
#         if (s == rev):
#             return True
#     return False
#
#
# ma = 0
# count = 0
# for i in range(1, len(a)):
#     pal = f(a[i - 1] + a[i])
#     if p(pal):
#         count += 1
#         ma = max(ma, int(pal))
# print(count, ma)


# def f(x,y,p):
#     if x + y >= 87 and p == 3:
#         return True
#     else:
#         if x + y < 87 and p == 3:
#             return False
#     return f(x+1,y, p+1) or f(x*2,y, p+1) or f(x,y+1, p+1) or f(x,y*2, p+1)
#
# for i in range(1,53):
#     if f(9,i,1):
#         print(i)


# def f(x,y,p):
#     if x + y >= 87 and p == 4:
#         return True
#     else:
#         if x + y < 87 and p == 4:
#             return False
#         else:
#             if x + y >= 87:
#                 return False
#     if p%2 == 1:
#         return f(x+1,y, p+1) or f(x*2,y, p+1) or f(x,y+1, p+1) or f(x,y*2, p+1)
#     else:
#         return f(x + 1, y, p + 1) and f(x * 2, y, p + 1) and f(x, y + 1, p + 1) and f(x, y * 2, p + 1)
#
# for i in range(1,77):
#     if f(9,i,1):
#         print(i)
#
# def f(x,y,p):
#     if x + y >= 87 and (p == 3 or p == 5):
#         return True
#     else:
#         if x + y < 87 and p == 5:
#             return False
#         else:
#             if x + y >= 87:
#                 return False
#     if p%2 == 0:
#         return f(x+1,y, p+1) or f(x*2,y, p+1) or f(x,y+1, p+1) or f(x,y*2, p+1)
#     else:
#         return f(x + 1, y, p + 1) and f(x * 2, y, p + 1) and f(x, y + 1, p + 1) and f(x, y * 2, p + 1)
#
# def f1(x,y,p):
#     if x + y >= 87 and p == 3:
#         return True
#     else:
#         if x + y < 87 and p == 3:
#             return False
#         else:
#             if x + y >= 87:
#                 return False
#     if p%2 == 0:
#         return f(x+1,y, p+1) or f(x*2,y, p+1) or f(x,y+1, p+1) or f(x,y*2, p+1)
#     else:
#         return f(x + 1, y, p + 1) and f(x * 2, y, p + 1) and f(x, y + 1, p + 1) and f(x, y * 2, p + 1)
#
# for i in range(1,77):
#     if f(9,i,1):
#         print(i)
#
# print("++++++")
#
# for i in range(1,77):
#     if f1(9,i,1):
#         print(i)
#

# def count_of_divs(x):
#     k = 0
#     for i in range(1, x + 1):
#         if x % i == 0:
#             k += 1
#     return k
#
#
# def get_all_divs(x):
#     res = []
#     for i in range(1, x + 1):
#         if x % i == 0:
#             res.append(i)
#     res.sort(reverse=1)
#     return res
#
#
# k = 1
# for x in range(248015,251575+1,2):
#     kk = count_of_divs(x)
#     if kk % 2 != 0:
#         print(x, kk, int(x ** 0.5))
#         k += 1

