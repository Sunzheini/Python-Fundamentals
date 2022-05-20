# 1
# my_list = input().split(' ')
# new = []
# for i in my_list:
#     current = abs(float(i))
#     new.append(current)
# print(new)

# 2a
# def calc(grade):
#     if 2.00 <= grade <= 2.99:
#         print('Fail')
#     elif 3.00 <= grade <= 3.49:
#         print('Poor')
#     elif 3.50 <= grade <= 4.49:
#         print('Good')
#     elif 4.50 <= grade <= 5.49:
#         print('Very Good')
#     elif 5.50 <= grade <= 6.00:
#         print('Excellent')
#
#
# calc(float(input()))

# 2b
# def calc(grade):
#     if 2.00 <= grade <= 2.99:
#         return 'Fail'
#     elif 3.00 <= grade <= 3.49:
#         return 'Poor'
#     elif 3.50 <= grade <= 4.49:
#         return 'Good'
#     elif 4.50 <= grade <= 5.49:
#         return 'Very Good'
#     elif 5.50 <= grade <= 6.00:
#         return 'Excellent'
#
#
# print(calc(float(input())))


# default argument
# def names(first = 'Daniel', last = 'Zorov'):
#     print(first, last)
#
#
# names('baba', 'marta')

# position of arguments
# def area(width, height):
#     return width * height
#
#
# print(area(height=3, width=2))


# 3
# def calc(operator, number1, number2):
#     if operator == "multiply":
#         return number1 * number2
#     elif operator == "divide":
#         return int(number1 / number2)
#     elif operator == "add":
#         return number1 + number2
#     elif operator == "subtract":
#         return number1 - number2
#
#
# print(calc(input(), int(input()), int(input())))


# lambda
#definirame i izpolzvame vednaga
# x = lambda a: a + 10 #pri parametyr a vryshta return a + 10
# print(x(5))

# full_name = lambda first, last: f'I am {first} {last}'
# print(full_name('Daniel', 'Zorov'))

# plus_five = lambda a: a + 5
# print(plus_five(9))

# swap
# def swap(a, b):
#     a = a + b
#     b = a - b
#     a = a - b
#     return a, b
#
# print(swap(int(input()), int(input())))


#4a
# def function(string, counter):
#     current_string = ''
#     current_string = string * counter
#     return current_string
#
#
# print(function(input(), int(input())))

#4b
# result = lambda string, counter: string * counter
# print(result(input(), int(input())))

#5
# def function(product, quantity):
#     if product == "coffee":
#         return quantity * 1.50
#     elif product == "water":
#         return quantity * 1.00
#     elif product == "coke":
#         return quantity * 1.40
#     elif product == "snacks":
#         return quantity * 2.00
#
#
# print(f"{function(input(), int(input())):.2f}")

#6a
# def function(width, height):
#     return width * height
#
#
# print(function(int(input()), int(input())))

#6b
# area = lambda width, height: width * height
# print(area(int(input()), int(input())))

#7
# def function(my_list):
#     rounded_list = []
#     for i in my_list:
#         current_number = round(float(i))
#         rounded_list.append(current_number)
#     return rounded_list
#
#
# new_list = input().split(' ')
# print(function(new_list))







