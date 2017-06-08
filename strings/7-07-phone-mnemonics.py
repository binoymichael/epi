PHONE_MAP = {str(i): list(a) for i, a in enumerate(["0", "1", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"])}



def mnenomic_for(input):
    input = list(input)
    result = []

    def compute_mnemonic(input, output=""):
        if not input:
            result.append(output)
            return

        head, *tail = input
        options = PHONE_MAP[head]
        for x in options:
            compute_mnemonic(tail, output + x)

    compute_mnemonic(input)
    return result



print(mnenomic_for("22"))