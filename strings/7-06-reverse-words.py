def reverse(input, left=0, right=None):
    if not right:
        right = len(input)

    right = right - 1
    while left < right:
        input[left], input[right] = input[right], input[left]
        left, right = left + 1, right - 1

    return input


def reverse_words(sentence):
    sentence = list(sentence)
    i, j = 0, 0

    while j < len(sentence):
        while not sentence[i].isalnum():
            i += 1
        j = i

        while j < len(sentence) and sentence[j].isalnum():
            j += 1

        reverse(sentence, i, j)
        i = j

    return "".join(sentence)



print(reverse_words(reverse(list("binoy robin"))))
