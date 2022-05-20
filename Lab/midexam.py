# 1
# biscuits_worker_day = int(input())
# number_of_workers = int(input())
# competitor_30_days = int(input())
#
# biscuits_30_days = 0
# difference_to_competitor = 0
#
# for i in range(1, 31):
#     if i % 3 == 0:
#         biscuits_30_days += int((biscuits_worker_day * number_of_workers) * 0.75)
#     else:
#         biscuits_30_days += biscuits_worker_day * number_of_workers
#
# print(f"You have produced {biscuits_30_days} biscuits for the past month.")
#
# if biscuits_30_days > competitor_30_days:
#     difference_to_competitor = (biscuits_30_days - competitor_30_days) / competitor_30_days * 100
#     print(f"You produce {difference_to_competitor:.2f} percent more biscuits.")
# elif biscuits_30_days < competitor_30_days:
#     difference_to_competitor = (competitor_30_days - biscuits_30_days) / competitor_30_days * 100
#     print(f"You produce {difference_to_competitor:.2f} percent less biscuits.")

# 2
# list_of_coffees = input().split(' ')
# number_of_commands = int(input())
#
# for i in range(number_of_commands):
#     command = input()
#     explode = command.split(' ')
#     action = explode[0]
#
#     if action == 'Include':
#         item1 = explode[1]
#         list_of_coffees.append(item1)
#
#     elif action == 'Remove':
#         item1 = explode[1]
#         item2 = int(explode[2])
#
#         if item2 > len(list_of_coffees):
#             continue
#         else:
#             if item1 == 'first':
#                 for j in range(item2):
#                     list_of_coffees.pop(0)
#             elif item1 == 'last':
#                 for j in range(item2):
#                     list_of_coffees.pop()
#
#     elif action == 'Prefer':
#         item1 = int(explode[1])
#         item2 = int(explode[2])
#
#         if 0 <= item1 < len(list_of_coffees):
#             if 0 <= item2 < len(list_of_coffees):
#                 list_of_coffees[item1], list_of_coffees[item2] = list_of_coffees[item2], list_of_coffees[item1]
#         else:
#             continue
#
#     elif action == 'Reverse':
#         list_of_coffees.reverse()
#
# print("Coffees:")
# print(' '.join(list_of_coffees))

# 3
# chat_log = []
# command = input()
#
# while command != 'end':
#     explode = command.split(' ')
#     action = explode[0]
#
#     if action == 'Chat':
#         item1 = explode[1]
#         chat_log.append(item1)
#
#     elif action == 'Delete':
#         item1 = explode[1]
#         if item1 in chat_log:
#             chat_log.remove(item1)
#
#     elif action == 'Edit':
#         item1 = explode[1]
#         item2 = explode[2]
#         if item1 in chat_log:
#             my_index = chat_log.index(item1)
#             chat_log[my_index] = item2
#
#     elif action == 'Pin':
#         item1 = explode[1]
#         if item1 in chat_log:
#             chat_log.remove(item1)
#             chat_log.append(item1)
#
#     elif action == 'Spam':
#         for i in range(1, len(explode)):
#             chat_log.append(explode[i])
#
#     command = input()
#
# print('\n'.join(chat_log))








