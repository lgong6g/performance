import pytest
import src.fibonacci.list as fibolist
import src.fibonacci.generator as fibogen


@pytest.mark.parametrize(
    "count, fibonacci_numbers",
    [
        pytest.param(
            10,
            [0, 1, 1, 2, 3, 5, 8, 13, 21, 34],
            id="Common Fibonacci numbers")
    ]
)
def test_fibonacci_numbers(count: int, fibonacci_numbers: list):
    assert fibolist.fibonacci_list(num_items=count) == fibonacci_numbers
    assert [i for i in fibogen.fibonacci_generator(num_items=count)] == fibonacci_numbers


@pytest.mark.parametrize(
    "count, wrong_fibonacci_numbers",
    [
        pytest.param(
            10,
            [2, 2, 3, 3, 6, 9, 12, 14, 22, 35],
            id="Wrong Fibonacci numbers")
    ]

)
def test_wrong_fibonacci_numbers(count: int, wrong_fibonacci_numbers: list):
    assert not fibolist.fibonacci_list(num_items=count) == wrong_fibonacci_numbers
    assert not [i for i in fibogen.fibonacci_generator(num_items=count)] == wrong_fibonacci_numbers
