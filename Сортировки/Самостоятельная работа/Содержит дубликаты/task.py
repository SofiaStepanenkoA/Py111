from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    comp_list=[]
    for i in range(len(nums)):
        if nums[i] not in comp_list:
            comp_list.append(nums[i])
        else:
            return True
    return False