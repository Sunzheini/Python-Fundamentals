# 1 - 01. World Tour - nesyobrazih tova: Note: After each command, print the current state of the string
# initial_stops = input()
#
# command = input()
# while command != 'Travel':
#     explode = command.split(':')
#     action = explode[0]
#
#     if action == 'Add Stop':
#         index = int(explode[1])
#         string = explode[2]
#
#         if 0 <= index < len(initial_stops):
#             if index == 0:
#                 temp = string + initial_stops
#                 initial_stops = temp
#
#             else:
#                 temp = initial_stops[0:index] + string + initial_stops[index:]
#                 initial_stops = temp
#
#         print(initial_stops)
#
#     elif action == 'Remove Stop':
#         start_index = int(explode[1])
#         end_index = int(explode[2])
#
#         if 0 <= start_index <= end_index < len(initial_stops):
#             if start_index == 0 and end_index < len(initial_stops)-1:
#                 temp = initial_stops[end_index + 1:]
#                 initial_stops = temp
#
#             elif start_index > 0 and end_index == len(initial_stops)-1:
#                 temp = initial_stops[0:start_index]
#                 initial_stops = temp
#
#             elif start_index == 0 and end_index == len(initial_stops)-1:
#                 initial_stops = ''
#             else:
#                 temp = initial_stops[0:start_index] + initial_stops[end_index+1:]
#                 initial_stops = temp
#
#         print(initial_stops)
#
#     elif action == 'Switch':
#         old_string = explode[1]
#         new_string = explode[2]
#
#         if old_string in initial_stops:
#             temp = initial_stops.replace(old_string, new_string)
#             initial_stops = temp
#
#         print(initial_stops)
#
#     command = input()
#
# print(f"Ready for world tour! Planned stops: {initial_stops}")

# 2 - 02. Ad Astra
# import re
#
# information = input()
# pattern = r'([|#])(?P<item>[A-Za-z ]+)(\1)(?P<date>[0-9]{2}/[0-9]{2}' \
#           r'/[0-9]{2})(\1)(?P<cal>[0-9][0-9]?[0-9]?[0-9]?[0]?)(\1)'
# matches = re.finditer(pattern, information)
#
# total = 0
#
# for i in matches:
#     total += int(i.group('cal'))
#
# last = total // 2000
#
# print(f'You have food to last you for: {last} days!')
# matches = re.finditer(pattern, information)
# for j in matches:
#     print(f"Item: {j.group('item')}, Best before: {j.group('date')}, "
#           f"Nutrition: {j.group('cal')}")

# 3 - 03. P!rates
# targets = {}
#
# command1 = input()
# while command1 != 'Sail':
#     explode = command1.split('||')
#     city = explode[0]
#     population = int(explode[1])
#     gold = int(explode[2])
#
#     if city not in targets.keys():
#         targets[city] = {'population': 0, 'gold': 0}
#
#     targets[city]['population'] += population
#     targets[city]['gold'] += gold
#
#     command1 = input()
#
# #{'Nassau': {'population': 95000, 'gold': 1000}}
#
# command2 = input()
# while command2 != 'End':
#     explode = command2.split('=>')
#     action = explode[0]
#
#     if action == 'Plunder':
#         town = explode[1]
#         people = int(explode[2])
#         gold = int(explode[3])
#
#         targets[town]['population'] -= people
#         targets[town]['gold'] -= gold
#         print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
#
#         if targets[town]['population'] == 0 or targets[town]['gold'] == 0:
#             print(f"{town} has been wiped off the map!")
#             targets.pop(town)
#
#     elif action == 'Prosper':
#         town = explode[1]
#         gold = int(explode[2])
#
#         if gold >= 0:
#             targets[town]['gold'] += gold
#             print(f"{gold} gold added to the city "
#                   f"treasury. {town} now has {targets[town]['gold']} gold.")
#         else:
#             print("Gold added cannot be a negative number!")
#
#     command2 = input()
#
# #{'Nassau': {'population': 95000, 'gold': 1000}}
#
# settlements = 0
# for i in targets.keys():
#     settlements += 1
#
# if settlements > 0:
#     print(f"Ahoy, Captain! There are {settlements} wealthy settlements to go to:")
#
#     for j in targets.keys():
#         print(f"{j} -> Population: {targets[j]['population']} citizens, "
#               f"Gold: {targets[j]['gold']} kg")
#
# else:
#     print("Ahoy, Captain! All targets have been plundered and destroyed!")

# 4a - 02. Fancy Barcodes - 90/100
# import re
#
# count = int(input())
# pattern = r'(@[#]+)(?P<barcode>[A-Z][A-Za-z0-9]{4,}[A-Z])(@[#]+)'
#
# for i in range(count):
#     barcode = input()
#
#     if re.search(pattern, barcode) is None:  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#         print('Invalid barcode')
#         continue
#
#     matches = re.finditer(pattern, barcode)
#
#     for j in matches:
#         current_barcode = j.group('barcode')
#
#         product_group = ''
#         is_any = False
#
#         for k in current_barcode:
#             if k in '0123456789':
#                 product_group += k
#                 is_any = True
#
#         if is_any:
#             product_group = int(product_group)
#             print(f"Product group: {product_group}")
#         else:
#             print(f"Product group: 00")

# 4b - 02. Fancy Barcodes - 100/100
# import re
#
# count = int(input())
# pattern = r'(@[#]+)(?P<barcode>[A-Z][A-Za-z0-9]{4,}[A-Z])(@[#]+)'
#
# for i in range(count):
#     barcode = input()
#
#     matches = re.match(pattern, barcode)        # moje da vryshta None!!!
#
#     if matches is None or len(matches.group()) < 10:
#         print("Invalid barcode")
#     else:
#         extract_nums = re.findall(r'\d', matches.group('barcode'))
#         if not extract_nums:
#             print("Product group: 00")
#         else:
#             print(f"Product group: {''.join(extract_nums)}")







