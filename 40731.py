# for i in range(1,1000):
#     s = i
#     n = 1
#     while s < 28:
#       s = s + 5
#       n = n * 3
#     if n == 81:
#         print(i)
#
# from itertools import product
# c = 0
# for x in product('enisy' , repeat = 4):
#     w = ''.join(x)
#     if w[0] != 'y' and w.count('e') >= 1 and w.count('i') >= 1:
#         c+=1
# print(c)

# s = 146*'5'
# while '333' in s or '555' in s:
#     if '555' in s:
#         s = s.replace('555' , '3' , 1)
#     else:
#         s = s.replace('333','5' , 1)
# print(s)

# def f(n):
#     if n < 3:
#         return 2*n
#     elif n >= 3 and n%2 == 0:
#         return 3*n + 5 + f(n-2)
#     elif n >= 3 and n%2 != 0:
#         return n + 2*f(n-6)
# print(f(61))

# with open('17-4.txt') as f:
#     s = []
#     a = [int(i) for i in f]
#     for j in range(len(a)):
#         if a[j]%13 == 4 and a[j]%8 == 1:
#             s.append(a[j])
# print(max(s))
# print(sum(s))
# for i in range(1,1000):
#     x = i
#     a = 0
#     b = 1
#     while x > 0:
#       if x % 2 == 0:
#         a = a + x % 13
#       else:
#         b = b * (x % 13)
#       x = x // 13
#     if a == 5 and b == 2:
#         print(i)
#
# def kolpr( a, b ):
#     if a == b:
#         return 1
#     if a > b or a == 10:
#         return 0
#     if a < b:
#         return kolpr(a+1,b)+ kolpr(a+3,b)
# print(kolpr(3,15) * kolpr(15,20))


# f = open('24-j5.txt', 'r')
# s = f.read()
# k = 0
# for i in range(len(s)-6):
#   if s[i:i+6] == "SOCKOS":
#     k += 1
# print(k)

# for i in range(2, 30001):
#     k = 0
#     n = 0
#     for x in range(1, i):
#         if i % x == 0:
#             k += x
#     for j in range(1, k):
#         if k % j == 0:
#             n += j
#     if i == n and i != k and i == min(i, k):
#         print(i, k)
# c = 0
# a1 = []
# with open("18-0.txt") as f:
#     a = [int(i) for i in f]
#     for j in range(len(a) - 1):
#         if a[j] < a[j+1]:
#             c += 1
#         else:
#             a1.append(c)
#             c = 0
# print(max(a1))

# def f(x,p):
#     if x > 34 and p == 3:
#         return True
#     else:
#         if x < 34 and p == 3:
#             return False
#
#     return f(x+1,p+1) or f(x+2,p+1) or f(x+3,p+1) or f(x*2,p+1)
#
# for i in range(1,33):
#   if f(i,1):
#     print(i)
#     break

# f = open ('27-b.txt') # для первого ответа - 27-1a.txt
# n=int(f.readline())
# data=f.readlines()
# summa=0
# minim=10001 # для минимальной разницы
# for i in range(0, n):
#     s = data[i].split()
#     a=int(s[0])
#     b=int(s[1])
#     summa+=min(a,b) # сумма максимумов из пар
#     raznitsa = abs(a-b) # разница
#     if raznitsa % 3 != 0:
#         minim=min(minim,raznitsa)
# if summa % 3 != 0:
#     print(summa)
# else:
#     print(summa + minim) # здесь добавляем! т.к. иначе берем наибольший из пары
#
# print("+++++++++")
#
# with open('27-b.txt') as f:
#     n = int(f.readline())
#     data = f.readlines()
#     summa = 0
#     minim = 10001
#     for i in range(0 , n):
#         p = data[i].split()
#         a = int(p[0])
#         b = int(p[1])
#         summa += min(a,b)
#         raznitsa = abs(a - b)
#         if raznitsa %3 != 0:
#             minim = min(minim , raznitsa)
#     if summa %3 != 0:
#         print(summa)
#     else:
#         print(summa + minim)

#
# def pick_peaks(arr):
#     max_val = max(arr)
#     index = arr.index(max_val)
#     return {'pos': index , 'peaks': max_val}
#
# print(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,3]))
#
# import itertools
# def choose_best_sum(t, k, ls):
#     maxi = 0
#     for x in itertools.permutations(ls , k):
#         if sum(x) <= t and sum(x) >= maxi :
#             maxi = sum(x)
#     return maxi
# xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
# print(choose_best_sum(230, 4, xs))

# from functools import reduce
#
# words = ['beegeek', 'stepik', 'python', 'iq-option']
# result = reduce(lambda a, b: a if len(a) > len(b) else b, words)
# print(result)