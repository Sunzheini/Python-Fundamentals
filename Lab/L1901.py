
#1
# name1 = input()
# name2 = input()
# delimiter = input()
# print(f"{name1}{delimiter}{name2}")

#2
# centuries = int(input())
#
# years = centuries * 100
# days = int(years * 365.2422)
# hours = days * 24
# minutes = hours * 60
#
# print(f"{centuries} centuries = {years} years = {days} "
#       f"days = {hours} hours = {minutes} minutes")

#3a
# number = int(input())
# for i in range(1, number+1):
#     number_as_string = str(i)
#     sum = 0
#     for j in range(len(number_as_string)):
#         temp2 = int(number_as_string[j])
#         sum += temp2
#     if sum == 5 or sum == 7 or sum == 11:
#         print(f"{number_as_string} -> True")
#     else:
#         print(f"{number_as_string} -> False")

#3b
# number = int(input())
# for i in range(1, number+1):
#     working_number = i
#     sum = 0
#
#     while(working_number > 0):
#         sum += working_number % 10
#         working_number = int(working_number/10)
#
#     if sum == 5 or sum == 7 or sum == 11:
#         print(f"{i} -> True")
#     else:
#         print(f"{i} -> False")

#4
# meters = int(input())
# kilometers = meters / 1000
# print(f"{kilometers:.2f}")

#5
# pounds = int(input())
# dollars = pounds * 1.31
# print(f"{dollars:.3f}")

#6
# year = int(input())
#
# is_year_happy = False
#
# while not is_year_happy:
#     year += 1
#     str_year = str(year)
#
#     set_year = set()
#     for i in range(len(str_year)):
#         set_year.add(str_year[i])
#     #ili set_year = set(str_year)
#
#     is_year_happy = len(str_year) == len(set_year)
#
# print(year)














