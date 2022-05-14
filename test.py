# dict = {"I":1 , "V":5 ,"X":10 ,"L":50 , "C":100 , "D":500 , "M":1000}
#
# def romanToInt(string, temp):
#     string_n = list(string)
#     for key , value in dict.items():
#         if key in string_n:
#             temp += value
#     return temp
# print(romanToInt("MCMXCIV" , 0))

# def longestCommonPrefix(self, strs):
#     res = ''
#     elem1 = strs[0]
#     elem2 = strs[1]
#     elem3 = strs[2]
#     for i in range(max(len(elem1), len(elem2), len(elem3))):
#         if elem1[i] == elem2[i] == elem3[i]:
#             res += elem1[i]
#         else:
#             break
#     return res
# def binary_search(lys, val):
#     first = 0
#     last = len(lys)-1
#     index = -1
#     while (first <= last) and (index == -1):
#         mid = (first+last)//2
#         if lys[mid] == val:
#             index = mid
#         else:
#             if val<lys[mid]:
#                 last = mid -1
#             else:
#                 first = mid +1
#     return index
#
# def sort_mas(list , target):
#     a = []
#     temp = []
#     for i in range(len(sorted(list))):
#         ost = target - list[i]
#         if ost in list:
#             index = binary_search(list,ost)
#             a.append([list[i], list[index]])
#         elif ost not in list:
#             pass
#
# n , target = map(int , input().split())
# list = [int(i) for i in input().split()]
# print(sort_mas(sorted(list), target))
#
# print(sort_mas([-6 ,-5 , 0 , 2 , 3 , 5] , 18))
# print(sort_mas([0, 1, 2, 3, 4, 5, 6, 7, 8, 9] , 17))

#
# def removeElement(nums , val):
#     for i in range(len(nums)):
#         if nums[i] == val:
#             nums.pop(i)
#     return nums
# print(removeElement([3,2,2,3] , 3))


nums = [0,0,1,1,1,2,2,3,3,4]
a = set(nums)
print(list(a))