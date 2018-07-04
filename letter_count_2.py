d = {1: 'one', 2: 'two', 3: 'three', 4: 'four',
     5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
     15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
     }

divide = {90: 'ninety', 80: 'eighty', 70: 'seventy', 60: 'sixty',
          50: 'fifty', 40: 'forty', 30: 'thirty', 20: 'twenty'}

divide.update(d)


def letterCheck(numb):
    for i in sorted(divide, reverse=True):
        if int(numb / i) > 0:
            return i


def letterCount(numb):
    text = ''
    while(numb > 0):
        if numb >= 100:
            k = int(numb / 100)
            if numb % 100 == 0:
                return d[k] + "hundred"
            text = d[k] + " hundred and"
            numb = numb % 100
        if numb != 0:
            val = letterCheck(numb)
            text = text + ' ' + divide[val]
            q = numb % val
            numb = numb / val
            if q in divide:
                text = text + ' ' + d[q]
            if q < 20:
                # print("It is - ", text, " - in plain English!")
                return text


count = 0
for i in range(1, 1000):
    letter = letterCount(i)
    if letter:
        letter = letter.replace(" ", "")
        # print(letter)
        count += len(letter)
    # print("Count now", count)
print("Total Count is:", count + len('onethousand'))
