from functools import reduce
from operator import add


def encode_spread_sheet_column(input):
    return reduce(add, ((26 ** i) * (ord(c) - ord('A') + 1)
                        for i, c in enumerate(input[::-1])))

assert encode_spread_sheet_column("AD") == 30
assert encode_spread_sheet_column("ZZ") == 702
