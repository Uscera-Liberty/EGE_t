# for i in range(1,1000):
#     d = i
#     n = 8
#     s = 78
#     while s <= 1200:
#       s = s + d
#       n = n + 2
#     if n == 46:
#         print(i)
# s = '5' + 152 * '6' + '5'
#
# while '63' in s or '664' in  s or '6665' in s:
#     if '63' in s: s = s.replace('63' , '4' , 1)
#     else:
#         if '664' in s: s = s.replace('664' , '65' , 1)
#         else:
#             if '6665' in s: s = s.replace('6665' , '663' , 1)
#
# print(s)
# s = ''
# def troik(x):
#     s = ""
#     while x:
#         s += str(x%3)
#         x//=3
#     return s
#
# print(str(troik(4**3*3**19)).count('0'))

# def F(n):
#   print("*")
#   if n > 0:
#     print("*")
#     G(n - 1)
# def G(n):
#   print("*")
#   if n > 1:
#     print("*")
#     F(n - 2)
#
# print(F(12))

# for i in range(130, 1000):
#     n = bin(i)[2:]
#     n1 = '0' * (8 - len(n)) + n
#     new = n1[:2] + n1[6:]
#
#     if int(new , 2) == 10:
#         print(i)

#
# def troik(x):
#     s = ""
#     while x:
#         s += str(x%5)
#         x//=5
#     return s[::-1]
#
# def pryt(x):
#     s = ""
#     while x:
#         s += str(x%9)
#         x//=9
#     return s[::-1]
#
# def vosyt(x):
#     s = ""
#     while x:
#         s += str(x%8)
#         x//=8
#     return s[::-1]
#
# s = []
# with open('17-4.txt') as f :
#     a = [int(i) for i in f]
#     for x in a:
#         if troik(x)[-1] == '3' and pryt(x)[-1] == '5' and vosyt(x)[-1] != '3':
#             s.append(x)
# print(len(s))
# print(max(s))
#
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
#     if a == 5 and b == 5:
#         print(i)

# def f(n, k):
#     if n > k or n == 43: return 0
#     if n == k: return 1
#     return f(n + 2, k) + f(n + n - 1, k) + f(n + n + 1, k)
#
#
# print(f(7, 63))


# f = open('24-j5.txt', 'r')
# s = f.read()
# k = 0
# for i in range(len(s)-4):
#   if s[i:i+4] == "KTOS":
#     k += 1
# print(k)

# def isPrime(n):
#     if n % 2 == 0:
#         return n == 2
#     d = 3
#     while d * d <= n and n % d != 0:
#        d += 2
#     return d * d > n
# c = 0
# for i in range(5408238, 5408389):
#     if isPrime(i) == True:
#         print(i , c)
#     c+=1

# f = open('26-55.txt')
# n = list(map(int, f.readline().split()))
# a = list(map(int, f.read().split()))
# m = int(input())
# for i in range(m):
#     k , n = map(int , input().split())
#     print(k+n)
# # list = [str(i) for i in range(0 , k)]
# # s = ''.join(list)
# # from itertools import product
# # c = 0
# # for x in product(s, repeat=n):
# #     if sum(map(int , x)) == n:
# #         print(x)
# #         c+=1
# # print(c)

# n=int(input())
# r=[]
# for _ in range(n):
#     (a,b)=tuple(map(int,input().split(' ')))
#     r.append(a+b)
# for z in r:
#     print(z)


def binary_searchiter(arr, n):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < n:
            low = mid + 1
        elif arr[mid] > n:
            high = mid - 1
        else:
            return mid
    return -1

def sort_mas(list , target):
    for i in range(len(list)):
        ost = target - list[i]
        if ost in list:
            index = binary_searchiter(list,ost)
            return  [list[i], list[index]]
        else:
            return []

print(sort_mas([-6 ,-5 , 0 , 2 , 4 ,4 , 3 , 5] , 8))
print(sort_mas([-6 ,-5 , 0 , 2 , 3 , 5] , 18))
print(sort_mas([0, 1, 2, 3, 4, 5, 6, 7, 8, 9] , 17))

















