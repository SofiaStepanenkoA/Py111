def funk(n: int, k: int) -> int:
    people = list(range(1, n + 1))
    current_index = 0

    while len(people) > 1:
        current_index = (current_index + k - 1) % len(people)
        people.pop(current_index)

    return people[0]

print(funk(7, 3))
