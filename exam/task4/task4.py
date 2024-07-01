import random
import time

data = [random.randint(13, 25) for _ in range(10 ** 6)]


# Сортировка подсчетами
def counting_sort(arr):
    counts = [0] * 13  # Диапазон чисел от 13 до 25
    for num in arr:
        counts[num - 13] += 1

    sorted_arr = []
    for i in range(13):
        sorted_arr.extend([i + 13] * counts[i])

    return sorted_arr


# Быстрая сортировка
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# Сортировка слиянием
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


methods = {
    'Counting Sort': counting_sort,
    'Merge Sort': merge_sort,
    'Quick Sort': quick_sort
}

# Измерение скорости выполнения
for name, sort_func in methods.items():
    start_time = time.time()
    sorted_data = sort_func(data.copy())
    elapsed_time = time.time() - start_time
    print(f"{name}: {elapsed_time:.4f} сек")

# По результатам десяти запусков наимешим временем выполнения обладает сортировка подсчетами
# Сложность сортировки подсчетами линейная
# Сложность сортировки слиянием 0(n*log(n))
# Сложность быстрой сортировки 0(n^2)