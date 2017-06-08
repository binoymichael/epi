def sinusoidal(input):
    top = input[1::4]
    middle = input[0::2]
    bottom = input[3::4]
    return "".join(v for v in top + middle + bottom)


print(sinusoidal("Hello World"))