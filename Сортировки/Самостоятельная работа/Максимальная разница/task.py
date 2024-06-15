from typing import List
import math


def maximum_gap(nums: List[int]) -> int:
    if len(nums) < 2:
        return 0

    min_val, max_val = min(nums), max(nums)
    if min_val == max_val:
        return 0

    bucket_size = math.ceil((max_val - min_val) / (len(nums) - 1))
    bucket_count = (max_val - min_val) // bucket_size + 1

    buckets = [[None, None] for _ in range(bucket_count)]

    for num in nums:
        bucket_idx = (num - min_val) // bucket_size
        if buckets[bucket_idx][0] is None:
            buckets[bucket_idx][0] = buckets[bucket_idx][1] = num
        else:
            buckets[bucket_idx][0] = min(buckets[bucket_idx][0], num)
            buckets[bucket_idx][1] = max(buckets[bucket_idx][1], num)

    max_gap = 0
    prev_max = min_val

    for bucket in buckets:
        if bucket[0] is not None:
            max_gap = max(max_gap, bucket[0] - prev_max)
            prev_max = bucket[1]

    return max_gap


# Примеры использования
print(maximum_gap([3, 6, 9, 1]))  # Output: 3
print(maximum_gap([10]))  # Output: 0
