from collections import defaultdict

from numpy import iterable


def func(data: iterable)->str:
    if not data:
        return ""

    consensus = []
    length = len(data[0])
    for i in range(length):
        count = defaultdict(int)

        for sequence in data:
            count[sequence[i]] += 1

        max_char = ''
        max_count = 0
        for char, cnt in count.items():
            if cnt > max_count:
                max_char = char
                max_count = cnt

        consensus.append(max_char)

    return ''.join(consensus)

data = [
    "ATTA",
    "ACTA",
    "AGCA",
    "ACAA"
]

print(func(data))  #  "ACTA"
