b1 = """1000.00!=

125 Market !=:125.45
126 Hardware =34.95
127 Video! 7.45
128 Book :14.32
129 Gasoline ::16.10
"""
#
# b1sol = """Original Balance: 1000.00\r
# 125 Market 125.45 Balance 874.55\r
# 126 Hardware 34.95 Balance 839.60\r
# 127 Video 7.45 Balance 832.15\r
# 128 Book 14.32 Balance 817.83\r
# 129 Gasoline 16.10 Balance 801.73\r
# Total expense  198.27\r
# Average expense  39.65"""


def balance(b1):
    for x in '''!%:,=''':
        if x in b1:
            b1 = b1.replace(x, '')
    l1 = b1.split()
    b2 = 'Original Balance: ' + l1[0] + '\r\n'

    balance = l1[0]
    count = 0
    total_expense = 0
    for x in range(1, len(l1)):
        if x % 3 == 0:
            expense = l1[x]
            count += 1
            total_expense += float(l1[x])
            balance = float(balance) - float(expense)
            val = 'Balance ' + str('%.2f' % balance)
            b2 += l1[x - 2] + ' ' + l1[x - 1] + ' ' + l1[x] + ' ' + val + '\n'
    average = total_expense / count
    b2 += 'Total expense' + str(' %.2f' % total_expense) + \
        '\r\n' + 'Average expense' + str(' %.2f' % average)

    return(b2)


print(balance(b1))
