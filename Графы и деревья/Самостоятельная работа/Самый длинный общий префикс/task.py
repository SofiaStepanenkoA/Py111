from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    if not strs:
        return ""
    if len(strs) == 1:
        return strs[0]
    strs.sort()
    first = strs[0]
    last = strs[-1]

    prefix = ""
    for i in range(min(len(first), len(last))):
        if first[i] == last[i]:
            prefix += first[i]
        else:
            break

    return prefix