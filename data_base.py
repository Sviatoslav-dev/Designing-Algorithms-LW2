import csv

class DataBase:
    def __init__(self):
        self.n_keys = 20000

    def generate(self, num=10000):
        pass

    def add(self, key, data):
        if self.find(key) != None:
            return -1

        area = self.getArea(key)

        main_data = []
        try:
            with open('main_area/' + area + '.csv', encoding='utf-8') as index_area:
                file_reader = csv.reader(index_area, delimiter=",")
                for row in file_reader:
                    main_data.append(row)
        except IOError:
            return -1

        for i in range(len(main_data)):
            if i < len(main_data) - 1 and i > 0:
                if key > int(main_data[i][0]) and key < int(main_data[i+1][0]):
                    main_data.insert(i+1, [str(key), data])
                    break
            elif i == len(main_data) - 1:
                if key > int(main_data[i][0]):
                    main_data.append([key, data])
            elif i == 0:
                if key < int(main_data[i][0]):
                    main_data.insert(i, [key, data])

        try:
            with open('main_area/' + area + '.csv', mode="w", encoding='utf-8') as w_file:
                file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
                for row in main_data:
                    file_writer.writerow(row)
        except IOError:
            return -1


    def getArea(self, key):
        index_data = []
        try:
            with open("index_area.csv", encoding='utf-8') as index_area:
                file_reader = csv.reader(index_area, delimiter=",")
                for row in file_reader:
                    index_data.append(row)
        except IOError:
            return None

        area = ''
        index_area_key = self.to_index_area_key(key)

        for row in index_data:
            if int(row[0]) == index_area_key:
                area = row[1]
        return area

    def to_index_area_key(self, key):
        res = 2000
        while key > res:
            res += 2000
        return res

    def find(self, key):
        area = self.getArea(key)

        if area != '':
            main_data = []
            try:
                with open('main_area/' + area + '.csv', encoding='utf-8') as index_area:
                    file_reader = csv.reader(index_area, delimiter=",")
                    for row in file_reader:
                        main_data.append(row)
            except IOError:
                return None

            for row in main_data:
                if int(row[0]) == key:
                    return row
        else:
            return None
        return None