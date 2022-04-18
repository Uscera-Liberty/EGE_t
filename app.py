# import random
#
# number = int(input())
# start = int(input())
# finish = int(input())
#
# for _ in range(number):
#     print(random.randint(start, finish))
#

# def smaller(arr):
#     c = 0
#     spis = []
#     for i in range(len(arr)):
#         n_f = arr[i]
#         for j in reversed(range(len(arr))):
#             if n_f > arr[j]:
#                 c+=1
#             elif i == len(arr)-j:
#                 break
#
#         spis.append(c)
#         c = 0
#     return spis
# #test.assert_equals(smaller([5, 4, 7, 9, 2, 4, 4, 5, 6]), [4, 1, 5, 5, 0, 0, 0, 0, 0])
#
# print(smaller([5, 4, 7, 9, 2, 4, 4, 5, 6]))
#
# return [len([a for a in arr[i:] if a < arr[i]]) for i in range(0, len(arr))]
# def divisible_by_three(st):
#     while len(st) != 1:
#         st = str(sum(int(n) for n in st))
#     return int(st) in [0, 3, 6, 9]
#
# print(divisible_by_three(19254))

def remove_smallest(numbers):
    raise NotImplementedError("TODO: remove_smallest")

    numbers_copy = numbers[:]
    minimum = min(numbers_copy)
    numbers_copy.remove(minimum)
    return numbers_copy
