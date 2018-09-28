a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa",
      "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]


def mxdiflg(a1, a2):
    return max([abs(len(x) - len(y)) for x in a1 for y in a2]) if a1 and a2 else -1


print(mxdiflg(a1, a2))
