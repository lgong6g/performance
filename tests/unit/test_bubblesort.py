import pytest
import numpy as np
import src.bubblesort.fast as fast
import src.bubblesort.clibs.cython_fast as cython_fast
import src.bubblesort.golem as golem
import src.bubblesort.clibs.cython_golem as cython_golem
import src.bubblesort.sorted as python_sorted
import src.bubblesort.list_comprehension as list_comprehension
import src.bubblesort.jit as jit


@pytest.mark.parametrize(
    "unsorted_numbers, sorted_numbers",
    [
        pytest.param([99, 12, 38, 3, 8, 66, 12],
                     [3, 8, 12, 12, 38, 66, 99],
                     id="Positive integer"),
        pytest.param([23, 11, 9, -5, 90, 34, 12, 18],
                     [-5, 9, 11, 12, 18, 23, 34, 90],
                     id="Positive and negative integers"),
        pytest.param([0.7983617310883225,
                      0.497852313467696,
                      0.9221591948947656,
                      0.8343150534461211,
                      0.12838290837484168,
                      0.13730090553354302,
                      0.816107991192677,
                      0.08228522754432144,
                      0.3656202087210071,
                      0.12232237545477109],
                     [0.08228522754432144,
                      0.12232237545477109,
                      0.12838290837484168,
                      0.13730090553354302,
                      0.3656202087210071,
                      0.497852313467696,
                      0.7983617310883225,
                      0.816107991192677,
                      0.8343150534461211,
                      0.9221591948947656],
                     id="Positive floats"),
        pytest.param([-0.37431728386808927,
                      0.26332771509528924,
                      1.8598142094732752,
                      -2.6399126565833146,
                      1.8216410360959885,
                      0.3992117963124119,
                      -0.6140237133525823,
                      0.4082533273929591,
                      -0.278978634049326,
                      -0.8131302305889101],
                     [-2.6399126565833146,
                      -0.8131302305889101,
                      -0.6140237133525823,
                      -0.37431728386808927,
                      -0.278978634049326,
                      0.26332771509528924,
                      0.3992117963124119,
                      0.4082533273929591,
                      1.8216410360959885,
                      1.8598142094732752],
                     id="Positive and negative floats")]
)
def test_bubble_sort(unsorted_numbers: list, sorted_numbers: list):
    assert golem.bubble_sort(numbers=unsorted_numbers.copy()) == sorted_numbers
    assert cython_golem.bubble_sort(unsorted_numbers.copy()) == sorted_numbers
    assert fast.bubble_sort(numbers=unsorted_numbers.copy()) == sorted_numbers
    assert cython_fast.bubble_sort(unsorted_numbers.copy()) == sorted_numbers
    assert list_comprehension.bubble_sort(numbers=unsorted_numbers.copy()) == sorted_numbers
    assert python_sorted.python_internal_sorted(numbers=unsorted_numbers.copy()) == sorted_numbers
    # Special assert for numpy array comparison
    assert (jit.bubble_sort(numbers=np.array(unsorted_numbers.copy())) == np.array(sorted_numbers)).all()
