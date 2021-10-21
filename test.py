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

with open('main_area.csv', 'r') as file:
    k = 1
    while k < 20000:
        line = file.readline()
        if len(line) != 20:
            print(len(line), k)
        k += 1