from data_base import DataBase

db = DataBase()

# db.create_main_area()
# db.generate()

# for i in range(17000, 18000):
#     print(i)
#     db.add(i, db.generate_random_string())
#db.add(25, db.generate_random_string())
#db.remove(17)

#print(db.remove(38))
#print(db.add(2300, 'nknjkj'))
print(db.find(2))
print(db.get_number_of_comparisons())