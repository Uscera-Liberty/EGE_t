# def primfacs(n):
#     i = 2
#     primfac = []
#     while i * i <= n:
#         while n % i == 0:
#             primfac.append(i)
#             n = n / i
#         i = i + 1
#     if n > 1:
#         primfac.append(n)
#     return primfac
#
# def lcm(*args):
#     result = []
#     x = 1
#     max1 = max(args)
#     max_res = primfacs(max1)
#     for n in args:
#         if n == 0:
#             return 0
#         n_list = primfacs(n)
#         for i in n_list:
#             if i not in max_res:
#                 result.append(i)
#     result.extend(max_res)
#     for i in result:
#         x *= i
#     return x
#
# from math import gcd
# def lcm1(*args):
#     lcm=1
#     for x in args:
#         if x!=0:
#             lcm=lcm*x//gcd(lcm,x)
#         else:
#             lcm=0
#     return lcm

def is_merge(s, part1, part2):
    s = [str(i) for i in s]
    f = 1
    for i in s:
        if i not in list(part1 + part2):
            f *= 0
        else:
            f *= 1
    return f == 1

print(is_merge('codewars', 'cod', 'wars'))

def is_merge(s, part1, part2):
    queue = [(s,part1,part2)]
    while queue:
        str, p1, p2 = queue.pop()
        if str:
            if p1 and str[0] == p1[0]:
                queue.append((str[1:], p1[1:], p2))
            if p2 and str[0] == p2[0]:
                queue.append((str[1:], p1, p2[1:]))
        else:
            if not p1 and not p2:
                return True
    return False