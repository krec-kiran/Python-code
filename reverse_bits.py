n = 417


def reverse_bits(n):
    if n == 0:
        return 0
    return (int((str(format(int(n), '08b')).lstrip('0'))[::-1], 2))


print(reverse_bits(n))
