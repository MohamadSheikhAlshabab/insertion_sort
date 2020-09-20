from insertion_sort import __version__
from insertion_sort.insertion_sort import insertion_sort

def test_version():
    assert __version__ == '0.1.0'

def test_insertion_sort_1():
    arr = [20, 18, 12, 8, 5, -2]
    expected = [-2, 5, 8, 12, 18, 20]
    actual = insertion_sort(arr)
    assert actual == expected

def test_insertion_sort_2():
    arr = [5,12,7,5,5,7]
    expected = [5,5,5,7,7,12]
    actual = insertion_sort(arr)
    assert actual == expected

def test_insertion_sort_3():
    arr = [2,3,5,7,13,11]
    expected = [2,3,5,7,11,13]
    actual = insertion_sort(arr)
    assert actual == expected

def test_insertion_sort_4():
    arr = " "
    expected = None
    actual = insertion_sort(arr)
    assert actual == expected
