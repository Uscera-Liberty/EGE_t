# N = 193
# s = "{:08b}".format(N)
# p = s.rfind('1')
# sR = s[p:]
# for i in range(p - 1, -1, -1):
#     sR = ('1' if s[i] == '0' else '0') + sR
# print(int(sR, 2))
# for i in range(1,1000):
#   s = i
#   n = 11
#   while s > -9:
#     s = s - 4
#     n = n + 5
#   if n == 56:print(i)

# from itertools import permutations
# c = 0
# for x in permutations('123456789ABCDEF',3):
#   w = ''.join(x)
#   c+=1
#   for i in range(0,3):
#     if (w[i]%2 == 1 and w[i+1]%2 == 1) and (w[i]%2 == 0 and w[i+1]%2 == 0):
#       c-=1
# print(c)
# s = 28*'1' + 34*'2'+ 45*'3'
# for i in range(1,100):
#     for j in range(1,100):
#         for l in range(1,100):
#             x = '0' + i * '1' + j*'2'+l*'3'
#             while '01' in x or '02' in x or '03' in x:
#                 x = x.replace('01','302',1)
#                 x = x.replace('02','3103',1)
#                 x = x.replace('03','20',1)
#             if x == s:
#                 print(i)

# x = (66+6**2019)*6**2019+66+6**6
# sum1 = 0
# while x:
#     sum1 = x%6 + sum1
#     x//=6
# print(sum1)

# def f(n):
#     if n < 2:
#         return 1
#     if n>=2 and n%3==0:
#         return f(n/3) - 1
#     if n>=2 and n%3!=0:
#         return f(n-1) + 17
#
# for n in range(10000,600000):
#     if f(n) == 110:
#         print(n)
#         break



# data = [int(x) for x in open('17-202.txt')]
# def cond(x):
#     return 100 <= x < 1000 and x % 10 == 5
# ma = 0
# count = 0
# for i in range(2, len(data)):
#     if (not cond(data[i - 2])) and cond(data[i - 1]) and (not cond(data[i])):
#         count += 1
#         ma = max(ma, sum(data[i - 2:i + 1]))
#
# print(count, ma)
# for i in range(1,1000):
#     x = i
#     a = 0; b = 1
#     while x > 0:
#       a = a + 1
#       b = b * (x % 8)
#       x = x // 8
#     if a == 3 and b == 10:
#         print(i)
#         break

# dp=[0]*12
# dp[2]=  1
# for i in range(2,12):
#     if i+2<12:dp[i+2]+=dp[i]
#     if i+5<12:dp[i+5]+=dp[i]
#     if i+i-1<12:dp[i+i-1]+=dp[i]
# print(dp[11])

# def solution(s):
#     for i in s:
#         if i != i.lower():
#             i += ' '
#     return s
#
# print(solution('helloWorld'))

