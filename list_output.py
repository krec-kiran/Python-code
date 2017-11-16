# a = [1, 1, 2, 3, 5, 8, 13, 21, 0, 34, 55, 89]
# b = []

# val = input("Enter your number choice ")

# for i in a:
#     if i < int(val):
#         b.append(i)

# print(b)


user1 = (input("Enter user-1 choice")).casefold()
user2 = (input("Enter user-2 choice")).casefold()

if user1 == "Rock" and user2 == "scissors":
  print("user1 wins")
if user1 == "Scissors" and user2 == "paper":
  print("user1 wins")
if user1 == "paper" and user2 == "rock":
  print("user1 wins")

if user2 == "Rock" and user1 == "scissors":
  print("user2 wins")
if user2 == "Scissors" and user1 == "paper":
  print("user2 wins")
if user2 == "paper" and user1 == "rock":
  print("user2 wins")
