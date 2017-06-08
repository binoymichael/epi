def encode_spread_sheet_column(input):
    answer = 0
    for index, char in enumerate(input[::-1]):
        answer += (26 ** index) * (ord(char) - ord('A') + 1)
    return answer

r = encode_spread_sheet_column("AD")
r = encode_spread_sheet_column("ZZ")
print(r)