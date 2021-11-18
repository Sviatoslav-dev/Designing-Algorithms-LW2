from data_base import DataBase

db = DataBase()

print(db.find(17301))
print(db.find(17302))
print(db.find(17310))
print(db.find(17313))
print(db.add(17332, 'tttttttt'))

# keys = [2582, 17960, 434, 17487, 17473, 4563, 23, 8677, 1564, 1900, 2321, 2323, 646, 867, 13333]
#
# for k in keys:
#     print(db.find(k))
#     print(db.get_number_of_comparisons())