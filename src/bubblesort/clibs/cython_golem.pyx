def bubble_sort(numbers: list):
    size = len(numbers)
    for _ in range(size):
        for j in range(size - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers