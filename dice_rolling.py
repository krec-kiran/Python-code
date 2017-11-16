# Roll a dice and randomly chooses a number between 1 to 6 infinitely till the user stops by saying - NO / N / n / no / No
import random
answer = "Y"
values = ["N","NO","No","n","no"]
while not answer in values:
    print(random.randint(1, 6))
    answer = input("Do you want to roll the dice again?")


