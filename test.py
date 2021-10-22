import math
# text = open('test_text.txt', '+r')
#
# print(text.seek(2))
#
# print(text.write('                                   '))
#
# text.close()

# file = open('main_area.csv', 'w')
#
# for _ in range(20000):
#     file.write('00000,             \n')
#
# file.close()

# with open("main_area.csv", 'r') as main_area_file:
#     main_area_file.seek(3 * 21)
#
#     line = main_area_file.readline()
#     print(line)

#print('ykjksdf' * -3)

# with open('main_area.csv', 'r') as file:
#     k = 1
#     while k < 11000:
#         line = file.readline()
#         if len(line) != 20:
#             print(len(line), k)
#         k += 1

array1 = [1, 4, 7, 23, 25, 29, 31, 32, 43, 45]
array2 = [1, 4, 7, 23, 25, 29, 31, 32, 43, 45, 55, 56, 58, 59, 60, 61, 62, 63, 64, 65, 66]
array3 = [1, 4, 7, 23, 25, 29]

def Sharas_search(array, K):
    N = len(array)
    k = int(math.log2(N))
    i = 2 ** k

    if K < array[i - 1]:
        j = 0
        delta = 2 ** (k - j)

        while delta > 0:
            j += 1
            if K < array[i - 1]:
                i -= delta // 2 + 1
                i = max(i, 1)
            elif K > array[i - 1]:
                i = max(i, 1)
                i += delta // 2 + 1

            if array[i - 1] == K:
                return 'Success'

            if delta > 1:
                delta = 2 ** (k - j)
            else:
                delta = 0
    elif K > array[i - 1]:
        l = int(math.log2(N - 2**k + 1))
        i = N + 1 - 2**l
        j = 1
        delta = 2 ** (l - j)
        if array[i - 1] == K:
            return 'Success'

        while delta > 0:
            j += 1
            if K < array[i - 1]:
                i -= delta // 2 + 1
            elif K > array[i - 1]:
                i += delta // 2 + 1

            if array[i - 1] == K:
                return 'Success'

            if delta > 1:
                delta = 2 ** (l - j)
            else:
                delta = 0
    else:
        return 'Success'

for n in array2:
    print(Sharas_search(array2, n))