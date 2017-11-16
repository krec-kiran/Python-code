import random

rand = random.randint(1, 100)
val = input("Enter your guess number\t")
if (rand == int(val)):
    print("Your guessed the right number")
elif (int(val) > rand):
    print("Your guess number is larger by", int(val) - rand)
elif (int(val) < rand):
    print("Your guess number is smaller by", rand - int(val))
