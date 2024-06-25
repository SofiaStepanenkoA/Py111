from typing import List


def is_subsequence(a: str, b: str) -> bool:
    it = iter(b)
    return all(char in it for char in a)


def find_lus_length(strs: List[str]) -> int:
    strs.sort(key=len, reverse=True)

    for i, s in enumerate(strs):
        if strs.count(s) == 1:
            if all(not is_subsequence(s, strs[j]) for j in range(len(strs)) if i != j):
                return len(s)

    return -1


print(find_lus_length(["aba", "cdc", "eae"]))  #  3
print(find_lus_length(["aaa", "aaa", "aa"]))  # -1
