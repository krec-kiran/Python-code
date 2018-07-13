fruits = ["rottenApple", "rottenBanana",
          "rottenApple", "rottenPineapple", "rottenKiwi"]

for i in range(len(fruits)):
    if 'rotten' in fruits[i]:
        fruits[i] = fruits[i].replace('rotten', '').lower()
print(fruits)
