from numpy import iterable


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


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


def func(data: iterable)->bool:
    data = merge_sort(data)
    current_end_time=float('-inf')
    for start, end in data:
        if start < current_end_time:
            return False
        current_end_time = end
    return True

data1 = [(1, 5),(6, 7),(22, 24),(7,13),(15, 20)]
data2 = [(13, 15), (15, 20), (18, 23)]

print(func(data1))  # True
print(func(data2))  # False
