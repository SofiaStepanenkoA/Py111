from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    num_to_index = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i


print(two_sum([3, 3], 6))  # Output: [0, 1]
