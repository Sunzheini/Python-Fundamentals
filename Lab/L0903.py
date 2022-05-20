# Text Processing

# python uses Unicode table
# string is a list of characters and are immutable

#multiline assignment
# a = """text
# textnew line
# text new line"""
# print(a)

#str(), split() - split bez parametri razdelq po neznacheshti simvoli (prazno mqsto napr)

#-------------------------------------------------------------------------------------

# 1
# command = input()
# while command != 'end':
#     new_text = command
#
#     #reversed_text = new_text[::-1]                   #method 1
#     #print(reversed_text)
#
#     # rev = reversed(new_text)
#     # reversed_text = ''
#     # for i in rev:
#     #     reversed_text += i
#     # print(reversed_text)                            #method 2
#
#     # rev = reversed(new_text)
#     # reversed_text = ''.join(rev)
#     # print(reversed_text)                            #method 3
#
#     rev = reversed(new_text)
#     reversed_text = ''.join(rev)
#     print(f'{new_text} = {reversed_text}')          #submitted to judge
#
#     command = input()

#-------------------------------------------------------------------------------------

#print(f"{''.join(text)}") # join moje taka - otvyn golemi kavichi a join s malki
#concatenate strings with +

# str1 = "red"
# str2 = str1 * 3 + 's'
# print(str2)         # prints redredreds


#Formatting
#like c
# str1 = "apples"
# str2 = "pears"
# str3 = "i love %s and %s" % (str1, str2)
# print(str3)

#with {}
# str1 = "apples"
# str2 = "pears"
# str3 = "i love {} and {}".format(str1, str2)
# print(str3)

#our way
# str1 = "apples"
# str2 = "pears"
# str3 = f"i love {str1} and {str2}"
# print(str3)


#slicing - can be used with strings and lists
#new_text = new[-5:]


#-------------------------------------------------------------------------------------
# 2
# command = input().split(' ')
# new_string = ''
# for i in range(len(command)):
#
#     new_string += command[i] * len(command[i])
#
# print(new_string)

#-------------------------------------------------------------------------------------
#string methods
#print('p'.isdigit())        #dava False
#print('P'.islower())        #dava false
#print('2'isalpha())        #proverqva dali e bukva
#print('2'isalnum())        #proverqva dali e bukva ili cifra

#print('Hello'.lower())

# print(" hello ".lstrip())       #maha praznite simvoli: prazno mqsto, tabluaciq i nov red
# print(" hello ".rstrip())
# print(" hello ".strip())


#replace
# txt = "I am Daniel"         #replace part of a string
# print(txt.replace("Daniel", "Maxi"))

# txt = "I am Daniel Daniel Daniel"
# print(txt.replace("Daniel", "Maxi", 2))

#-------------------------------------------------------------------------------------
# 3
# string_one = input()
# string_two = input()
#
# while string_one in string_two:
#     string_two = string_two.replace(string_one, '')
#
# print(string_two)

# 4
# banned = input().split(', ')
# txt = input()
#
# for i in banned:
#     new_symbol = len(i) * '*'
#     while i in txt:
#         txt = txt.replace(i, new_symbol)
#
# print(txt)

#5a
# command = input()
# digits = ''
# letters = ''
# special = ''
#
# for i in command:
#     if i.isdigit():
#         digits += i
#     elif i.islower() or i.isupper():
#         letters += i
#     else:
#         special += i
#
# print(digits)
# print(letters)
# print(special)

#5b
# command = input()
# digits = ''
# letters = ''
# special = ''
#
# for i in command:
#     if i.isdigit():
#         digits += i
#     elif i.isalpha():       #moje i taka
#         letters += i
#     else:
#         special += i
#
# print(digits)
# print(letters)
# print(special)

#ot 1.52h reshihme i edna zadacha za Dict dopylnitelno
#-------------------------------------------------------------------------------------

# validator = {}
# results = {}
#
# command = input()
# while command != 'end of contests':
#     explode = command.split(':')
#     contest = explode[0]
#     password = explode[1]
#
#     validator[contest] = password
#
#     command = input()
#
# command2 = input()
# while command2 != 'end of submissions':
#     explode = command2.split('=>')
#     contest = explode[0]
#     password = explode[1]
#     username = explode[2]
#     points = int(explode[3])
#
#     if contest in validator.keys():
#         if password == validator[contest]:
#             if username not in results.keys():
#                 results[username] = {}
#
#             if contest in results[username].keys():
#                 if points > results[username][contest]:
#                     results[username][contest] = points
#             else:
#                 results[username][contest] = points
#
#     command2 = input()
#
# best_sum = 0
# best_user = ''
#
# for i in results.keys():
#     current_user = i
#     current_sum = 0
#     for j in results[i].keys():
#         current_sum += results[i][j]
#     if current_sum > best_sum:
#         best_sum = current_sum
#         best_user = i
#
# print(f"Best candidate is {best_user} with total {best_sum} points.")
# print('Ranking:')
#
# for k in sorted(results.keys()):
#     print(k)
#     for (m, p) in sorted(results[k].items(), key=lambda cp: -cp[1]):
#         print(f'#  {m} -> {p}')





















