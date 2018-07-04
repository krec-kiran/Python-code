# Kate and Michael want to buy a pizza and share it. Depending on the price of the pizza, they are going to divide the costs:
#
# If the pizza is less than €5,- Michael invites Kate, so Michael pays the full price.
# Otherwise Kate will contribute 1/3 of the price, but no more than €10 (she's broke :-) and Michael pays the rest.
# How much is Michael going to pay? Calculate the amount with two decimals, if necessary.
# Kata - 7kyu


def payment(cost):
    mike_pay = 0
    if(cost < 5):
        mike_pay = cost
    elif (cost / 3 <= 10):
        mike_pay = (2 / 3) * (cost)
    else:
        mike_pay = None
    return mike_pay


for i in range(40):
    mikeBill = payment(i)
    if mikeBill:
        print("Cost:£%d % .2f" % (i, mikeBill))
    else:
        print("no treat possible!")
