def encode(input):
    i, j, l = 0, 1, len(input)
    result = ""
    while not j > l:
        s = input[i]
        while j < l and s == input[j]:
            j += 1
        result += str(j - i) + s
        i, j = j, j + 1

    return result

def decode(input):
    result = ""
    for i in range(0, len(input), 2):
        result += int(input[i]) * input[i + 1]
    return result

print(encode(decode("3e4b")))




