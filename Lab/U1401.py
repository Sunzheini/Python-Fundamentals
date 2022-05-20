
#1
# name = input()
#
# if name == "Johnny":
#     print("Hello, my love!")
# else:
#     print(f"Hello, {name}!")

#2
# age = int(input())
# if age <= 14:
#     print("drink toddy")
# elif age <= 18:
#     print("drink coke")
# elif age <= 21:
#     print("drink beer")
# else:
#     print("drink whisky")

#3
# number = int(input())
# if number == 88:
#     print("Leo finally won the Oscar! Leo is happy")
# elif number == 86:
#     print("Not even for Wolf of Wall Street?!")
# elif number != 88 and number != 86 and number < 88:
#     print("When will you give Leo an Oscar?")
# else:
#     print("Leo got one already!")

#4
# a_string = input()
# b_string = ''
# for i in range(len(a_string)):
#     b_string += a_string[i]
#     b_string += a_string[i]
# print(b_string)

#5
# number = int(input())
# if number > 0:
#     for i in range(1, number+1):
#         print(f"{i} sheep...", end='')

#6
# number_of_orders = int(input())
# total_price = 0
# for i in range(number_of_orders):
#     price_per_capsule = float(input())
#     days = int(input())
#     capsules_count = int(input())
#     current_order_price = price_per_capsule * days * capsules_count
#     print(f"The price for the coffee is: ${current_order_price:.2f}")
#     total_price += current_order_price
# print(f"Total: ${total_price:.2f}")

#7a
# divisor = int(input())
# boundary = int(input())
# for i in range(boundary, 0, -1):
#     if i % divisor == 0:
#         print(i)
#         break

#7b
# divisor = int(input())
# boundary = int(input())
# print(int(boundary / divisor) * divisor)

#8
# first_string = input()
# second_string = input()
# for i in range(len(first_string)):
#     if first_string[i] != second_string[i]:
#         different_letter = second_string[i]
#         temp_word = first_string[0:i] + different_letter + first_string[i + 1:]
#         first_string = temp_word
#         print(first_string)

#9
# budget = float(input())
# price_kg_flour = float(input())
#
# price_pack_eggs = price_kg_flour * 0.75
# price_1l_milk = price_kg_flour + 0.25 * price_kg_flour
# price_250ml_milk = price_1l_milk / 4
# price_for_1_bread = price_pack_eggs + price_kg_flour + price_250ml_milk
#
# number_of_coloured_eggs = 0
# number_of_bread_loaves = 0
#
# while(1):
#    if budget >= price_for_1_bread:
#        number_of_bread_loaves += 1
#        number_of_coloured_eggs += 3
#        if number_of_bread_loaves % 3 == 0:
#            number_of_coloured_eggs -= (number_of_bread_loaves - 2)
#        budget -= price_for_1_bread
#    else:
#        break
#
# print(f"You made {number_of_bread_loaves} loaves of Easter bread! Now you "
#       f"have {number_of_coloured_eggs} eggs and {budget:.2f}BGN left.")

#10
# allowed_quantity = int(input())
# days_left = int(input())
# total_cost = 0
# spirit = 0
#
# for i in range(1, days_left+1):
#
#     if i % 11 == 0:
#         allowed_quantity += 2
#
#     if i % 2 == 0:
#         total_cost += allowed_quantity * 2
#         spirit += 5
#
#     if i % 3 == 0:
#         total_cost += allowed_quantity * 8
#         spirit += 13
#
#     if i % 5 == 0:
#         total_cost += allowed_quantity * 15
#         spirit += 17
#         if i % 3 == 0:
#             spirit += 30
#
#     if i % 10 == 0:
#         spirit -= 20
#         total_cost += 23
#
# if days_left % 10 == 0:
#     spirit -= 30
#
# print(f"Total cost: {total_cost}")
# print(f"Total spirit: {spirit}")