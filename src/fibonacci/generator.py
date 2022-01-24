from memory_profiler import memory_usage


# https://github.com/pythonprofilers/memory_profiler/issues/42
# Does not work with current yield statement @profile
def fibonacci_generator(num_items: int = 100_000) -> list:
    a, b = 0, 1
    while num_items:
        yield a
        a, b = b, a+b
        num_items -= 1


if __name__ == "__main__":
    # https://stackoverflow.com/questions/31662706/profiling-memory-usage-in-python-generators
    print(f'Memory usage before: {memory_usage()}MB')
    count = 100_000_0
    print(f'Current task: Find all fibonacci numbers up to {str(count)}')
    for i in fibonacci_generator(count):
        pass
    print(f'Memory usage after: {memory_usage()}MB')
