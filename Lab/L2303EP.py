# 1 - 01. The Imitation Game (text processing)
#
# encrypted = input()
#
# instruction = input()
# while instruction != 'Decode':
#     explode = instruction.split('|')
#
#     if explode[0] == 'Move':
#         number = int(explode[1])
#         temp = ''
#         temp += encrypted[number:]
#         temp += encrypted[:number]
#         encrypted = temp
#
#     elif explode[0] == 'Insert':
#         index = int(explode[1])
#         value = explode[2]
#         temp = ''
#         temp += encrypted[:index]
#         temp += value
#         temp += encrypted[index:]
#         encrypted = temp
#
#     elif explode[0] == 'ChangeAll':
#         substring = explode[1]
#         replacement = explode[2]
#
#         temp = encrypted.replace(substring, replacement)
#         encrypted = temp
#
#     instruction = input()
#
# print(f"The decrypted message is: {encrypted}")

# 2 - 02. Destination Mapper (regex) --> izberi "python" v regex 101!

# import re
#
# places = input()
# output = []
# travel_points = 0
#
# pattern = r'(?P<part1>=|\/)(?P<part2>[A-Z][A-Za-z][A-Za-z]+)(?P<part3>=|\/)'
# matches = re.finditer(pattern, places)
#
# for i in matches:
#     if i.group('part1') == i.group('part3'):
#         output.append(i.group('part2'))
#
# for j in output:
#     travel_points += int(len(j))
#
# print(f'Destinations: ', end='')
# print(f"{', '.join(output)}")
# print(f"Travel Points: {travel_points}")

# 3 - 03. Heroes of Code and Logic VII (dict)

# party_size = int(input())
# party_dict = {}
#
# for i in range(party_size):
#     current_hero = input().split(' ')
#     name = current_hero[0]
#     hp = int(current_hero[1])
#     mp = int(current_hero[2])
#     party_dict[name] = {}
#     party_dict[name]['hp'] = hp
#     party_dict[name]['mp'] = mp
#
# command = input()
# while command != 'End':
#     explode = command.split(' - ')
#     action = explode[0]
#
#     if action == 'CastSpell':
#         hero_name = explode[1]
#         mp_needed = int(explode[2])
#         spell_name = explode[3]
#
#         if party_dict[hero_name]['mp'] >= mp_needed:
#             party_dict[hero_name]['mp'] -= mp_needed
#             print(f"{hero_name} has successfully cast {spell_name} and "
#                   f"now has {party_dict[hero_name]['mp']} MP!")
#         else:
#             print(f"{hero_name} does not have enough MP to cast {spell_name}!")
#
#     elif action == 'TakeDamage':
#         hero_name = explode[1]
#         damage = int(explode[2])
#         attacker = explode[3]
#
#         party_dict[hero_name]['hp'] -= damage
#
#         if party_dict[hero_name]['hp'] > 0:
#             print(f"{hero_name} was hit for {damage} HP by {attacker} and now "
#                   f"has {party_dict[hero_name]['hp']} HP left!")
#         else:
#             print(f"{hero_name} has been killed by {attacker}!")
#             party_dict.pop(hero_name)
#
#     elif action == 'Recharge':
#         hero_name = explode[1]
#         amount = int(explode[2])
#
#         before_recharge = party_dict[hero_name]['mp']
#         party_dict[hero_name]['mp'] += amount
#
#         if party_dict[hero_name]['mp'] > 200:
#             recharged = 200 - before_recharge
#             party_dict[hero_name]['mp'] = 200
#         else:
#             recharged = amount
#
#         print(f"{hero_name} recharged for {recharged} MP!")
#
#     elif action == 'Heal':
#         hero_name = explode[1]
#         amount = int(explode[2])
#
#         before_heal = party_dict[hero_name]['hp']
#         party_dict[hero_name]['hp'] += amount
#
#         if party_dict[hero_name]['hp'] > 100:
#             healed = 100 - before_heal
#             party_dict[hero_name]['hp'] = 100
#         else:
#             healed = amount
#
#         print(f"{hero_name} healed for {healed} HP!")
#
#     command = input()
#
# for i in party_dict.keys():
#     print(i)
#     for j in party_dict[i].keys():
#         print(f"  {j.swapcase()}: {party_dict[i][j]}")


