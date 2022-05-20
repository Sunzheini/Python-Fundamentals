# flagove
import re

# re.I ili re.IGNORECASE
# text = 'DAniel is superman Maxi is noob'
# result = re.findall(r'Daniel', text, re.I)
# print(result)       #['DAniel']

# re.X ili re.VERBOSE
# text = 'DAniel is superman Maxi is noob, his age is 39'
# result = re.search(r'''(^\w{6}) # match 5 letters at the start
#                         .+(\d{2}$) #match 2 digits at the end''', text, re.X)
# print(result.group(1))       #DAniel
# print(result.group(2))       #39

# re.M ili re.MULTILINE - verificirame nachalo i krai na nqkakyv text
# text = 'DAniel is superman Maxi is noob, his age is 39'
# result = re.findall(r'\d{2}$', text, re.M)
# print(result)

#-------------------------------------------------------------------------------------
# 1
# import re
#
# pattern = r'\d+'
#
# while True:
#     text = input()
#
#     if not text:      #taka moje da podavame novi redove dokato nqma veche nishto
#         break
#
#     result = re.findall(pattern, text)
#     if len(result) > 0:
#         print(' '.join(result), end=' ')


# --- moje i taka
# command = input()
# while command != '':
#     links.append(command)
#     command = input()
# ---


# 2
# import re
# pattern = r'\b_[a-zA-Z0-9]+\b'
# text = input()
#
# result = re.findall(pattern, text)
#
# words_list = []
#
# for i in result:
#     words_list.append(i[1:])
#
# print(','.join(words_list))

# 3
# import re
# text = input()
# word = input()
#
# pattern = rf'\b{word}\b'            # rf string
# result = re.findall(pattern, text, re.I)
#
# print(len(result))

# 4
# import re
#
# text = input()
#
# user_pattern = r'( |^)[a-zA-Z0-9]+((\.|\-|_)[a-zA-Z0-9]+)*'
# host_pattern = r'[a-zA-Z]+(-[a-zA-Z]+)*(\.[a-zA-Z]+(-[a-zA-Z]+)*)+'
#
# pattern = rf'{user_pattern}@{host_pattern}'
#
# emails = re.finditer(pattern, text)
#
# for i in emails:
#     print(i[0])

# 5
# import re
# to_purchase = False
# total_cost = 0
# furniture_list = []
#
# pattern = r'(?P<furniture_name>[a-zA-Z]+)<<(?P<price>\d+([\.]\d+)*)!(?P<quantity>\d+)'
#
# while 1:
#     command = input()
#     if command == 'Purchase':
#         to_purchase = True
#         break
#
#     matches = re.finditer(pattern, command)
#
#     for i in matches:
#         furniture_name = i.group('furniture_name')
#         price = i.group('price')
#         quantity = i.group('quantity')
#
#         furniture_list.append(furniture_name)
#         total_cost += float(price) * int(quantity)
#
# print('Bought furniture:')
# for j in furniture_list:
#     print(j)
# print(f'Total money spend: {total_cost:.2f}')

# 6
# import re
#
# pattern = r'www\.[A-Za-z0-9\-]+\.[a-z.]+'
# links = []
#
# command = input()
# while command != '':
#     matches = re.findall(pattern, command)
#     links.append(''.join(matches))
#     command = input()
#
# for i in links:
#     if i != '':
#         print(i)















