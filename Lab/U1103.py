
#  +---+---+---+---+---+
#  | m | o | v | i | e |
#  +---+---+---+---+---+
#    0   1   2   3   4
#   -5  -4  -3  -2  -1
# a = 'movie'
# print(a[-5])

# print(''.join(reversed('12345')))
# print('12345'[::-1])   # syshtoto

# message = 'Hello World!,,,,,'
# print(message.strip(','))   #maha zapetaikite

# sentence = 'this phrase is a string!'
# print(sentence[-7]) #zapochva printiraneto pored ot sedmiq predposleden

# text = 'Hello Daniel'
# print(text.title())         #pyrvite bukvi pravi glavni
# print(text.swapcase())      #obryshta glavni malki
# print(text.find('Daniel'))      #Daniel zapochva ot 6ti index

#\t - tab, \b - maha 1 space, \

# txt = 'price is {price:.2f} dollars'
# print(txt.format(price=199))

#-------------------------------------------------------------------------------------

# 1
# user_names = input().split(', ')
# for i in user_names:
#     if 3 <= len(i) <= 16:
#         to_print = True
#         for j in range(len(i)):
#             if not i[j].isalnum() and '-' not in i[j] and '_' not in i[j]:
#                 to_print = False
#
#         if to_print:
#             print(i)

# 2
# command = input().split(' ')
# string1 = command[0]
# string2 = command[1]
# total = 0
#
# if len(string1) > len(string2):
#     for i in range(len(string1)):
#         if len(string2) > i:
#             total += ord(string1[i]) * ord(string2[i])
#         else:
#             total += ord(string1[i])
#
# else:
#     for i in range(len(string2)):
#         if len(string1) > i:
#             total += ord(string2[i]) * ord(string1[i])
#         else:
#             total += ord(string2[i])
#
# print(total)

# 3
# path = input()
# position1 = 0
# position2 = 0
#
# for i in range(len(path)-1, -1, -1):
#     if path[i] == "\\":
#         break
#     else:
#         position1 = i - len(path)
#
# new_string = path[position1::]
#
# #LinkedList.cs
# for j in range(len(new_string)-1, -1, -1):
#     if new_string[j] == chr(46):
#         break
#     else:
#         position2 = j - len(new_string)
#
# print(f'File name: {path[position1:position2-1:]}')
# print(f'File extension: {path[position2::]}')

# 4
# command = input()
# encrypted = ''
#
# for i in command:
#     order = ord(i) + 3
#     encrypted += chr(order)
#
# print(encrypted)

# 5
# command = input()
# for i in range(len(command)):
#     if command[i] == ':':
#         print(f':{command[i+1]}')

# 6
# command = input()
# clean = ''
# last_letter = ''
# for i in range(len(command)):
#     if command[i] != last_letter:
#         clean += command[i]
#     last_letter = command[i]
# print(clean)

# 7
# text = input()
# new_text = list()
# strength = 0
#
# for ch in text:
#     if ch.isdigit():
#         strength += int(ch)
#         strength -= 1
#         continue
#     else:
#         if strength < 1:
#             new_text.append(ch)
#         else:
#             if ch == ">":
#                 new_text.append(ch)
#             else:
#                 strength -= 1
#                 continue
# print("".join(new_text))

# 8
# command = input().split()             #splitva i po 1 space i po tab!!!!!!!!!!!
# total = 0
#
# for i in command:
#     if i != '':
#         first_letter = i[0:1:]
#         last_letter = i[-1::]
#         number = int(i[1:-1:])
#
#         if first_letter.isupper():
#             first_letter_position = ord(first_letter) - 64
#             number /= first_letter_position
#
#         elif first_letter.islower():
#             first_letter_position = ord(first_letter) - 96
#             number *= first_letter_position
#
#         if last_letter.isupper():
#             last_letter_position = ord(last_letter) - 64
#             number -= last_letter_position
#
#         elif last_letter.islower():
#             last_letter_position = ord(last_letter) - 96
#             number += last_letter_position
#
#         total += number
#
# print(f"{total:.2f}")

# 9 - sam
# command = input()
# current_string = ''
# to_print = ''
# unique = ''
# times = ''
# ready = False
#
# for i in range(len(command)):
#     if command[i] not in '0123456789':
#
#         if ready:
#             to_print += current_string * int(times)
#             current_string = ''
#             times = ''
#             ready = False
#
#         current_string += command[i].upper()
#
#         if command[i].upper() not in unique:
#             unique += command[i].upper()
#
#     else:
#         times += command[i]
#         ready = True
#
# if ready:
#     to_print += current_string * int(times)
#     current_string = ''
#     times = ''
#     ready = False
#
# print(f'Unique symbols used: {len(unique)}')
# print(to_print)

#-------------------------------------------------------------------------------------
# replace neshto s nishto
# #stava i: data = [x.strip() for x in tickets.split(',')]
#-------------------------------------------------------------------------------------

# 10
# def additional_func(partition):
#     current_max_num = 0
#     special_char = ''
#
#     for ch in partition:
#         if ch != special_char:
#             if current_max_num >= 6:
#                 break
#             current_max_num = 1
#             special_char = ch
#         else:
#             current_max_num += 1
#
#     return [current_max_num, special_char]
#
#
# def ticket_validator(ticket):
#     ticket_condition = ''
#
#     if len(ticket) != 20:
#         ticket_condition = "invalid ticket"
#     elif ticket[0] * 20 == ticket and ticket[0] in '@#$^':
#         ticket_condition = f'ticket "{ticket}" - 10{ticket[0]} Jackpot!'
#     else:
#         data_source = ''
#         if additional_func(ticket[0:int(len(ticket) / 2)]) > additional_func(ticket[int(len(ticket) / 2):]):
#             data_source = additional_func(ticket[int(len(ticket) / 2):])
#         else:
#             data_source = additional_func(ticket[0: int(len(ticket) / 2)])
#         number_of_special_signs = data_source[0]
#         special_sign = data_source[1]
#
#         if number_of_special_signs < 6 or special_sign not in '@#$^':
#             ticket_condition = f'ticket "{ticket}" - no match'
#         else:
#             ticket_condition = f'ticket "{ticket}" - {number_of_special_signs}{special_sign}'
#
#     return ticket_condition
#
#
# def winning_ticket(data):
#     for ticket in data:
#         print(ticket_validator(ticket))
#
#
# info = input()
# data = [x.strip() for x in info.split(',')]
# winning_ticket(data)















