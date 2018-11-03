def baby_count(s):
    b_count = s.count('b') + s.count('B')
    a_count = s.count('a') + s.count('A')
    y_count = s.count('y') + s.count('Y')

    if b_count < 2 or a_count < 1 or y_count < 1:
        return 'Where\'s the baby?!'
    count = min(int(b_count / 2), a_count, y_count)
    return count
