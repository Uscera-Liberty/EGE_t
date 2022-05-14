# for i in range(1,1000):
#     n = str(bin(i)[2:])
#     n1 = n + str((n.count('1')) % 2)
#     n2 = n1 + str((n1.count('1')) % 2)
#
#     if int(n2 , 2) > 125 :
#         print(i)

# for i in range(1,1000):
#     s = i
#     n = 0
#     while s < s * s:
#         s = s - 1
#         n = n + 3
#     if n > 2000:
#         print(i)
#         break
# s = 15 * '3' +10*'2' + 10 * '4' + 10 * '2'
# while '42' in s or '32' in s:
#     if '42' in s:
#         s = s.replace('42' , '61' , 1)
#     else:
#         s = s.replace('32' , '61' , 1)
# print(sum([int(i) for i in s]))


# for a in range(1,1000):
#     f = 1
#     for x in range(1,1000):
#         f *= (a%12 == 0) and (530%x == 0) <= ((not(a%x==0)) <= (not(170%x==0)))
#     if f:
#         print(a)
#         break

# def f(n):
#     if n > 16:
#         return n - 3
#     elif n <= 16:
#         return 2 * f(n+1) + 2*n + 3
# print(f(2))

# with open('17-6.txt') as f:
#     a = [int(i) for i in f]
#     c = 0
#     s = []
#     for n in range(len(a) - 2):
#         if bin(a[n]).count('1') == 3 and bin(a[n+1]).count('1') == 3 and bin(a[n+2]).count('1') == 3:
#             c+=1
#             s.append(max(a[n] , a[n+1] , a[n+2]))
# print(sum(s) , c)
#
# def f(x , y , p):
#     if x+y >= 62 and p==3:
#         return True
#     elif x+y < 62 and p == 3:
#         return False
#     return f(x+1 , y, p+1) or f(x+y , y , p+1) or f(x, y+1, p+1) or f(x , y+x , p+1)
#
# for i in range(1 , 62):
#     if f(8 , i , 1):
#         print(i)
#         break
# print("++++")
#
#
# def f(x , y , p):
#     if x+y >= 62 and p==3:
#         return True
#     else:
#         if x+y < 62 and p == 3:
#             return False
#         elif x+ y >= 62:
#             return False
#     if p%2 == 1:
#         return f(x+1 , y, p+1) or f(x+y , y , p+1) or f(x, y+1, p+1) or f(x , y+x , p+1)
#     else:
#         return f(x + 1, y, p + 1) and f(x + y, y, p + 1) and f(x, y + 1, p + 1) and f(x, y + x, p + 1)
#
# for i in range(1,62):
#     if f(8 , i , 1):
#         print(i)
#
# print("+++++")
#
# def f(x , y , p):
#     if x+y >= 62 and (p==3 or p==5):
#         return True
#     else:
#         if x+y < 62 and p == 5:
#             return False
#         elif x + y >= 62:
#             return False
#     if p%2 == 0:
#         return f(x+1 , y, p+1) or f(x+y , y , p+1) or f(x, y+1, p+1) or f(x , y+x , p+1)
#     else:
#         return f(x + 1, y, p + 1) and f(x + y, y, p + 1) and f(x, y + 1, p + 1) and f(x, y + x, p + 1)
#
#
# def f1(x, y, p):
#     if x + y >= 62 and p == 3:
#         return True
#     else:
#         if x + y < 62 and p == 3:
#             return False
#         elif x + y >= 62:
#             return False
#     if p % 2 == 0:
#         return f(x + 1, y, p + 1) or f(x + y, y, p + 1) or f(x, y + 1, p + 1) or f(x, y + x, p + 1)
#     else:
#         return f(x + 1, y, p + 1) and f(x + y, y, p + 1) and f(x, y + 1, p + 1) and f(x, y + x, p + 1)
#
# for i in range(1,62):
#     if f(8,i,1):
#         print(i)
#
# print("++++++")
#
# for i in range(1,62):
#     if f1(8,i,1):
#         print(i)
# for i in range(1 ,2000):
#     for n in range(1,2000):
#         x = i
#         y = n
#         a = 0
#         b = 0
#         while x * y > 0:
#           if x > 0:
#             a = a + 1
#           if y > 0 and y%7 > b:
#             b = y % 7
#           x = x // 10
#           y = y // 7
#         if a == 4 and b == 5:
#             print(i*n)
# count = 0
# l = []
# for j in range(118811, 118972):
#   a = j
#   for i in range(2 , a//2+1):
#     if (a%i == 0):
#       count += 1
#       l.append(i)
#   if count == 4:
#     print(l[-1] , l[-2])
#     l = []
#   count = 0
#   l = []

