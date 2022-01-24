import pyximport
pyximport.install()


try:
    import src.bubblesort.random_number_list as random_number_list
    from src.bubblesort.clibs import cython_golem
except ModuleNotFoundError:
    import random_number_list as random_number_list
    from clibs import cython_golem

if __name__ == "__main__":
    cython_golem.bubble_sort(random_number_list.read())
