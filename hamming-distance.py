def ham_dist(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("Not defined - unequal length sequnces")
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))


s1 = [2, 5, 3]
s2 = [2, 5, 5]

if __name__ == '__main__':
  print(ham_dist("karolin", "kathrin"))
  print(ham_dist("karolin", "kerstin"))
  print(ham_dist("1011101", "1001001"))
  print(ham_dist("2173896", "2233796"))

  print(list(zip(s1, s2)))

  print("VALUES", sum(a * b for a, b in zip(s1, s2)))

  print("Sum", sum(s1, 10))
