from typing import List


def generate(num_rows: int) -> List[List[int]]:
    if num_rows == 0:
        return []
    tre = [[1]]
    for i in range(1,num_rows):
        row = [1]
        for j in range(1, i):
            row.append(tre[i - 1][j - 1] + tre[i - 1][j])
        row.append(1)
        tre.append(row)
    return tre
n=5
print(generate(n))