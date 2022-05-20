# 1
# tail = input()
# body = input()
# head = input()
#
# meerkat = [head, body, tail]
# print(meerkat)

#1b
# tail = input()
# body = input()
# head = input()
#
# meerkat = [tail, body, head]
#
# temp = meerkat[0]
# meerkat[0] = meerkat[2]
# meerkat[2] = temp
#
# print(meerkat)

#1c
# tail = input()
# body = input()
# head = input()
#
# meerkat = [tail, body, head]
#
# meerkat[0], meerkat[2] = meerkat[2], meerkat[0]
#
# print(meerkat)

#2
# number_of_courses = int(input())
# list_of_courses = []
# for i in range(number_of_courses):
#     list_of_courses.append(input())
# print(list_of_courses)

#3
# number = int(input())
# count_positives = 0
# sum_negatives = 0
# list_positives = []
# list_negatives = []
#
# for i in range(number):
#     current_number = int(input())
#     if current_number >= 0:
#         list_positives.append(current_number)
#         count_positives += 1
#     else:
#         list_negatives.append(current_number)
#         sum_negatives += current_number
#
# print(list_positives)
# print(list_negatives)
# print(f"Count of positives: {count_positives}")
# print(f"Sum of negatives: {sum_negatives}")

#4
# number = int(input())
# word = input()
# first_list = []
# second_list = []
#
# for i in range(number):
#     current_entry = input()
#     first_list.append(current_entry)
#     if word in current_entry:
#         second_list.append(current_entry)
#
# print(first_list)
# print(second_list)

#5
# number = int(input())
# my_list = []
#
# for i in range(number):
#     my_list.append(int(input()))
#
# command = input()
# filtered_list = []
#
# for i in range(len(my_list)):
#     if command == "even":
#         if my_list[i] % 2 == 0:
#             filtered_list.append(my_list[i])
#     elif command == "odd":
#         if my_list[i] % 2 != 0:
#             filtered_list.append(my_list[i])
#     elif command == "negative":
#         if my_list[i] < 0:
#             filtered_list.append(my_list[i])
#     elif command == "positive":
#         if my_list[i] >= 0:
#             filtered_list.append(my_list[i])
#
# print(filtered_list)

#5b
# number = int(input())
# even = []
# odd = []
# positive = []
# negative = []
#
# for i in range(number):
#     current_number = int(input())
#     if current_number % 2 == 0:
#         even.append(current_number)
#     elif current_number % 2 != 0:
#         odd.append(current_number)
#     elif current_number >= 0:
#         positive.append(current_number)
#     elif current_number < 0:
#         negative.append(current_number)
#
# command = input()
# print(eval(command))

















