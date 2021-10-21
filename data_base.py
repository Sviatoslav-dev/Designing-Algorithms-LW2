import csv
import random
import string

class DataBase:
    def __init__(self):
        self.area_size = 1000

    def create_main_area(self):
        file = open('main_area.csv', 'w')
        for _ in range(11000):
            file.write('00000,             \n')
        file.close()

    def generate_random_string(self):
        length = random.randint(1, 12)
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for _ in range(length))
        return rand_string

    def generate(self, num=10000):
        for i in range(num):
            print(i)
            key = random.randint(1, 20000)
            data = self.generate_random_string()
            self.add(key, data)

    def to_index_area_key(self, key):
        res = 2000
        while key > res:
            res += 2000
        return res

    def get_address(self, key):
        index_data = []
        try:
            with open("index_area.csv") as index_area:
                file_reader = csv.reader(index_area, delimiter=",")
                for row in file_reader:
                    index_data.append(row)
        except IOError:
            return None

        area = ''
        if type(key) == type(1000):
            index_area_key = self.to_index_area_key(key)
        else:
            index_area_key = 'overflow'

        for row in index_data:
            if row[0] == str(index_area_key):
                area = row[1]
        return int(area)

    def find(self, key):
        address = self.get_address(key)

        with open("main_area.csv", 'r') as main_area_file:
            main_area_file.seek(address * 21)

            area = main_area_file.read(self.area_size * 20)
            area = area.split(sep='\n')
            main_area_search = self.find_in_area(area, key)
            if main_area_search != None:
                return main_area_search
            elif self.occupancy(area) >= self.area_size:
                address = self.get_address('overflow')
                main_area_file.seek(address * 21)
                area = main_area_file.read(self.area_size * 20)
                area = area.split(sep='\n')
                main_area_search = self.find_in_area(area, key)
                return main_area_search
            else:
                return None

    def num_to_len_5(self, num):
        str_num = str(num)
        if len(str_num) > 5:
            return -1

        return '0' * ((5 - len(str_num))) + str_num

    def str_to_len_n(self, s, n):
        return s + (' ' * (n - len(s)))

    def create_line(self, key, data):
        return self.num_to_len_5(key) + ',' + self.str_to_len_n(data, 13)

    def add_line(self, linses, line):
        for i in range(len(linses)):
            if int(linses[i][:5]) == int(line[:5]):
                linses[i] = line
                return linses


            if i < len(linses) - 1:
                if int(linses[i + 1][:5]) != 0:
                    if int(line[:5]) > int(linses[i][:5]) and int(line[:5]) < int(linses[i + 1][:5]):
                        linses.insert(i + 1, line)
                        break
                elif int(linses[i][:5]) != 0:
                    if int(line[:5]) > int(linses[i][:5]):
                        linses.insert(i + 1, line)
                        break

            if i == 0:
                if int(line[:5]) < int(linses[i][:5]) or int(linses[i][:5]) == 0:
                    linses.insert(i, line)
                    break
        return linses[:-1]

    def find_in_area(self, area, key):
        for line in area:
            if int(line[:5]) == 0:
                return None

            if int(line[:5]) == key:
                return line

    def add(self, key, data):
        address = self.get_address(key)
        new_line = self.create_line(key, data)

        with open("main_area.csv", '+r') as main_area_file:
            main_area_file.seek(address * 21)

            area = main_area_file.read(self.area_size * 20)
            area = area.split(sep='\n')
            area = area[:-1]

            if self.occupancy(area) < self.area_size or self.find_in_area(area, key) != None:
                print('---------')
                area = self.add_line(area, new_line)
                main_area_file.seek(address * 21)
            else:
                print('++++++++=')
                address = self.get_address('overflow')
                main_area_file.seek(address * 21)
                area = main_area_file.read(self.area_size * 20)
                area = area.split(sep='\n')
                area = area[:-1]
                area = self.add_line(area, new_line)
                main_area_file.seek(address * 21)

            united_area = ''
            for line in area:
                #print(line)
                united_area += self.str_to_len_n(line, 19) + '\n'

            main_area_file.write(united_area)

    def remove_in_area(self, key, area):
        for i in range(len(area)):
            if int(area[i][:5]) != 0:
                if int(area[i][:5]) == key:
                    print('+++++++++')
                    del area[i]
                    break
            else:
                break
        area.append('00000,             ')
        return area

    def remove(self, key):
        address = self.get_address(key)

        with open("main_area.csv", '+r') as main_area_file:
            main_area_file.seek(address * 21)

            area = main_area_file.read(self.area_size * 20)
            area = area.split(sep='\n')
            area = area[:-1]

            if self.occupancy(area) < self.area_size or self.find_in_area(area, key) != None:
                if self.find_in_area(area, key) == None:
                    return -1
                area = self.remove_in_area(key, area)
                main_area_file.seek(address * 21)
            else:
                address = self.get_address('overflow')
                main_area_file.seek(address * 21)
                area = main_area_file.read(self.area_size * 20)
                area = area.split(sep='\n')
                area = area[:-1]
                if self.find_in_area(area, key) == None:
                    return -1
                area = self.remove_in_area(key, area)
                main_area_file.seek(address * 21)

            united_area = ''
            for line in area:
                united_area += self.str_to_len_n(line, 19) + '\n'

            main_area_file.write(united_area)

    def occupancy(self, area):
        k = 0
        for line in area:
            if int(line[:5]) == 0:
                return k
            k += 1
        return k