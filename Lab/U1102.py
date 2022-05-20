#vlojen cikyl
# test = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
# print(f"test pog: {test}")

#map
# test = list(map(int, input().split(', ')))
# print(test)

#filter lambda
# test = list(filter(lambda x: x % 2 == 0, map(int, input().split(', '))))
# print(test)

#filter normal
# def filter_function(a):
#     if a % 2 == 0:
#         return True
#     return False
#
#
# test = list(filter(filter_function, map(int, input().split(', '))))
# print(test)

#swap s index
# i = ['one', 'two', 'three', 'four']
# a, b = i.index('two'), i.index('three')
# i[b], i[a] = i[a], i[b]
# print(i)


# 1
# list1 = input().split(', ')
# list2 = input()
# result = [i for i in list1 if i in list2]
# print(result)

# 2a
# version = list(map(int, input().split('.')))
# if version[2] < 9:
#     version[2] += 1
# else:
#     version[2] = 0
#     if version[1] < 9:
#         version[1] += 1
#     else:
#         version[1] = 0
#         version[0] += 1
# print(f'{version[0]}.{version[1]}.{version[2]}')

# 2b
# def next_version(version_number):
#     version_number = int(''.join(version_number)) + 1
#     result = [str(num) for num in str(version_number)]
#     print('.'.join(result))
#
#
# data = input().split('.')
# next_version(data)

# 3
# text = input().split(' ')
# result = [i for i in text if len(i) % 2 == 0]
# print('\n'.join(result))

# 4
# numbers = input().split(', ')
# positive = [i for i in numbers if int(i) >= 0]
# negative = [i for i in numbers if int(i) < 0]
# even = [i for i in numbers if int(i) % 2 == 0]
# odd = [i for i in numbers if int(i) % 2 != 0]
# print(f"Positive: {', '.join(positive)}")
# print(f"Negative: {', '.join(negative)}")
# print(f"Even: {', '.join(even)}")
# print(f"Odd: {', '.join(odd)}")

# 5
# rooms = int(input())
# free_chairs = 0
# checker = True
# for i in range(1, rooms + 1):
#     command = input().split(' ')
#     chairs = command[0]
#     people = int(command[1])
#     if len(chairs) < people:
#         print(f"{people - len(chairs)} more chairs needed in room {i}")
#         checker = False
#     else:
#         free_chairs += len(chairs) - people
# if checker:
#     print(f"Game On, {free_chairs} free chairs left")

# 6
# electrons = int(input())
# shell_number = 1
# atom = []
#
# while electrons > 0:
#     current_charge = 2 * shell_number ** 2
#     if current_charge <= electrons:
#         atom.append(current_charge)
#         electrons -= current_charge
#     else:
#         atom.append(electrons)
#         electrons = 0
#     shell_number += 1
#
# print(atom)

# 7 sam
# import math
#
# numbers = list(map(int, input().split(', ')))
# max_number = max(numbers)
#
# times = math.ceil(max_number / 10)
#
# for i in range(1, times + 1):
#     current_list = []
#     for j in range(len(numbers)-1, -1, -1):
#         current_number = numbers[j]
#         if current_number <= i * 10:
#             current_list.append(current_number)
#             numbers.remove(current_number)
#     current_list.reverse()
#     print(f"Group of {i * 10}'s: {current_list}")

# 8
# message = input().split(' ')
#
# for i in range(len(message)):
#     current_word = message[i]
#     character = ''
#     temp_word = ''
#     new_word = ''
#     for j in current_word:
#         if j.isdigit():
#             character += j
#         else:
#             temp_word += j
#
#     new_word = chr(int(character)) + temp_word
#
#     new_list = list(new_word)
#     new_list[1], new_list[-1] = new_list[-1], new_list[1]
#     print(''.join(new_list), end=' ')

# 9
# target_list = list(map(int, input().split(' ')))
# command = input()
#
# while command != 'End':
#     explode = command.split(' ')
#     order = explode[0]
#     index = int(explode[1])
#     value = int(explode[2])
#
#     if order == 'Shoot':
#         if 0 <= index < len(target_list):
#             target_list[index] -= value
#             if target_list[index] <= 0:
#                 target_list.pop(index)
#
#     if order == 'Add':
#         if 0 <= index < len(target_list):
#             target_list.insert(index, value)
#         else:
#             print("Invalid placement!")
#
#     if order == 'Strike':
#         if index < len(target_list):
#             strike_range_start = index - value
#             strike_range_stop = index + value
#
#             if strike_range_start >= 0 and strike_range_stop < len(target_list):
#                 for i in range(len(target_list)-1, -1, -1):
#                     if strike_range_start <= i <= strike_range_stop:
#                         target_list.pop(i)
#             else:
#                 print("Strike missed!")
#
#     command = input()
#
# for j in range(len(target_list)):
#     print(target_list[j], end='')
#     if j < len(target_list)-1:
#         print('|', end='')

# 10
# neighborhood = list(map(int, input().split('@')))  # [10, 10, 10, 2]
# command = input()
# last_position = 0
# counter = 0
#
# while command != 'Love!':
#     explode = command.split(' ')
#     jump_length = int(explode[1])
#     jump_length += last_position
#
#     #   check if bigger than neighborhood
#     if jump_length > len(neighborhood) - 1:
#         jump_length = 0
#
#     if neighborhood[jump_length] == 2:
#         neighborhood[jump_length] = 0
#         print(f"Place {jump_length} has Valentine's day." )
#     elif neighborhood[jump_length] == 0:
#         print(f"Place {jump_length} already had Valentine's day.")
#     elif neighborhood[jump_length] > 2:
#         neighborhood[jump_length] -= 2
#
#     last_position = jump_length
#
#     command = input()
#
# print(f"Cupid's last position was {last_position}.")
#
# for i in range(len(neighborhood)):
#     if neighborhood[i] > 0:
#         counter += 1
#
# if counter > 0:
#     print(f"Cupid has failed {counter} places.")
# else:
#     print(f"Mission was successful.")

# 11
# collecting_items = input().split(', ')
# command = input()
#
# while command != 'Craft!':
#     explode = command.split(' - ')
#     operation = explode[0]
#     item = explode[1]
#
#     if operation == 'Collect':
#         if item not in collecting_items:
#             collecting_items.append(item)
#
#     elif operation == 'Drop':
#         if item in collecting_items:
#             collecting_items.remove(item)
#
#     elif operation == 'Combine Items':
#         new_explode = item.split(':')
#         old_item = new_explode[0]
#         new_item = new_explode[1]
#
#         if old_item in collecting_items:
#             my_index = collecting_items.index(old_item)
#             collecting_items.insert(my_index + 1, new_item)
#
#     elif operation == 'Renew':
#         if item in collecting_items:
#             temp = item
#             collecting_items.remove(item)
#             collecting_items.append(temp)
#
#     command = input()
#
# print(', '.join(collecting_items))










