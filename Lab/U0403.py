# dictionary e 6 pyti po byrzo ot list

# person = {'name': 'Daniel', 'gender': 'M', 'age': 39}
# print(person.keys())
# print(person.values())
# print(person.items())

# person.pop('gender')
# print(person)

# person.popitem()
# print(person)

# print(person.get('age'))

# person.clear()
# print(person)


# test = ('arg1', 'arg2', 'arg3')
# val = 0
# my_dict = dict.fromkeys(test, val)
# print(my_dict)


# data = ['one', 'two', 'three']
# numbers = [1, 2, 3]
# result = dict(zip(data, numbers))
# print(result)


# messed_dict = {'c': 3, 'b': 2, 'a': 1}
# for i, j in sorted(messed_dict.items()):
#     print(f'{i} - {j}')

# for k in sorted(results.keys()):
#     print(k)
#     for (m, p) in sorted(results[k].items(), key=lambda cp: -cp[1]):
#         print(f'#  {m} -> {p}')

# number = [1, 2, 3]
# squares_dict = {x: x * x for x in number}
# print(squares_dict)


# people = {1: {'name': 'Daniel', 'age': 39}, 2: {'name': 'Maxi', 'age': 9}}
# print(people[1]['name'])

#-------------------------------------------------------------------------------------
# 1
# command = input()
# my_dict = {}
#
# for i in command:
#     if i != ' ':
#         if i not in my_dict.keys():
#             my_dict[i] = 0
#         my_dict[i] += 1
#
# for j in my_dict.keys():
#     print(f'{j} -> {my_dict[j]}')

# 1b
# from collections import Counter
# word = input()
# result = Counter(word)
#
# for i, j in result.items():
#     if i != ' ':
#         print(f'{i} -> {j}')

# 2
# command = input()
# my_dict = {}
#
# while command != 'stop':
#     a_resource = command
#     quantity = int(input())
#
#     if a_resource not in my_dict.keys():
#         my_dict[a_resource] = 0
#
#     my_dict[a_resource] += quantity
#
#     command = input()
#
# for i in my_dict.keys():
#     print(f'{i} -> {my_dict[i]}')

# 3a
# country_names = input().split(', ')
# capitals = input().split(', ')
# my_dict = dict(zip(country_names, capitals))
#
# for i in my_dict.keys():
#     print(f'{i} -> {my_dict[i]}')

# 4
# phonebook = {}
# command = input()
#
# while '-' in command:
#     explode = command.split('-')
#     name = explode[0]
#     number = explode[1]
#
#     phonebook[name] = number
#
#     command = input()
#
# for i in range(int(command)):
#     search = input()
#     if search not in phonebook.keys():
#         print(f'Contact {search} does not exist.')
#     else:
#         print(f'{search} -> {phonebook[search]}')

# 5
# legendary_dict = {'shards': 0, 'fragments': 0, 'motes': 0}
# junk_dict = {}
# exit_loop = False
#
# while 1:
#
#     if exit_loop:
#         break
#
#     loot = input().split()
#     for i in range(0, len(loot), 2):
#         quantity = int(loot[i])
#         item = loot[i+1].lower()
#
#         if item in legendary_dict.keys():
#             legendary_dict[item] += quantity
#
#             if legendary_dict[item] >= 250:
#                 legendary_dict[item] -= 250
#
#                 if item == 'shards':
#                     print('Shadowmourne obtained!')
#                 elif item == 'fragments':
#                     print('Valanyr obtained!')
#                 elif item == 'motes':
#                     print('Dragonwrath obtained!')
#
#                 exit_loop = True
#                 break
#
#         else:
#             if item not in junk_dict:
#                 junk_dict[item] = quantity
#             else:
#                 junk_dict[item] += quantity
#
# for j in legendary_dict.keys():
#     print(f'{j}: {legendary_dict[j]}')
#
# for k in junk_dict.keys():
#     print(f'{k}: {junk_dict[k]}')

# 6
# products = {}
# command = input()
#
# while command != 'buy':
#
#     new_product = command.split(' ')
#     name = new_product[0]
#     price = float(new_product[1])
#     quantity = int(new_product[2])
#
#     if name not in products.keys():
#         products[name] = {}
#         products[name]['price'] = price
#         products[name]['quantity'] = quantity
#     else:
#         products[name]['price'] = price
#         products[name]['quantity'] += quantity
#
#     command = input()
#
# for i in products.keys():
#     total = products[i]['price'] * products[i]['quantity']
#     print(f'{i} -> {total:.2f}')

