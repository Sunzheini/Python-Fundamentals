# from math import ceil, floor
# from turtle import *   # == import all
# import sys

#a = int(input()) # by default input is string!
# outfit = ''
# largest_number = -sys.maxsize
# smallest_number = sys.maxsize

# age =! Age =! AGE - # python is case sensitive
# don't use firstName with capital N like other languages

# noob = first_name + last_name + str(age)
# age is str because contatenation must be done in string format

# # # zakryglqne do 2 znaka sled desetichniq znak
# print(round(45.97777, 2))

# i = a // 4
# (num1 ** 10) # na deceta stepen

# if day_of_week in 'Mo Tu We Th Fr':
# if type_of_animal == 'dog' or 'cat' or 'fish':
# if -100 <= number <= 100 and number != 0:

# if number % 10 == 7: # zavyrshva na 7
# if counter % 3 == 0: # vseki 3ti den

#     if total_points > 1250.5:
#         break

# za da napravim for cikyl ni trqbva predv broqt iteracii!
# for num in range(10, 1, -1):  # nachalo, krai i kakvo da pravi na vsqka st.
# stypkata e samo s celi chisla
# first_name = input()
# for i in first_name:
#     print(i)
# print(first_name[2])        # number of symbol from string

# while True:
    # break # prekysva samo cikyla v koito se namira.
        # t.e. ako e vlojen v drug prekysva samo po-dolniq

# line = input()
# while line != 'Stop':
#     print('Loop')
#     line = input()

# i = 0
# while i < 10:
#     if i % 2 == 0:
#         i += 1
#         continue
#     print(i)
#     i += 1

# moje while else in python samo

# coins_counter += sum // 200 # ako sum e < 200, propuskame reda

# print(len(text))               # dyljina na string
# print(chr(99)   # print 99 from ASCI

# print(end='') # na edin red printira vsichki iteracii na cikyla

# if i == number_of_floors:
#     print(f"L{i}{j} ", end='')
#     if j == rooms_per_floor - 1:
#         print()       # nov red

# chasovnik
# for h in range(0, 24):
#     for m in range(0, 60):
#         print(f"{h:02d}:{m:02d}")

# \n - print nov red

# counter = 1
# all_is_printed = False
# for row in range(1, n + 1):
#     for column in range(1, row + 1):
#         print(counter, end=' ')
#         counter += 1
#         if counter > n:
#             all_is_printed = True
#             break
#     if all_is_printed:
#         break
#     print()

# enumerate
# first_number = int(input())
# second_number = int(input())
# for current_number in range(first_number, second_number + 1):
#     odd_digits_sum = 0
#     even_digits_sum = 0
#     current_number_as_string = str(current_number)
#     for index, digit in enumerate(current_number_as_string):
#         if index % 2 == 0:
#             odd_digits_sum += int(digit)
#         else:
#             even_digits_sum += int(digit)
#     if odd_digits_sum == even_digits_sum:
#         print(current_number, end=' ')

# it_is_prime = True
#         for i in range(2, entry_as_number):
#             if entry_as_number % i == 0:
#                 it_is_prime = False
#                 break
#         if it_is_prime:
#             sum_of_prime += entry_as_number
#         else:
#             sum_of_nonprime += entry_as_number

# n = int(input())
# for i in range(1111, 9999 + 1):
#     i_as_string = str(i)
#     number_is_special = True
#     for j in i_as_string:
#         if int(j) == 0 or n % int(j) != 0: # predotvratqva delenie na 0
#             number_is_special = False
#             break
#     if number_is_special:
#         print(i, end=' ')

# print(ord("D")) # printira 68 (ASCI)
# print(chr(68)) # printira D (ASCI)

# barcode generator
# beginning = input()
# ending = input()
# for i in range(int(beginning[0]), int(ending[0]) + 1):
#     for j in range(int(beginning[1]), int(ending[1]) + 1):
#         for k in range(int(beginning[2]), int(ending[2]) + 1):
#             for m in range(int(beginning[3]), int(ending[3]) + 1):
#                 if i % 2 != 0 and j % 2 != 0 and k % 2 != 0 and m % 2 != 0:
#                     print(f"{i}{j}{k}{m}", end=' ')

# text = input()
# reversed_word = ''
# for i in range(len(text)-1, -1, -1):
#     reversed_word += text[i]
# print(reversed_word)
#
#slice notation
# first_string = input()
# second_string = input()
# for i in range(len(first_string)):
#     if first_string[i] != second_string[i]:
#         different_letter = second_string[i]
#         temp_word = first_string[0:i] + different_letter + first_string[i + 1:]
#         first_string = temp_word
#         print(first_string)

# a[start:stop]  # items start through stop-1
# a[start:]      # items start through the rest of the array
# a[:stop]       # items from the beginning through stop-1
# a[:]           # a copy of the whole array
# a[-1]    # last item in the array
# a[-2:]   # last two items in the array
# a[:-2]   # everything except the last two items
# a[::-1]    # all items in the array, reversed
# a[1::-1]   # the first two items, reversed
# a[:-3:-1]  # the last two items, reversed
# a[-3::-1]  # everything except the last two items, reversed


#print(bool(10 > 9)) #printira True kato print(10 > 9)

#'a' in 'abc' #True

#number = None #tova e "nishto"

#x = 0 ; x = - 0 ; x = '' ; x = False ; x = None # vsicho dava False na bool(x)

