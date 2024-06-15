from typing import List, Optional

def majority_element(nums: List[int]) -> Optional[int]:
    if not nums:
        return None

    counter = 0
    majority_element = 0

    for num in nums:
        if counter == 0:
            majority_element = num
            counter = 1
        elif num == majority_element:
            counter += 1
        else:
            counter -= 1

    return majority_element

# Тестирование
print(majority_element([2, 2, 1, 1, 1, 2, 2]))  # Output: 2
print(majority_element([]))  # Output: None
