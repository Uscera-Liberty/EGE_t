# def swap(res, n):
#     for i in range(len(res) - 1):
#         if res[i+1] == n:
#             res[i+1] = res[i]
#             res[i] = n
#     return res
#
# def champion_rank(pilot, events):
#     a = [str(i) for i in events.split(' ')]
#     res = [int(i) for i in range(30)]
#     for i in range(len(a) - 1):
#         if a[i] == 'I' or a[i] == 'O':
#             continue
#         if a[i+1] == 'I':
#             res.remove(int(a[i]))
#         if a[i+1] == 'O':
#             swap(res, int(a[i]))
#     if pilot in res:
#         return res.index(pilot)
#     else:
#         return -1

# test.assert_equals(champion_rank(3, ""), 3)
# test.assert_equals(champion_rank(12, "4 O 3 O"), 12)
# test.assert_equals(champion_rank(10, "1 I 10 O 2 I"), 7)

# def gcd(num1, num2):
#     if num1 == 0:
#         return (num2, 0, 1)
#     else:
#         div, x, y = gcd(num2 % num1, num1)
#     return div
#
#
# def proper_fractions(n):
#     c = 0
#     for i in range(1 , n+1):
#         if gcd(i , n) == 1:
#             c+=1
#     return c

print("Введите одно слово:")
word = input()
word_v1 = ''
for i in word:
    word_v1 = word_v1 + i + ' '
word_v1 = word_v1[:-1]
print(" " * (len(word) - 1) + word_v1[::-1])
for i in range(1, len(word)-1):
    a = " " * (len(word) - i - 1)
    b = word[-i-1] + " " * (len(word) * 2 - 3) + word[i]
    c = " " * (i-1) + word[i]
    print(a + b + c)
print(word_v1 + " " * (len(word) - 2) + word[-1])
for i in range(1, len(word)-1):
    a = word[i] + " " * (len(word) * 2 - 3) + word[-i-1]
    b = " " * (len(word)-2-i) + word[-i-1]
    print(a + b)
print(word_v1[::-1])