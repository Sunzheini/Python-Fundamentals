
#1
# first = int(input())
# second = int(input())
# third = int(input())
# fourth = int(input())
#
# result = int((first + second) / third) * fourth
#
# print(result)

#2
# first = input()
# second = input()
# third = input()
# astring = first + second + third
# print(astring)

#3
# people = int(input())
# capacity = int(input())
# courses = 0
#
# while people > 0:
#         courses += 1
#         people -= capacity
# print(courses)

#4
# number_of_chars = int(input())
# sum = 0
# for i in range(number_of_chars):
#     current_char = input()
#     sum += ord(current_char)
# print(f"The sum equals: {sum}")

#5
# beginning = int(input())
# ending = int(input())
#
# for i in range(beginning, ending+1):
#     print(chr(i), end=' ')

#6
# number = int(input())
# for i in range(0, number):
#     for j in range(0, number):
#         for k in range(0, number):
#             print(f"{chr(97+i)}{chr(97+j)}{chr(97+k)}")

#7
# capacity = 255
# liters_held = 0
# number_of_lines = int(input())
# for i in range(number_of_lines):
#     input_liters = int(input())
#     if (liters_held + input_liters) > capacity:
#         print("Insufficient capacity!")
#     else:
#         liters_held += input_liters
# print(liters_held)

#8
# group_size = int(input())
# days_adventure = int(input())
# gold = 0
#
# for i in range(1, days_adventure+1):
#
#     if i % 10 == 0:
#         group_size -= 2
#
#     if i % 15 == 0:
#         group_size += 5
#
#     gold += 50
#     gold -= (group_size * 2)
#
#     if i % 3 == 0:
#         gold -= (group_size * 3)
#
#     if i % 5 == 0:
#         gold += (group_size * 20)
#         if i % 3 == 0:
#             gold -= (group_size * 2)
#
# average = gold // group_size
# print(f"{group_size} companions received {average} coins each.")


#9
# number_of_snowballs = int(input())
# best_weight = 0
# best_speed = 0
# best_quality = 0
# best_value = 0
# for i in range(number_of_snowballs):
#     current_weight = int(input())
#     current_speed = int(input())
#     current_quality = int(input())
#     current_value = (current_weight / current_speed) ** current_quality
#     if current_value >= best_value:
#         best_weight = current_weight
#         best_speed = current_speed
#         best_quality = current_quality
#         best_value = current_value
# print(f"{best_weight} : {best_speed} = {int(best_value)} ({best_quality})")

#10
# lost_fights_count = int(input())
# helmet_repair_cost = float(input())
# sword_repair_cost = float(input())
# shield_repair_cost = float(input())
# armor_repair_cost = float(input())
# shield_break_counter = 0
# total = 0
#
# for i in range(1, lost_fights_count+1):
#     if i % 2 == 0:
#         total += helmet_repair_cost
#     if i % 3 == 0:
#         total += sword_repair_cost
#         if i % 2 == 0:
#             total += shield_repair_cost
#             shield_break_counter += 1
#             if shield_break_counter % 2 == 0:
#                 total += armor_repair_cost
#
# print(f"Gladiator expenses: {total:.2f} aureus")











