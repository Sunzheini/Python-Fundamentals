# RegEx - selektirame konkreten text ot po golqm text

#find or find & replace

# \d - vryshta samo mesta kydeto ima cifra
# \D - nqma cifra
# \s - kydeto ima prazno mqsto
# \S - kydeto nqma prazno mqsto
# \w - ima bukva ili cifra
# \W - nqma bukva ili cifra
# \b - boundary

# + - 1 or more occurences
# * - 0 ot more occurences
# ? - 0 ili 1 ot simvolite (ili ima ili nqma)
# . - match any character except newline i za da polzvame kato tochka slagame \. -> www\.[A-Za-z0-9-]+\.[a-z.]+
# ^The.*Spain$ - vsichko mejdu The i Spain
# | - ili
# () - grupa
# {} - exact number of occurences       {5,} 5 pyti ili poveche    {5,8} ot 5 do 8 pyti
# ^ - new line starts with
# $ - ends with

# [arn] - neshtata koito sa vytre
# [a-zA-Z]
# [0-5][0-9] - 1 simvol ot 0 do 5 i edin simvol ot 0 do 9, t.e. 00 - 59
# [^arn] - vsichki simvoli razlichni ot arn

# (?<=\s) - positive lookbehind: proveri predi tova koeto iskash da machnesh ima prazno mqsto,
# no ne vkliuchvai praznoto mqsto
# (?=\s) - positive lookahead

# I#have*new BMW ==> (^|(?<=[^A-Za-z]))\w+

# methods
#-------------------------------------------------------------------------------------
# findall() - returns list!!! containing all matches or empty list if none

# search - pyrviq sluchai na namereno
# import re
# text = 'The movie was scary'
# x = re.search(r'^The.*scary$', text)
# print(x)

# if re.search(pattern, barcode) is None:  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#     print('Invalid barcode')
#     continue


# matches = re.match(pattern, barcode)  # moje da vryshta None!!!
# if matches is None:
#     print("Invalid barcode")


# split - split po neshto i vryshta list sys splitnatite neshta
# import re
# text = 'The movie was scary'
# result = re.split(r'\s', text)
# print(result)

# groups
#-------------------------------------------------------------------------------------
# import re
# text = 'The price of OLIVEOIL is 4 leva'
# result = re.search(r'(\b[A-Z]+\b).+(\b\d+)', text)
# print(result.group(1))  #grupa 1: OLIVEOIL
# print(result.groups())  # vryshta 2te: ('OLIVEOIL', '4')

# r"([=/])[A-Z][A_Za-z]{2,}\1"              \1 mai v krygli skobi syshto
# kakvoto si hvanal v nachaloto hvani go i v kraq (= ili /)

# for i in matches:
#     print(match[2])     #printira 2ra grupa!!!

#-------------------------------------------------------------------------------------

# 1
# import re
# text = input()
# matches = re.findall(r"\b[A-Z][a-z]+ [A-Z][a-z]+\b", text)
# print(" ".join(matches))

# 2a
# import re
# text = input()
# matches = re.findall(r"\+359 2 \d{3} \d{4}|\+359-2-\d{3}-\d{4}\b", text)
# print(", ".join(matches))

# 2b
# import re
# text = input()
# matches = re.finditer(r"\+359([ -])2\1\d{3}\1\d{4}\b", text)   #skobite sa grupirane na elementi

# output = list()                                                # finditer vryshta iterator
# for i in matches:
#     output.append(i.group())
# print(', '.join(output))

# 3
# import re
# text = input()
# expression = r"(?P<day>\d{2})(?P<separator>[./-])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})"
#
# matches = re.finditer(expression, text)
#
# output = list()
# for i in matches:
#     day = i.group("day")
#     month = i.group("month")
#     year = i.group("year")
#
#     print(f"Day: {day}, Month: {month}, Year: {year}")

# 4
# import re
# text = input()
# matches = re.finditer(r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.[0-9]+)?($|(?=\s))", text)
#
# output = list()
# for i in matches:
#     output.append(i.group())
# print(' '.join(output))



