# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def createPhoneNumber(digits):
    digits = list(map(str, digits))
    digits = "".join(digits)
    return("(" + (digits[0:3]) + ")" + " " +
           (digits[3:6]) + "-" + (digits[6:]))


print(createPhoneNumber(digits))
