import re


def is_palindrome2(sentence):
    def sanitize(s):
        return re.sub('[^a-zA-Z]', '', s).lower()
    return sanitize(sentence) == sanitize(sentence[::-1])


def is_palindrome(sentence):
    left, right = 0, len(sentence) - 1

    while right > left:
        if not sentence[left].isalnum():
            left += 1
            continue

        if not sentence[right].isalnum():
            right -= 1
            continue

        if sentence[left].lower() == sentence[right].lower():
            left += 1
            right -= 1
        else:
            return False

    return True

print(is_palindrome("A man, a plan, a canal, Panama."))
print(is_palindrome("Ray a Ray"))
