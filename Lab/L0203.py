# Dictionaries: key-value pairs

# dict() ili dict {}
# dict(name='Daniel', age=22) #kliuch = stoinost
# my_dict = {'name': 'Daniel', 'age': 22}
# print(my_dict)

#print by key
# print(my_dict['name'])
# print(my_dict.get('age')) #.get na lipsvasht kliuch vryshta None, t.e. po-dobre
# print(my_dict.get('lipsvasht')) #.get na lipsvasht kliuch vryshta None, t.e. po-dobre

#ne mojem da promenqme kliuchovete, no mojem stoinostite, taka i dobavqme novi
# my_dict['age'] = 77
# print(my_dict.get('age'))

#-------------------------------------------------------------------------------------
# 1
# data = input().split(' ')
# bakery = {}
#
# for i in range(0, len(data), 2):
#     food = data[i]
#     quantity = int(data[i+1])

#     bakery[food] = quantity
#
# print(bakery)

#-------------------------------------------------------------------------------------
#iteration with keys()
# squares_dict = {1: 1, 2: 4, 3: 9}
# for i in squares_dict.keys():
#     squares_dict[i] *= 2
#     print(i, end=' ')    #prints keys
#     print(squares_dict[i], end=' ')  #prints values
# print(squares_dict)

#iteration with values()
# squares_dict = {1: 1, 2: 4, 3: 9}
# for i in squares_dict.values():
#     print(i, end=' ')  #prints values

#iteration with items() - vryshta tuple
# squares_dict = {1: 1, 2: 4, 3: 9}
# for (i, j) in squares_dict.items():
#     print(f"Keys: {i}, Values: {j}")

#-------------------------------------------------------------------------------------
#check for existence
# my_dict = {'name': 'Daniel', 'age': 39}
# if 'name' in my_dict.keys(): #you can skip .keys()
#     print(my_dict['name'])
# if 39 in my_dict.values():
#     print('yes')

#-------------------------------------------------------------------------------------
# 2
# pairs = input().split(' ')
# search = input().split(' ')
# stock = {}
#
# for i in range(0, len(pairs), 2):
#     food = pairs[i]
#     quantity = pairs[i+1]
#     stock[food] = quantity
#
# for j in search:
#     if j in stock.keys():
#         print(f"We have {stock[j]} of {j} left")
#     else:
#         print(f"Sorry, we don't have {j}")

# 3
# def statistics():
#     print('Products in stock:')
#     for i in stock.keys():
#         print(f'- {i} {stock[i]}')
#     print(f'Total Products: {len(stock.keys())}')       #moje i taka s keys
#     print(f'Total Quantity: {sum(stock.values())}')     #moje i taka s values
#
#
# stock = {}
#
# command = input()
# while 1:
#     if command == 'statistics':
#         statistics()
#         break
#     else:
#         explode = command.split(' ')
#         product = explode[0]
#         quantity = int(explode[1])
#
#         if product in stock.keys():
#             stock[product] += quantity
#         else:
#             stock[product] = quantity
#
#     command = input()

#-------------------------------------------------------------------------------------
#dictionary methods
# my_dict = {"value1": 2, "value2": 4}
# my_dict.clear()                     # clear dictionary
# copied_dict = my_dict.copy()        # syzdava kopie
# my_dict.pop("value1")               #maha element
# my_dict.popitem()                   #removes an item that was last inserted and returns it as a tuple (key, value)

# del my_dict['value1']               #deletes this item (different from clear)
# del my_dict                         #deletes the whole dictionary variable

#nested dictionaries
# students = {1: {'name': 'Daniel', 'age': 39}, 2: {'name': 'Maxi', 'age': 9}}
#
# students[3] = {}
# students[3]['name'] = 'maimuna'
#
# for key, value in students.items():
#     print(f'{key}: {value}')
#     for nested_key, nested_value in value.items():
#         print(f'{nested_key}: {nested_value}')

#-------------------------------------------------------------------------------------
# 4
# command = input()
# courses = {}
#
# while ':' in command:
#
#     # data = command.split(':')
#     # name = data[0]
#     # id_nr = data[1]
#     # course = data[2]
#
# #                  variant s tuple na predhodnite 4 reda
#     (name, id_nr, course) = command.split(':')
#
#     if course not in courses.keys():
#         courses[course] = {}
#     courses[course][id_nr] = name
#     command = input()
#
# search = ' '.join(command.split('_'))
#
# for i in courses.keys():
#     if i == search:
#         for j in courses[search].keys():
#             print(f'{courses[search][j]} - {j}')

#-------------------------------------------------------------------------------------
# dictionary comprehension
# data = [('Daniel', 39), ('Maxi', 9)]
# my_dict = {i: j for (i, j) in data}
# print(my_dict)

# nums = [1, 2, 3]
# cubes = {x: x * x for x in nums}
# print(cubes)
#-------------------------------------------------------------------------------------

# 5
# command = input().split(', ')
# my_dict = {x: ord(x) for x in command}
# print(my_dict)

# 6
# words = input().split(' ')
# my_dict = {}
# to_print = []
#
# for i in words:
#     if i.lower() not in my_dict.keys():
#         my_dict[i.lower()] = 1
#
#     else:
#         my_dict[i.lower()] += 1
#
# for j in my_dict.keys():
#     if my_dict[j] % 2 != 0:
#         to_print.append(j)
#
# print(' '.join(to_print))

# 7
# number = int(input())
# my_dict = {}
# for i in range(number):
#     word = input()
#     synonym = input()
#
#     if word not in my_dict.keys():
#         my_dict[word] = []
#
#     my_dict[word].append(synonym)
#
# for j in my_dict.keys():
#     joined = ', '.join(my_dict[j])
#     print(f'{j} - {joined}')




