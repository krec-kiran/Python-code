roman_directory = {1: 'I', 2:
                   'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}


def get_roman_numeral(numb, digit, roman_literal):

    remainder = numb % digit
    quotient = int(numb / digit)

    if quotient > 1:
        roman_digit = roman_literal * quotient
    else:
        roman_digit = roman_literal

    return remainder, roman_digit


def convert_number_to_roman(numb):
    roman_equivalent = ''

    while(numb > 10):

        if numb >= 1000:
            numb, roman_literal = get_roman_numeral(numb, 1000, 'M')
            roman_equivalent += roman_literal
        if numb >= 500:
            numb, roman_literal = get_roman_numeral(numb, 500, 'D')
            roman_equivalent += roman_literal
        if numb >= 100:
            numb, roman_literal = get_roman_numeral(numb, 100, 'C')
            roman_equivalent += roman_literal
        if numb >= 50:
            numb, roman_literal = get_roman_numeral(numb, 50, 'L')
            roman_equivalent += roman_literal
        if numb >= 10:
            numb, roman_literal = get_roman_numeral(numb, 10, 'X')
            roman_equivalent += roman_literal

    if numb < 10:
        roman_equivalent += roman_directory[numb]
        print('Roman equivalent:', roman_equivalent)


if __name__ == '__main__':
    number = input('Enter your number')
    convert_number_to_roman(int(number))
