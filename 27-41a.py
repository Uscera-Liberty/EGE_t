# file = open("27-41a.txt","r")
# f = []
# x = 0
# for line in file:
#     x += 1
#     if x == 1:
#         f.append(int(line))
#     else:
#         f.append(line)
# file.close()
#
# start = f[0]
# f.remove(f[0])
#
# perm = []
# for x in f:
#     temp = []
#     c = 0
#     for e in x:
#         if (e != " ") and (e != "\n"):
#             c *= 10
#             c += int(e)
#         else:
#             temp.append(c)
#             c = 0
#     perm.append(temp)
#
# temp = perm
# buffer_1 = []
# buffer_2_usefull = []
# buffer_2_useless = []
# buffer_other = []
# summary_min = 0
#
# for elem in temp:
#     minimal = min(elem)
#     elem.remove(min(elem))
#     if (elem[0]%2 == 0) and (elem[1]%2 == 0):
#         if minimal%2 == 0:
#             buffer_2_useless.append(elem)
#             summary_min += minimal
#         else:
#             elem.append(minimal)
#             buffer_2_usefull.append(elem)
#     elif (elem[0]%2 == 1) and (elem[1]%2 == 1):
#         buffer_1.append(elem)
#         summary_min += minimal
#     else:
#         buffer_other.append(elem)
#         summary_min += minimal
#
# print(len(buffer_1), "- 1")
# print(len(buffer_2_useless), "- 2_useless")
# print(len(buffer_2_usefull), "- 2_usefull")
# print(len(buffer_other), "- other")
#
# summary_1 = 0
# summary_2 = 0
#
#
# for elem in buffer_1:
#     summary_1 += elem[0]
#     summary_2 += elem[1]
# for elem in buffer_2_useless:
#     summary_1 += elem[0]
#     summary_2 += elem[1]
#
# if len(buffer_1)%2 == 0:
#     for elem in buffer_other:
#         if elem[0]%2 == 1:
#             summary_1 += elem[0]
#             summary_2 += elem[1]
#         else:
#             summary_1 += elem[1]
#             summary_2 += elem[0]
# else:
#     for elem in buffer_other:
#         if elem[0]%2 == 0:
#             summary_1 += elem[0]
#             summary_2 += elem[1]
#         else:
#             summary_1 += elem[1]
#             summary_2 += elem[0]
#
# if len(buffer_other)%2 == 0:
#     print(buffer_2_usefull)
#     spisok = []
#     for elem in buffer_2_usefull:
#         minimal = min(elem)
#         elem.remove(minimal)
#         medium  = min(elem)
#         elem.append(minimal)
#         spisok.append(medium-minimal)
#     print(spisok)
#     print(spisok.index(min(spisok)))
#     reboot = buffer_2_usefull[spisok.index(min(spisok))]
#     buffer_2_usefull.remove(reboot)
#     if len(buffer_1)%2 == 0:
#         summary_1 += min(reboot)
#         reboot.remove(min(reboot))
#         summary_min += min(reboot)
#         summary_2 += max(reboot)
#     else:
#         summary_2 += min(reboot)
#         reboot.remove(min(reboot))
#         summary_min += min(reboot)
#         summary_1 += max(reboot)
# for elem in buffer_2_usefull:
#     summary_min += min(elem)
#     elem.remove(min(elem))
#     summary_1 += elem[0]
#     summary_2 += elem[1]
#
# print(summary_min,summary_1,summary_2)

##Есть пары чисел ; составить максимально возможную сумму чисел такую чтобы она не делилась на 3
#считываем файл и переводим в инт
f = open('27-40b.txt')
n = int(f.readline())

def get():
    return list(map(int, f.readline().split()))
#формируем список с информацией
s = get()
for i in range(n-1):
    #формируем новую пару и делаем из этого сумму чисел из
    # двух пар ,которые потом будем распределять, а также наша
    # комбинация будет состоять из 3 элементов ,где нудевой это число из
    # суммы пар с остатком ноль,и дальше также
    para = get()
    cmb = [a+b for a in s for b in para]
    #заполняем комбинацию тремя нулями в которые потом будем класть
    # остальные элементы
    s1 = [0]*3
    #проходим по списку и формируем комбинации где 1 элемент
    # это сумма с остатком 1 и тд,а еще проверям максимальна ли эта сумма
    for x in cmb:
        if x>s1[x%3]:s1[x%3] = x
    #формируем еще один список где не будет нулей
    s = [x for x in s1 if x != 0]
#выводм максимальное число
m = 0
for x in s:
    if x%3 != 0 and x>m:
        m=x
print(m)