# 7
# number = int(input())
# my_dict = {}
#
# for i in range(number):
#     command = input().split(' ')
#     action = command[0]
#     name = command[1]
#
#     if action == 'register':
#         plate = command[2]
#
#         if name not in my_dict.keys():
#             my_dict[name] = plate
#             print(f"{name} registered {plate} successfully")
#         else:
#             print(f"ERROR: already registered with plate number {my_dict[name]}")
#
#     elif action == 'unregister':
#         if name in my_dict.keys():
#             my_dict.pop(name)
#             print(f"{name} unregistered successfully")
#         else:
#             print(f"ERROR: user {name} not found")
#
# for i in my_dict.keys():
#     print(f'{i} => {my_dict[i]}')

# 8
# courses_dict = {}
# command = input()
#
# while command != 'end':
#     explode = command.split(' : ')
#     course = explode[0]
#     student = explode[1]
#
#     if course not in courses_dict.keys():
#         courses_dict[course] = []
#
#     courses_dict[course].append(student)
#
#     command = input()
#
# for i in courses_dict.keys():
#     print(f'{i}: {len(courses_dict[i])}')
#     for j in courses_dict[i]:
#         print(f'-- {j}')

# 9
# academy_dict = {}
# number = int(input())
#
# for i in range(number):
#     name = input()
#     grade = float(input())
#
#     if name not in academy_dict.keys():
#         academy_dict[name] = []
#
#     academy_dict[name].append(grade)
#
# for j in academy_dict.keys():
#     average = sum(academy_dict[j])/len(academy_dict[j])
#     if average >= 4.50:
#         print(f'{j} -> {average:.2f}')

# 10
# information_dict = {}
# command = input()
#
# while command != 'End':
#     explode = command.split(' -> ')
#     company = explode[0]
#     person_id = explode[1]
#
#     if company not in information_dict.keys():
#         information_dict[company] = []
#
#     if person_id not in information_dict[company]:
#         information_dict[company].append(person_id)
#
#     command = input()
#
# for i in information_dict.keys():
#     print(f'{i}')
#     for j in information_dict[i]:
#         print(f'-- {j}')

#11
# my_dict = {}
# command = input()
#
# while command != 'Lumpawaroo':
#
#     change_condition = True
#
#     if '|' in command:
#         explode = command.split(' | ')
#         force_side = explode[0]
#         force_user = explode[1]
#
#         if force_side not in my_dict.keys():
#             my_dict[force_side] = []
#
#         for i in my_dict.keys():
#             if force_user in my_dict[i]:
#                 change_condition = False
#
#         if change_condition:
#             my_dict[force_side].append(force_user)
#
#     elif '->' in command:
#         explode = command.split(' -> ')
#         force_side = explode[1]
#         force_user = explode[0]
#
#         if force_side not in my_dict.keys():
#             my_dict[force_side] = []
#
#         for j in my_dict.keys():
#             if force_user in my_dict[j]:
#                 my_dict[j].remove(force_user)
#                 my_dict[force_side].append(force_user)
#                 change_condition = False
#                 break
#
#         if change_condition:
#             my_dict[force_side].append(force_user)
#
#         print(f"{force_user} joins the {force_side} side!")
#
#     command = input()
#
# for k in my_dict.keys():
#     if len(my_dict[k]) > 0:
#         print(f'Side: {k}, Members: {len(my_dict[k])}')
#         for m in my_dict[k]:
#             print(f'! {m}')

#12
# results = {}
# submissions = {}
# command = input()
#
# while command != 'exam finished':
#     explode = command.split('-')
#
#     if explode[1] == 'banned':
#         name = explode[0]
#         results.pop(name)
#
#     else:
#         name = explode[0]
#         topic = explode[1]
#         points = int(explode[2])
#
#         if name not in results.keys():
#             results[name] = {}
#
#         if topic not in results[name].keys():
#             results[name][topic] = points
#
#             if topic not in submissions.keys():
#                 submissions[topic] = 1
#             else:
#                 submissions[topic] += 1
#
#         else:
#             if points > results[name][topic]:
#                 results[name][topic] = points
#
#             if topic not in submissions.keys():
#                 submissions[topic] = 1
#             else:
#                 submissions[topic] += 1
#
#     command = input()
#
# print('Results:')
# for i, j in results.items():
#     for k in j.keys():
#         print(f'{i} | {j[k]}')
#
# print('Submissions:')
# for x in submissions.keys():
#     print(f'{x} - {submissions[x]}')



