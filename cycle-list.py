#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 10:21:47 2017

@author: Kirans
"""

bicycles = ['trek', 'cannondale', 'redline', 'specialized']

for i in bicycles:
    print(i.title() + ", is the bicyle name" + "\n")


for value in range(1, 5):
    print(value)

numbers = list(range(1, 10))
print(numbers)

squares = [values**2 for values in range(1, 11)]
print(squares)
print(sum(squares))

print(squares[2:7])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
for player in players[:4]:
    print(player.title())

temp_players = players[:]
print("The new set of players :")
for i in temp_players:
    print(i.title())

players.append("kiran")

print(players)


dimensions = (200, 500)
print(dimensions[0])
print(dimensions[1])
for dimension in dimensions:
    print(dimension)

buffet = ('pasta', 'pizza', 'french toast', 'english', 'salads')
print("The buffet of resturant X is")
for item in buffet:
    print(item.title())

buffet = ('dosa', 'idli', 'french toast', 'english', 'salads')
print("The revised menu of the resturant X is")
for item in buffet:
    print(item.title())


alien_0 = {'color': 'green', 'points': 5, 'x-pos': 100, 'y-pos': 200}
print(alien_0['color'])
print(alien_0['points'])

print("Dictionary key value pairs")

for key, values in alien_0.items():
    print(key, ":", values)

print("\n")

for key in alien_0:
    print(key.title(), "::", alien_0[key])


def greet_user(name):
    print("Hello", name.title())
    pass

greet_user("demo")


def make_pizza(*toppings):
    print(toppings)
    pass

make_pizza('pepporoni', 'mushroom', 'green peppers')


import profile

user_profile = profile.build_profile(
    'Albert', 'Einstein', location='Princeton', field='Physics', age=80, country='USA')
print(user_profile)
