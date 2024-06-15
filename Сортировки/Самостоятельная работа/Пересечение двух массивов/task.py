from typing import List


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    set1 = set(nums1)
    set2 = set(nums2)
    inter=[]
    for i in set1:
        if i in set2:
            inter.append(i)
    return inter

print(intersection([1,2,2,1],[2,2]))
