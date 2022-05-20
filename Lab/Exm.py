

# 1
# spell = input()
# command = input()
# while command != 'Abracadabra':
#     explode = command.split(' ')
#     action = explode[0]
#
#     if action == 'Abjuration':
#         spell = spell.upper()
#         print(spell)
#
#     elif action == 'Necromancy':
#         spell = spell.lower()
#         print(spell)
#
# # ------------------------------------------------------------------------------------
#     # A7ci0
#     # Illusion 1 c
#     #probvai s enumerate
#
#     elif action == 'Illusion':
#         index = int(explode[1])
#         letter = explode[2]
#
#         if 0 <= index <= len(spell)-1:
#             # if index == 0:
#             #     temp = letter + spell[index:]
#             #     spell = temp
#             # elif index == len(spell)-1:
#             #     temp = spell[0:index] + letter
#             #     spell = temp
#             # else:
#             #     temp = spell[0:index] + letter + spell[index+1:]
#             #     spell = temp
#             temp = ''
#             for index1, digit in enumerate(spell):
#                 if index1 == index:
#                     temp += letter
#                 else:
#                     temp += spell[index1]
#             spell = temp
#             print('Done!')
#         else:
#             print("The spell was too weak.")
#
# # ------------------------------------------------------------------------------------
#
#     elif action == 'Divination':
#         substring1 = explode[1]
#         substring2 = explode[2]
#
#         if substring1 in spell:
#             temp = spell.replace(substring1, substring2)
#             spell = temp
#             print(spell)
#
#     elif action == 'Alteration':
#         substring = explode[1]
#
#         if substring in spell:
#             temp = spell.replace(substring, '')
#             spell = temp
#             print(spell)
#
#     else:
#         print("The spell did not work!")
#
#     command = input()

# 2
# import re
# number = int(input())
# pattern = r'(?P<g1>.+)>(?P<g2>[0-9]{3})\|(?P<g3>[a-z]{3})\|(?P<g4>[A-Z]{3})\|(?P<g5>[^<>]{3})<(?P<g6>\1)'
#
# for i in range(number):
#     password = input()
#
#     matches = re.match(pattern, password)
#
#     if matches is None:
#         print("Try another password!")
#     else:
#         new = re.finditer(pattern, password)
#         encode = ''
#         for j in new:
#
#             encode += j.group('g2')
#             encode += j.group('g3')
#             encode += j.group('g4')
#             encode += j.group('g5')
#
#         print(f"Password: {encode}")

# 3
# messages = {}
# capacity_per_user = int(input())
#
# # {'name': {'sent': 4, 'received': 7}}
#
# command = input()
# while command != 'Statistics':
#     explode = command.split('=')
#     action = explode[0]
#
#     if action == 'Add':
#         username = explode[1]
#         sent = int(explode[2])
#         received = int(explode[3])
#
#         if username not in messages.keys():
#             messages[username] = {'sent': sent, 'received': received}
#         else:
#             pass
#
#     elif action == 'Message':
#         sender = explode[1]
#         receiver = explode[2]
#
#         if sender in messages.keys() and receiver in messages.keys():
#
#             messages[sender]['sent'] += 1
#             if messages[sender]['sent'] + messages[sender]['received'] >= capacity_per_user:
#                 print(f"{sender} reached the capacity!")
#                 messages.pop(sender)
#
#             messages[receiver]['received'] += 1
#             if messages[receiver]['sent'] + messages[receiver]['received'] >= capacity_per_user:
#                 print(f"{receiver} reached the capacity!")
#                 messages.pop(receiver)
#
#     elif action == 'Empty':
#         removed = explode[1]
#
#         if removed == 'All':
#             messages.clear()
#         else:
#             messages.pop(removed)
#
#     command = input()
#
# count = 0
#
# for i in messages.keys():
#     count += 1
# print(f"Users count: {count}")
#
# for j in messages.keys():
#     total = messages[j]['sent'] + messages[j]['received']
#     print(f'{j} - {total}')

#----------------------------------------------------------------------------


# x = lambda a: a ** 3
# print(x(2))