# check sum of digits of number
# number = int(input())
# for i in range(1, number+1):
#     working_number = i
#     sum = 0
#     while(working_number > 0):
#         sum += working_number % 10
#         working_number = int(working_number/10)
#     if sum == 5 or sum == 7 or sum == 11:
#         print(f"{i} -> True")
#     else:
#         print(f"{i} -> False")

# is_special = sum == 5 or sum == 7 or sum == 11


#       while s boolean; set; using boolean; print without if
# year = int(input())
# is_year_happy = False
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
# print(year)


#       use of end=''
# for i in range(beginning, ending+1):
#     print(chr(i), end=' ..<>.. ')

#       triplet char iteration
# number = int(input())
# for i in range(0, number):
#     for j in range(0, number):
#         for k in range(0, number):
#             print(f"{chr(97+i)}{chr(97+j)}{chr(97+k)}")


#print(eval(command))

#rev string
# rev_word = reversed(word)

#if j.isdigit():

#built-in funkcii
# print()
# type()
# input()
# abs()
# pow()
# dir()
# sorted()
# max()

#LISTS
#-----------------------------------------------------------------------#

#list_example = list() ili list1 = []
#ili my_list = [input(), input(), input()]
# print(list_example[1])

#syzdavane na spisyk s nuli
# for i in range(beggars):
#     beggars_income.append(0)
##syshtoto e beggars_income = [0] * beggars

#splitva po neshto stringa v spisyk
# alphabet = input().split(', ')
# print(alphabet)

#joinva po neshto spisyka v string
# alphabet = input().split(', ')
# print('--'.join(alphabet))
# print('\n'.join(chat_log))

#access ot zad na pred
# my_pets = ("cat", "dog", "parrot")
# print(my_pets[-1]) #parrot
# print(my_pets[-2]) #dog

#reverse elements
#meerkat[0], meerkat[2] = meerkat[2], meerkat[0]

#swap s index
# i = ['one', 'two', 'three', 'four']
# a, b = i.index('two'), i.index('three')
# i[b], i[a] = i[a], i[b]
# print(i)

# for element in my_list:
#     print(element)
# ili
# for i in range(len(my_list)):
#     print(my_list[i])
# ili
# while i < len(my_list):
#     print(my_list[i])
#     i += 1
# ili
# while my_list:
#     print(my_list[0])
#     current_element = my_list[0]
#     my_list.remove(current_element)

#if 3 not in my_list:

#list methods:
# append - dobavqme element kym kraq na spisyka - deck2.append(cards[j])
# clear - result.clear()
# copy
# count #broim kolko pyti se sreshta neshto v lista
# extend #moje da zakachi nov spisyk kym kraq na presishniq
# index #vryshta pyrvoto mqsto na koeto se namira neshto
# insert - fruits.insert(2, 'noob')
# pop / pop(#position) - target_list.pop(index)
# remove - maha konkreten element - numbers.remove(str(currentminelement))
# reverse #pravi obraten spisyk - list_of_coffees.reverse()
# sorted

#po dobre ot zad na pred pop
#for i in range(len(target_list)-1, -1, -1):
#                     if strike_range_start <= i <= strike_range_stop:
#                         target_list.pop(i)

# sorted_names = sorted(names)
# sorted_names = sorted(sorted_names, key=lambda name: -len(name))

#filter
# numbers_list = [1, 2, 3, 4, 5, 6]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers_list))
# test = list(filter(lambda x: x % 2 == 0, map(int, input().split(', '))))

#concatenate lists with +
#use set() to extract unique values only

# for j in range(len(donations)):
#     beggars_income[counter] += int(donations[j])
#     counter += 1
#     if counter >= beggars:
#         counter = 0

#currentminelement = min(copy_numbers)

#map
# copy_numbers = list(map(int, numbers))
# doubled_list = list(map(lambda x: x*2, numbers_list))

#explode = ..
#breakdown_command = command.split(' ')
#         breakdown_type = breakdown_command[0]
#         breakdown_product = breakdown_command[1]

#COMPREHENSION
#-----------------------------------------------------------------------#

# num_list = [i for i in range(5)]
# new_list = [i**2 for i in old_list if i > 3]
# new_list = [i**2 if i > 3 else i * 2 for i in old_list]

# lift = [int(cart) for cart in input().split(" ")]

# vowels = ['a', 'o', 'u', 'e', 'i']
# no_vowels = [i for i in input_text if i not in vowels]

#prazen list ot stringove
# schedule = ["" for i in range(11)]

#vlojen cikyl
# test = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]


#FUNCTIONS
#-----------------------------------------------------------------------#

# def calc(operator, number1, number2):
#     if operator == "multiply":
#         return number1 * number2
#     elif operator == "divide":
#         return int(number1 / number2)

# default argument
# def names(first = 'Daniel', last = 'Zorov'):
#     print(first, last)

# position of arguments
# def area(width, height):
#     return width * height
#
# print(area(height=3, width=2))

# lambda
#definirame i izpolzvame vednaga
# x = lambda a: a + 10 #pri parametyr a vryshta return a + 10
# print(x(5))

# full_name = lambda first, last: f'I am {first} {last}'
# print(full_name('Daniel', 'Zorov'))

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

#Classes and Functions
#-----------------------------------------------------------------------#






#NEW
#-----------------------------------------------------------------------#



