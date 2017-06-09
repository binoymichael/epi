from collections import Counter


def search(haystack, needle):
    haystack_map = Counter(list(haystack))

    needle_list = list(needle)
    for char in needle_list:
        if char in haystack_map and haystack_map[char] > 0:
            haystack_map[char] -= 1
        else:
            return False
    return True

letter = "hello world"
magazine = "some big piece of text that has a hello and a world"

print(search(magazine, letter))