#
# from itertools import permutations
# f = open('27-40b.txt')
# n = int(f.readline())
#
# def get():
#     a = list(map(int , f.readline().split()))
#     return list(permutations(a))
#
# s = get()
#
# for _ in range(n-1):
#     pare =get()
#     # в кмб храним суммы всех чисел со всеми комбинациями
#     cmb = [ sorted([a[0]+b[0] ,a[1]+b[1] , a[2]+b[2]]) for a in s for b in pare]
#     # сюда будем добавлять новые комбинации подходящие нам с суммами
#     s1 = [[0,0,0]] * 3
#     for x in cmb:
#         # здесь мы проводим сортировку ибо записываем в каждый подмассив кмб ту комбинацию где остатки от суммы равны ее положениям
#         # к примеру нулевое положение будет занимать комбнация где у первое и второе число четно и тд
#         i = x[0]%2 + x[1]%2
#         # и если в третьей группе нашлось число большее то следовательно мы его туда
#         # и записываем в нужную комбинацию с нужной позицией
#         if x[2] > s1[i][2]: s1[i] = x
#     s = [x for x in s1 if x[2] != 0]
# # поэтому здесь мы пишем что мы ищем подкомбинацию с индексом 1 (то есть одно число из двух групп нечетное а другое четное)
# # и мы ищем в этой подкомбинации третье число
# # print(s[1][2])
# def isPrime(n):
#     if n % 2 == 0:
#         return n == 2
#     d = 3
#     while d * d <= n and n % d != 0:
#        d += 2
#     return d * d > n
#
# def is_palidrom(in_str):
#     arr_len =len(in_str)
#     for index in range(arr_len // 2):
#         if in_str[index] != in_str[- 1 - index]:
#             return False
#     return True
# #
# def simple(c):
#     for x in range(2,round(c**0.5)+1):
#         if c%x == 0:
#             return False
#     return True
#
# def summ(c):
#     p = str(c)
#     s = 1
#     for x in p:
#         if x != "0":
#             s *= int(x)
#     return(s)
#
# poli = []
# plpoli = []
# for i in range(100,1000000000+1):
#     s = str(i)
#     if len(s)%2 == 1 and ((s[0] == "1" and s[len(s)-1] == "1") or (s[0] == "3" and s[len(s)-1] == "3") or (s[0] == "7" and s[len(s)-1] == "7") or (s[0] == "9" and s[len(s)-1] == "9")):
#         for x in range(len(s)//2):
#             if s[x] == s[len(s)-x-1]:
#                 pol = True
#             else:
#                 pol = False
#                 break
#         if pol == True:
#             if simple(i):
#                 print(i,summ(i))
#                 poli.append(i)
#                 plpoli.append(summ(i))
#
# for i in range(3):
#     print("--------------------")
#
# print(max(plpoli))
#
# max_count = 0
# max_plpoli = 0
# for x in plpoli:
#     if plpoli.count(x) > max_count:
#         max_count = plpoli.count(x)
#         max_plpoli = x
#
# res = []
# for r in range(max_count):
#     ind = plpoli.index(max_plpoli)
#     plpoli[ind] = 0
#     res.append(poli[ind])
#
# for b in range(5):
#     print(max(res))
#     res.remove(max(res))

# def searchInsert(nums, target):
#     pos = 0
#     if target in nums:
#         return nums.index(target)
#     elif nums[-1] < target:
#         return len(nums)
#     else:
#         mid = (len(nums) // 2) - 1
#         if nums[mid] > target:
#             nums = nums[:mid]
#         else:
#             nums = nums[mid:]
#             pos += mid
#     for i in range(len(nums)):
#         if nums[i] < target:
#             pos += 1
#     return pos
#
#
# print(searchInsert(nums = [1], target = 2))

s = str(input())
leftSymbols = []
for c in s:
# If left symbol is encountered
    if c in ['(', '{', '[']:
        leftSymbols.append(c)
    # If right symbol is encountered
    elif c == ')' and len(leftSymbols) != 0 and leftSymbols[-1] == '(':
        leftSymbols.pop()
    elif c == '}' and len(leftSymbols) != 0 and leftSymbols[-1] == '{':
        leftSymbols.pop()
    elif c == ']' and len(leftSymbols) != 0 and leftSymbols[-1] == '[':
        leftSymbols.pop()
    # If none of the valid symbols is encountered
    else:
        print("NOT")
if len(leftSymbols) == 0:
    print("YES")
