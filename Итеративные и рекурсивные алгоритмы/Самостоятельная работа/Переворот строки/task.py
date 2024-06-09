from typing import List


def reverse_string(s: List[str]) -> None:
    left_border=0
    right_border=len(s)-1
    while left_border<right_border:
        s[left_border],s[right_border]=s[right_border],s[left_border]
        left_border+=1
        right_border-=1
# (reverse_string('test'))
