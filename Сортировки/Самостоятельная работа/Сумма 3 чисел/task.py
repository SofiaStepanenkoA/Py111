def three_sum(nums):
    # Сортируем массив
    nums.sort()
    triplets = []

    # Проходим по массиву
    for i in range(len(nums) - 2):
        # Пропускаем одинаковые элементы, чтобы избежать дубликатов
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Используем два указателя
        left, right = i + 1, len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == 0:
                triplets.append([nums[i], nums[left], nums[right]])

                # Пропускаем одинаковые элементы
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1

    return triplets


# Примеры использования
nums1 = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums1))  # [[-1, -1, 2], [-1, 0, 1]]

nums2 = [0, 1, 1]
print(three_sum(nums2))  # []

nums3 = [0, 0, 0]
print(three_sum(nums3))  # [[0, 0, 0]]
