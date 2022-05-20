#list methods:
# append
# clear
# copy
# count #broim kolko pyti se sreshta neshto v lista
# extend #moje da zakachi nov spisyk kym kraq na presishniq
# index #vryshta pyrvoto mqsto na koeto se namira neshto
# insert
# pop / pop(#position)
# remove
# reverse #pravi obraten spisyk
# sort

#insert
# fruits = ['apple', 'banana', 'cherry']
# fruits.insert(2, 'noob')
# print(fruits)

#vryshta poziciite kydeto ima syvpadneie
# fruits = ['apple', 'banana', 'cherry', 'apple']
# index = (i for i, value in enumerate(fruits) if value == 'apple')
# print(list(index))

#syzdava list s range
# numbers = list(range(0, 100, 10))
# print(numbers)

#splitva po neshto stringa v spisyk
# alphabet = input().split(', ')
# print(alphabet)

#joinva po neshto spisyka v string
# alphabet = input().split(', ')
# print('--'.join(alphabet))



#1a
# my_list = input().split(" ")
#
# new_list = []
# for i in my_list:
#     if int(i) > 0:
#         new_list.append(-int(i))
#     elif int(i) < 0:
#         new_list.append(abs(int(i)))
#     else:
#         new_list.append(0)
# print(new_list)

#1b
# my_list = [-i if i > 0 else abs(i) for i in list(map(int, input().split(' ')))]
# print(my_list)

#2
# factor = int(input())
# count = int(input())
# number = factor
# my_list = []
# for i in range(count):
#     my_list.append(number)
#     number += factor
# print(my_list)

#3
# team_a = list(range(1, 12))
# team_b = list(range(1, 12))
# sequence_list = input().split(' ')
# terminated = False
#
# for i in range(len(sequence_list)):
#     current_card = sequence_list[i]
#     current_team = current_card[0:1]
#     current_player = int(current_card[2:])
#
#     if current_team == "A":
#         if current_player in team_a:
#             team_a.remove(current_player)
#     elif current_team == "B":
#         if current_player in team_b:
#             team_b.remove(current_player)
#
#     if len(team_a) < 7 or len(team_b) < 7:
#         terminated = True
#         break
#
# print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
#
# if terminated:
#     print("Game was terminated")

#4
# donations = input().split(', ')
# beggars = int(input())
# beggars_income = []
# counter = 0
# for i in range(beggars):
#     beggars_income.append(0)
##syshtoto e beggars_income = [0] * beggars
#
# for j in range(len(donations)):
#     beggars_income[counter] += int(donations[j])
#     counter += 1
#     if counter >= beggars:
#         counter = 0
#
# print(beggars_income)

#5
# cards = input().split(' ')
# shuffles = int(input())
# deck1 = []
# deck2 = []
# result = []
#
# for num in range(shuffles):
#
#     result.clear()
#     deck1.clear()
#     deck2.clear()
#     counter = 0
#
#     for i in range(int(len(cards)/2)):
#         deck1.append(cards[i])
#     for j in range(int(len(cards)/2), len(cards)):
#         deck2.append(cards[j])
#     for k in range(int(len(cards)/2)):
#         result.append(deck1[counter])
#         result.append(deck2[counter])
#         counter += 1
#
#     cards = result.copy()
#
# print(result)

#6
# numbers = input().split(' ')
# remove = int(input())
#
# copy_numbers = list(map(int, numbers))
#
# for i in range(remove):
#     currentminelement = min(copy_numbers)
#     numbers.remove(str(currentminelement))
#     copy_numbers.remove(currentminelement)
#
# print(', '.join(numbers))

#7
# gifts = input().split(' ')
#
# while 1:
#     command = input()
#     if command == "No Money":
#         break
#     else:
#         breakdown_command = command.split(' ')
#         breakdown_type = breakdown_command[0]
#         breakdown_product = breakdown_command[1]
#
#         if breakdown_type == "OutOfStock":
#             for i in range(len(gifts)):
#                 if gifts[i] == breakdown_product:
#                     gifts[i] = "None"
#
#         elif breakdown_type == "Required":
#             index = int(breakdown_command[2])
#             if 0 < index < len(gifts):
#                 gifts[index] = breakdown_product
#
#         elif breakdown_type == "JustInCase":
#             gifts[-1] = breakdown_product
#
# for j in range(len(gifts)-1, -1, -1):
#     if gifts[j] == "None":
#         gifts.pop(j)
#
# print(' '.join(gifts))

