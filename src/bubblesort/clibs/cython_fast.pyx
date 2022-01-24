def bubble_sort(numbers: list):
    has_swapped = True
    num_of_iterations = 0

    while has_swapped:
        has_swapped = False
        for i in range(len(numbers) - num_of_iterations - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                has_swapped = True
        num_of_iterations += 1

    return numbers