

#built-in funkcii
# print()
# type()
# input()
# abs()
# pow()
# dir()
# sorted()
# max()


#1
# def function(a, b, c):
#     return min(a, b, c)
#
#
# print(function(int(input()), int(input()), int(input())))

#2a
# def sum_numbers(a, b):
#     return a + b
#
#
# def subtract(num1, num2, num3):
#     return sum_numbers(num1, num2) - num3
#
#
# number1 = int(input())
# number2 = int(input())
# number3 = int(input())
# result = subtract(number1, number2, number3)
# print(result)

#2b
# def sum_numbers(a, b):
#     return a + b
#
#
# def subtract(current_sum, c):
#     return current_sum - c
#
#
# a, b, c = int(input()), int(input()), int(input())
# result = subtract(sum_numbers(a, b), c)
# print(result)

#3
# def function(a, b):
#     for i in range(ord(a)+1, ord(b)):
#         print(chr(i), end=' ')
#
#
# function(input(), input())

#4
# def function(a):
#     odd_sum = 0
#     even_sum = 0
#     for index, digit in enumerate(a):
#         if int(digit) % 2 != 0:
#             odd_sum += int(digit)
#         else:
#             even_sum += int(digit)
#     print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")
#
#
# number = input()
# function(number)

#5a
# def function(a):
#     copy_numbers = list(map(int, a))
#     only_even = []
#     for i in copy_numbers:
#         if i % 2 == 0:
#             only_even.append(i)
#     return only_even
#
#
# numbers = input().split(' ')
# print(function(numbers))

#5b kekw
# result = list(filter(lambda x: x % 2 == 0, list(map(int, input().split(' ')))))
# print(result)

#6a
# def function(a):
#     sorted_list = []
#     for i in range(len(a)):
#         sorted_list.append(min(a))
#         a.remove(min(a))
#     return sorted_list
#
#
# my_list = list(map(int, input().split(' ')))
# print(function(my_list))

#6b kekw
#result = sorted(list(map(int, input().split(' '))))

#7
# def printmin(a):
#     print(f"The minimum number is {min(a)}")
#
#
# def printmax(b):
#     print(f"The maximum number is {max(b)}")
#
#
# def printsum(c):
#     print(f"The sum number is: {sum(c)}")
#
#
# numbers = list(map(int, input().split(' ')))
# printmin(numbers)
# printmax(numbers)
# printsum(numbers)

#8a
# def check_palindrome(a):
#     for i in a:
#         normal_number = i
#         reverse_number = ''
#         for j in range(len(i)-1, -1, -1):
#             reverse_number += i[j]
#         if normal_number == reverse_number:
#             print(True)
#         else:
#             print(False)
#
#
# my_list = input().split(', ')
# check_palindrome(my_list)

#8b
# def palindrome_func(nums):
#
#     for num in nums:
#         if num == num[::-1]:
#             print('True')
#         else:
#             print('False')
#
#
# numbers = input().split(', ')
# palindrome_func(numbers)

#9 sam
# def check_password(a):
#
#     is_valid = True
#     counter = 0
#
#     if len(a) < 6 or len(a) > 10:
#         print("Password must be between 6 and 10 characters")
#         is_valid = False
#     #letters: 65 - 90 and 97 - 122, digits: 48 - 57
#
#     for i in a:
#         if (48 <= ord(i) <= 57) or (65 <= ord(i) <= 90) or (97 <= ord(i) <= 122):
#             pass
#         else:
#             print("Password must consist only of letters and digits")
#             is_valid = False
#             break
#
#     for j in a:
#         if 48 <= ord(j) <= 57:
#             counter += 1
#
#     if counter < 2:
#         print("Password must have at least 2 digits")
#         is_valid = False
#
#     if is_valid:
#         print("Password is valid")
#
#
# password = input()
# check_password(password)

#10 sam
# def function(a):
#     my_sum = 0
#     for i in range(a, 0, -1):
#         if a % i == 0:
#             my_sum += i
#     if (my_sum / 2) == a:
#         print("We have a perfect number!")
#     else:
#         print("It's not so perfect.")
#
#
# number = int(input())
# function(number)

#11a
# def function(a):
#     counter = 0
#     while a > 1:
#         counter += 1
#         a -= 10
#
#     dots = 10 - counter
#
#     if counter < 10:
#         print(f'{counter * 10}% [', end='')
#         for i in range(counter):
#             print('%', end='')
#         for j in range(dots):
#             print('.', end='')
#         print(']')
#         print('Still loading...')
#     else:
#         print(f'{counter * 10}% Complete!')
#         print('[', end='')
#         for k in range(10):
#             print('%', end='')
#         print(']')
#
#
# progress = int(input())
# function(progress)

#12a
# def function(a, b):
#     factorial1 = 1
#     factorial2 = 1
#     result = 0
#
#     for i in range(a, 0, -1):
#         factorial1 *= i
#
#     for j in range(b, 0, -1):
#         factorial2 *= j
#
#     result = factorial1 / factorial2
#     print(f"{result:.2f}")
#
#
# number1 = int(input())
# number2 = int(input())
# function(number1, number2)

#12b rekursiq
# def factorial(num):
#     return 1 if num == 0 or num == 1 else num * (factorial(num-1))
#
## factorial(3)            #1st call with 3
## 3 * factorial(2)        #2nd call with 2
## 3 * 2 * factorial(1)    #3rd call with 1
## 3 * 2 * 1               #return from 3rd call as number=1
## 3 * 2                   #return from 2nd call
## 6                       #return from 1st call