#8a
# information = input().split('#')
# water = int(input())
# effort = 0
# total = 0
#
# print("Cells:")
#
# for i in information:
#     current_info = i.split(' = ')
#     current_type = current_info[0]
#     current_rating = current_info[1]
#
#     if current_type == "High" and 81 <= int(current_rating) <= 125:
#         if water >= int(current_rating):
#             water -= int(current_rating)
#             effort += int(current_rating) / 4
#             total += int(current_rating)
#             print(f" - {current_rating}")
#     elif current_type == "Medium" and 51 <= int(current_rating) <= 80:
#         if water >= int(current_rating):
#             water -= int(current_rating)
#             effort += int(current_rating) / 4
#             total += int(current_rating)
#             print(f" - {current_rating}")
#     elif current_type == "Low" and 1 <= int(current_rating) <= 50:
#         if water >= int(current_rating):
#             water -= int(current_rating)
#             effort += int(current_rating) / 4
#             total += int(current_rating)
#             print(f" - {current_rating}")
#
# print(f"Effort: {effort:.2f}")
# print(f"Total Fire: {total}")

#9
# information = input().split('|')
# budget = int(input())
#
# spent = 0
# bought_items = []
#
# for i in information:
#     current_info = i.split('->')
#     current_item = current_info[0]
#     current_price = float(current_info[1])
#
#     if current_item == "Clothes" and current_price <= 50.00:
#         if budget >= current_price:
#             budget -= current_price
#             spent += current_price
#             bought_items.append(current_price + current_price * 0.4)
#     elif current_item == "Shoes" and current_price <= 35.00:
#         if budget >= current_price:
#             budget -= current_price
#             spent += current_price
#             bought_items.append(current_price + current_price * 0.4)
#     elif current_item == "Accessories" and current_price <= 20.50:
#         if budget >= current_price:
#             budget -= current_price
#             spent += current_price
#             bought_items.append(current_price + current_price * 0.4)
#
# for j in bought_items:
#     print(f"{j:.2f}", end=' ')
#
# print()
#
# print(f"Profit: {(spent * 0.4):.2f}")
# budget += spent + spent * 0.4
#
# if budget >= 150:
#     print("Hello, France!")
# else:
#     print("Not enough money.")

#10
# energy = 100
# coins = 100
#
# events = input().split('|')
# managed = True
#
# for i in events:
#     event_info = i.split('-')
#     event_name = event_info[0]
#     event_number = int(event_info[1])
#
#     if event_name == "rest":
#         if (energy + event_number) >= 100:
#             print(f"You gained {100 - energy} energy.")
#             energy = 100
#             print(f"Current energy: {energy}.")
#         elif (energy + event_number) < 100:
#             print(f"You gained {event_number} energy.")
#             energy += event_number
#             print(f"Current energy: {energy}.")
#
#     elif event_name == "order":
#         if energy >= 30:
#             coins += event_number
#             energy -= 30
#             print(f"You earned {event_number} coins.")
#         else:
#             energy += 50
#             print("You had to rest!")
#
#     else:
#         if coins >= event_number:
#             print(f"You bought {event_name}.")
#             coins -= event_number
#         else:
#             print(f"Closed! Cannot afford {event_name}.")
#             managed = False
#             break
#
# if managed:
#     print("Day completed!")
#     print(f"Coins: {coins}")
#     print(f"Energy: {energy}")

#more1
# command = input().split(', ')
# initial_length = len(command)
#
# for i in range(len(command)-1, -1, -1):
#     if int(command[i]) == 0:
#         command.pop(i)
#
# while len(command) < initial_length:
#     command.append('0')
#
# copy_command = list(map(int, command))
# print(copy_command)







































