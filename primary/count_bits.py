def count_bits(i):
    number_of_bits = 0
    while i:
        number_of_bits += (i & 1)
        i >>= 1
    return number_of_bits

print(count_bits(4))
print(count_bits(7))
