# Given a lottery ticket (ticket), represented by an array of 2-value arrays, you must find out if you've won the jackpot. Example ticket:
#
# [ [ 'ABC', 65 ], [ 'HGR', 74 ], [ 'BYHT', 74 ] ]
# To do this, you must first count the 'mini-wins' on your ticket. Each sub array has both a string and a number within it. If the character code of any of the characters in the string matches the number, you get a mini win. Note you can only have one mini win per sub array.
#
# Once you have counted all of your mini wins, compare that number to the other input provided (win). If your total is more than or equal to (win), return 'Winner!'. Else return 'Loser!'.
# All inputs will be in the correct format. Strings on tickets are not always the same length.
# Kata - 6kyu


def jackpot(lottery):
    miniWins = 0
    for i in range(len(lottery)):
        text = lottery[i][0]
        val = lottery[i][1]
        for i in text:
            if ord(i) == val:
                miniWins += 1
                break
    return miniWins


win = int(input("Enter the input win "))
lottery = [['ABC', 67], ['HGR', 72], ['BYHT', 72], ['CDEFG', 68]]
miniWins = jackpot(lottery)
print("MiniWins", miniWins)
if miniWins >= win:
    print("Winner!")
else:
    print("Loser!")
