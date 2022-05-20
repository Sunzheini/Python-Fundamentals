#
#
# population = list(map(int, input().split(', ')))
# min_wealth = int(input())
# is_possible = True
#
# while 1:
#     current_min = min(population)
#     current_max = max(population)
#     if current_min < min_wealth:
#         if current_max == min_wealth:
#             is_possible = False
#             break
#         else:
#             where_min = population.index(current_min)
#             population[where_min] += 1
#             where_max = population.index(current_max)
#             population[where_max] -= 1
#     else:
#         break
#
# if is_possible:
#     print(population)
# else:
#     print("No equal distribution possible")
