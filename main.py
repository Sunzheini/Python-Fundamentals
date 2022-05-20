# import time
#
# from forex_python.converter import CurrencyRates
#
# c = CurrencyRates()
# amount = int(input('Enter the amount: '))
# from_currency = input('From Currency: ').upper()
# to_currency = input('To Currency: ').upper()
#
# print(amount, from_currency, '<--- To --->', to_currency)
#
# result = c.convert(from_currency, to_currency, amount)
#
# print(f"{result:.2f} {to_currency}")
# time.sleep(10)

#-----------------------------------------------------------#

# import time
#
# allowed_quantity = int(input("Enter allowed quantity: "))
# days_left = int(input("Enter days left: "))
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
# time.sleep(10)

#-----------------------------------------------------------#



# import time
#
# number = int(input("Enter a number: "))
# for i in range(1, number+1):
#     for j in range(0, i):
#         print("*", end='')
#     print()
# for i in range(number-1, 0, -1):
#     for j in range(0, i):
#         print("*", end='')
#     print()
# time.sleep(10)

#-------------------------------------------------------------#

import pyautogui
import time
import webbrowser

webbrowser.open("http://192.168.0.112/relay/0?turn=on")
time.sleep(1)
pyautogui.hotkey('ctrl', 'w')

#-------------------------------------------------------------#


