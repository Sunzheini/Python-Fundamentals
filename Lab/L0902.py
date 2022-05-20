# comprehension

# num_list = [i for i in range(5)]
# print(num_list)

# num_list = [1, 2, 3, 4]
# new_list = [i**2 for i in num_list]
# print(new_list)

# old_list = [1, 2, 3, 4, 5, 6]
# new_list = [i**2 for i in old_list if i > 3]
# print(new_list)

# old_list = [1, 2, 3, 4, 5, 6]
# new_list = [i**2 if i > 3 else i * 2 for i in old_list]
# print(new_list)

# 1
# input_text = input()
# vowels = ['a', 'o', 'u', 'e', 'i']
# no_vowels = [i for i in input_text if i not in vowels]
# print(''.join(no_vowels))

# 2
# wagons = int(input())
# train = [0 for i in range(wagons)]
# #stava i train = [0] * wagons
# command = input()
# while command != 'End':
#     info = command.split(' ')
#     info0 = info[0]
#     info1 = int(info[1])
#
#     if info0 == 'add':
#         train[-1] += info1
#     elif info0 == 'insert':
#         info2 = int(info[2])
#         train[info1] += info2
#     elif info0 == 'leave':
#         info2 = int(info[2])
#         train[info1] -= info2
#     command = input()
# print(train)

# 3
# notes = input()
# schedule = ["" for i in range(11)]
#
# while notes != 'End':
#     explode = notes.split("-")
#     number = int(explode[0])
#     task = explode[1]
#
#     schedule.pop(number)
#     schedule.insert(number, task)
#
#     #schedule[number] = task
#
#     notes = input()
#
# new_list = [j for j in schedule if j != ""]
#
# print(new_list)

# 4
# words = input().split(' ')
# palindrome = input()
# new_list = []
# counter = 0
#
# for i in words:
#     if i == i[::-1]:
#         new_list.append(i)
#
#     # if i == palindrome:
#     #     counter += 1
#
# print(new_list)
# print(f"Found palindrome {words.count(palindrome)} times")


#reverse a string or a list:
#rev_word = reversed(word)

#sorted
# numbers = [3, 4, 1, 2, 7, 5]
# # sorted_numbers = sorted(numbers) #sortira list po vyzhodqsht red
# sorted_numbers = sorted(numbers, key=lambda x: -x) #sortira naobratno


# 5
# names = input().split(', ')
#
# #variant1
# sorted_names = sorted(names)
# sorted_names = sorted(sorted_names, key=lambda name: -len(name))
# print(sorted_names)
#
# #variant2
# # whole_sorted_names = sorted(names, key=lambda name: (-len(name), name))
# # print(whole_sorted_names)


#map
# strings_list = ['1', '2', '3', '4']
# int_list = list(map(int, strings_list))
# print(int_list)

# numbers_list = [1, 2, 3, 4]
# doubled_list = list(map(lambda x: x*2, numbers_list))
# print(doubled_list)

#filter
# numbers_list = [1, 2, 3, 4, 5, 6]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers_list))
# print(even_numbers)


# 6a
# numbers = input().split(', ')
# numbers = list(map(int, numbers))
# even_indices = []
#
# for i in range(len(numbers)):
#     if numbers[i] % 2 == 0:
#         even_indices.append(i)
#
# print(even_indices)

# 6b
# nums = [int(el) for el in input().split(", ")]
# print([index for index in range(len(nums)) if nums[index] % 2 == 0])


#concatenate lists with +
#use set() to extract unique values only


# 7
# happiness = list(map(int, input().split(' ')))
# factor = int(input())
#
# for i in range(len(happiness)):
#     happiness[i] *= factor
#
# average = sum(happiness)/len(happiness)
#
# happy_number = list(filter(lambda x: x >= average, happiness))
#
# if len(happy_number) >= len(happiness) / 2:
#     print(f"Score: {len(happy_number)}/{len(happiness)}. Employees are happy!")
# else:
#     print(f"Score: {len(happy_number)}/{len(happiness)}. Employees are not happy!")
