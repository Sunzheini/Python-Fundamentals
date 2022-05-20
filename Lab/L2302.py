

#class - blueprint for creating objects

#instance(object) attributes
#__init__() - initialize attributes

#instance(object) methods

# class MyClassIsPerson:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#
# daniel = MyClassIsPerson('Daniel', 'Zorov', '39')
#
# print(daniel.first_name)
# print(daniel.last_name)
# print(daniel.age)


# class MyClassIsPerson:
#     def __init__(self, first_name, last_name, age):
#         self.first = first_name
#         self.last = last_name
#         self.ag = age
#
#
# daniel = MyClassIsPerson('Daniel', 'Zorov', '39')
#
# print(daniel.first)
# print(daniel.last)
# print(daniel.ag)


# class MyClassIsPerson:
#     def __init__(self, first_name, last_name, age=39):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     def say_hello(self):
#         return f'Hello {self.first_name} {self.last_name} {self.age}'
#
#
# daniel = MyClassIsPerson('Daniel', 'Zorov')
#
# print(daniel.first_name)
# print(daniel.last_name)
# print(daniel.age)
# print()
#
# danielcho = MyClassIsPerson(last_name='Danielcho', first_name='Zorov')
# print(danielcho.age)
# print(danielcho.last_name)
# print()
# print(danielcho.say_hello())

#------------------------------------------------------------------------------

# 1
# class Comment:
#     def __init__(self, username, content, likes=0):
#         self.username = username
#         self.content = content
#         self.likes = likes
#
#
# my_comment = Comment('D', 'Z', 33)
# print(my_comment.likes)

#------------------------------------------------------------------------------

#objects
# class MyClassIsPerson:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#
# daniel = MyClassIsPerson('Daniel', 'Zorov', 39)
# daniel.age += 1
# daniel.last_name = 'mumu'
# print(daniel.age)
# print(daniel.last_name)

#------------------------------------------------------------------------------

# 2
# class Party:
#     def __init__(self):
#         self.people = []
#
#
# party = Party()
#
# while 1:
#     command = input()
#     if command == 'End':
#         break
#     party.people.append(command)
#
# print(f"Going: {', '.join(party.people)}")
# print(f"Total: {len(party.people)}")

#------------------------------------------------------------------------------

# class Person:
#     species = 'mammal'
#
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#
# daniel = Person('Daniel', 'Zorov', 39)
# print(daniel.species)



# class Test:
#     value = 52
#
#     def __init__(self):
#         self.value = 42
#
# print(Test.value)
#
# t = Test()
# print(t.value)
#
# del t.value
# print(t.value)

# Methods
#------------------------------------------------------------------------------

# class Test:
#     value = 52
#
#     def __init__(self, val1, val2):
#         self.val1 = val1
#         self.val2 = val2
#
#     def sum_numbers(self, val3):
#         return self.val1 * self.val2 * val3
#
#
# obj = Test(11, 22)
# print(obj.sum_numbers(3))
#------------------------------------------------------------------------------

# 3 list of objects
# class Email:
#
#     def __init__(self, sender, receiver, content):
#         self.sender = sender
#         self.receiver = receiver
#         self.content = content
#         self.is_sent = False
#
#     def send(self):
#         self.is_sent = True
#
#     def get_info(self):
#         return f"{self.sender} says to {self.receiver}: " \
#                f"{self.content}. Sent: {self.is_sent}"
#
#
# emails = []
# indices = []
#
# while 1:
#     command = input()
#     if command == "Stop":
#         indices = list(map(int, input().split(', ')))
#         break
#
#     explode = command.split(' ')
#     input_sender = explode[0]
#     input_receiver = explode[1]
#     input_content = explode[2]
#
#     email = Email(input_sender, input_receiver, input_content)
#     emails.append(email)
#
# for i in range(len(emails)):
#     if i in indices:
#         emails[i].send()
#     print(emails[i].get_info())

# 4 protected class attribute __animals (cannot access), _animals (can access with warning??)
# class Zoo:
#     __animals = 0
#
#     def __init__(self, name):
#         self.name = name
#         self.mammals = []
#         self.fishes = []
#         self.birds = []
#
#     def add_animal(self, species, name):
#         if species == 'mammal':
#             self.mammals.append(name)
#         elif species == 'fish':
#             self.fishes.append(name)
#         elif species == 'bird':
#             self.birds.append(name)
#         Zoo.__animals += 1
#
#     def get_info(self, species):
#         result = ''
#
#         if species == 'mammal':
#             result += f"Mammals in {self.name}: {', '.join(self.mammals)}"
#         elif species == 'fish':
#             result += f"Fishes in {self.name}: {', '.join(self.fishes)}"
#         elif species == 'bird':
#             result += f"Birds in {self.name}: {', '.join(self.birds)}"
#
#         result += f"\nTotal animals: {Zoo.__animals}"
#         return result
#
#
# name_of_zoo = input()
# zoo_object = Zoo(name_of_zoo)
# my_number = int(input())
#
# for i in range(my_number):
#     animal_info = input().split(' ')
#     species = animal_info[0]
#     name = animal_info[1]
#     zoo_object.add_animal(species, name)
#
# final_line = input()
#
# print(zoo_object.get_info(final_line))

# 5 sam
# class Circle:
#     __pi = 3.14
#
#     def __init__(self, diameter):
#         self.diameter = diameter
#         self.radius = self.diameter / 2
#
#     def calculate_circumference(self):
#         result = self.radius * Circle.__pi * 2
#         return result
#
#     def calculate_area(self):
#         result = Circle.__pi * self.radius * self.radius
#         return result
#
#     def calculate_area_of_sector(self, angle):
#         result = self.radius * self.radius * angle / 360 * Circle.__pi
#         return result
#
#
# circle = Circle(10)
# angle = 5
#
# print(f"{circle.calculate_circumference():.2f}")
# print(f"{circle.calculate_area():.2f}")
# print(f"{circle.calculate_area_of_sector(angle):.2f}")









