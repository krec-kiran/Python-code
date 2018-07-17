# Kate and Michael want to buy a pizza and share it. Depending on the price of the pizza, they are going to divide the costs:
#
# If the pizza is less than €5,- Michael invites Kate, so Michael pays the full price.
# Otherwise Kate will contribute 1/3 of the price, but no more than €10 (she's broke :-) and Michael pays the rest.
# How much is Michael going to pay? Calculate the amount with two decimals, if necessary.
# Kata - 7kyu


def michael_pays(cost):
    mike_pay = 0
    if(cost < 5):
        mike_pay = cost
    else:
        if cost / 3 <= 10:
            cost = cost - cost / 3
        else:
            cost = cost - 10

        mike_pay = cost

    return round(mike_pay, 2)
