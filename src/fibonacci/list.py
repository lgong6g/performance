# @profile
def fibonacci_list(num_items: int = 100_000) -> list:
    numbers = []
    a, b = 0, 1
    while len(numbers) < num_items:
        numbers.append(a)
        a, b = b, a+b
    return numbers


if __name__ == "__main__":
    count = 100_000
    print(f'Current task: Find all fibonacci numbers up to {str(count)}')
    for i in fibonacci_list(count):
        pass
