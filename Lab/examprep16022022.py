#1-1

# total = 0
# is_special = False
#
# while 1:
#     command = input()
#     if command == 'special':
#         is_special = True
#         break
#     elif command == 'regular':
#         break
#     else:
#         current_part_price = float(command)
#         if current_part_price <= 0:
#             print("Invalid price!")
#             continue
#         total += current_part_price
#
# tax = total * 0.2
# total_no_tax = total
# total += tax
#
# if is_special:
#     total -= total * 0.1
#
# if total == 0:
#     print("Invalid order!")
# else:
#     print("Congratulations you've just bought a new computer!")
#     print(f"Price without taxes: {total_no_tax:.2f}$")
#     print(f"Taxes: {tax:.2f}$")
#     print("-----------")
#     print(f"Total price: {total:.2f}$")

#2-2
# numbers = list(map(int, input().split(' ')))
# command = input()
# while command != 'end':
#     explode = command.split(' ')
#     operation = explode[0]
#
#     if operation == 'swap':
#         index1 = int(explode[1])
#         index2 = int(explode[2])
#         numbers[index2], numbers[index1] = numbers[index1], numbers[index2]
#
#     elif operation == 'multiply':
#         index1 = int(explode[1])
#         index2 = int(explode[2])
#         numbers[index1] *= numbers[index2]
#
#     elif operation == 'decrease':
#         for i in range(len(numbers)):
#             numbers[i] -= 1
#
#     command = input()
#
# output = list(map(str, numbers))
# print(', '.join(output))

#1-2 Da Lift
# people = int(input())
# lift = [int(cart) for cart in input().split(" ")]
#
# for i in range(len(lift)):
#     can_load = min(4 - lift[i], people)
#     lift[i] += can_load
#     people -= can_load
#
# if people > 0:
#     print(f"There isn't enough space! {people} people in a queue!")
# elif len([cart for cart in lift if cart < 4]) > 0:
#     print("The lift has empty spots!")
#
# print(" ".join([str(cart) for cart in lift]))