# ##Есть пары чисел ; составить минимально возможную сумму чисел такую чтобы она делилась на 3
# #считываем файл и переводим в инт
# f = open('21-41a')
# n = int(f.readline())
#
# def get():
#     return list(map(int, f.readline().split()))
# #формируем список с информацией
# s = get()
#
# for i in range(n-1):
#     #формируем новую пару и делаем из этого сумму чисел из
#     # двух пар ,которые потом будем распределять, а также наша
#     # комбинация будет состоять из 3 элементов ,где нудевой это число из
#     # суммы пар с остатком ноль,и дальше также
#     para = get()
#     cmb = [a+b for a in s for b in para]
#     #заполняем комбинацию тремя нулями в которые потом будем класть
#     # остальные элементы
#     s1 = [10000000000000]*3
#     #проходим по списку и формируем комбинации где 1 элемент
#     # это сумма с остатком 1 и тд,а еще проверям максимальна ли эта сумма
#     for x in cmb:
#         if x<s1[x%3]:s1[x%3] = x
#     #формируем еще один список где не будет нулей
#     s = [x for x in s1 if x != 10000000000000]
# #выводм максимальное число
# m = 0
# for x in s:
#     if x%3 == 0 and x<m:m=x
# print(m)
#
# ##Есть пары чисел ; составить максимально возможную сумму оканчивающуюся на 8
# #считываем файл и переводим в инт
# f = open('21-41a')
# n = int(f.readline())
#
# def get():
#     return list(map(int, f.readline().split()))
# #формируем список с информацией
# s = get()
#
# for i in range(n-1):
#     #формируем новую пару и делаем из этого сумму чисел из
#     # двух пар ,которые потом будем распределять, а также наша
#     # комбинация будет состоять из 3 элементов ,где нудевой это число из
#     # суммы пар с остатком ноль,и дальше также
#     para = get()
#     cmb = [a+b for a in s for b in para]
#     #заполняем комбинацию тремя нулями в которые потом будем класть
#     # остальные элементы
#     s1 = [0]*10 #количество остатков
#     #проходим по списку и формируем комбинации где 1 элемент
#     # это сумма с остатком 1 и тд,а еще проверям максимальна ли эта сумма
#     for x in cmb:
#         if x<s1[x%10]:s1[x%10] = x
#     #формируем еще один список где не будет нулей
#     s = [x for x in s1 if x != 0]
# #выводм максимальное число
#
# print(s[8])
#
#
# ##Есть тройки ; необходимо выбрать из каждой тройки два
# # числа так чтобы сумма не делилась на 5 и была максимально возможной
# #считываем файл и переводим в инт
# f = open('21-41a')
# n = int(f.readline())
#
# def get():
#     a = list(map(int, f.readline().split()))
#     return (a[0]+a[1] , a[0]+a[2] , a[2]+a[1])
# #формируем список с информацией
# s = get()
#
# for i in range(n-1):
#     #формируем новую пару и делаем из этого сумму чисел из
#     # двух пар ,которые потом будем распределять, а также наша
#     # комбинация будет состоять из 3 элементов ,где нудевой это число из
#     # суммы пар с остатком ноль,и дальше также
#     para = get()
#     cmb = [a+b for a in s for b in para]
#     #заполняем комбинацию тремя нулями в которые потом будем класть
#     # остальные элементы
#     s1 = [0]*10 #количество остатков
#     #проходим по списку и формируем комбинации где 1 элемент
#     # это сумма с остатком 1 и тд,а еще проверям максимальна ли эта сумма
#     for x in cmb:
#         if x>s1[x%5]:s1[x%5] = x
#     #формируем еще один список где не будет нулей
#     s = [x for x in s1 if x != 0]
# #выводм максимальное число
#
# print(max(s[1:]))
#
#
# ##Есть пары : нужно получить число минимально возможное где последняя цифра
# # совпадает с максимально возможной
# #считываем файл и переводим в инт
# f = open('21-41a')
# n = int(f.readline())
#
# def get():
#     a = list(map(int, f.readline().split()))
#     return (a[0]+a[1] , a[0]+a[2] , a[2]+a[1])
# #формируем список с информацией
# s = get()
# m = 0
# m += max(s)
# for i in range(n-1):
#     #формируем новую пару и делаем из этого сумму чисел из
#     # двух пар ,которые потом будем распределять, а также наша
#     # комбинация будет состоять из 3 элементов ,где нудевой это число из
#     # суммы пар с остатком ноль,и дальше также
#     para = get()
#     m+=max(para)
#     cmb = [a+b for a in s for b in para]
#     #заполняем комбинацию тремя нулями в которые потом будем класть
#     # остальные элементы
#     s1 = [10**20]*10 #количество остатков
#     #проходим по списку и формируем комбинации где 1 элемент
#     # это сумма с остатком 1 и тд,а еще проверям максимальна ли эта сумма
#     for x in cmb:
#         if x<s1[x%10]:s1[x%10] = x
#     #формируем еще один список где не будет нулей
#     s = [x for x in s1 if x != 10**20]
# #выводм максимальное число
#
# print(s[m%10])
#
#
# #та задача :есть тройки дальше их нужно распределить по такому признаку ,чтобы в одной группе сумма всех чисел в первой должна быть нечетной
# # а во второй четной найдите максимально возможное значение в третьей группе
#
# # здесь мы используем комбинации сумм для определения правильной последовательности
# from itertools import permutations
# f = open('27-41a.txt')
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
# print(s[1][2])
#

