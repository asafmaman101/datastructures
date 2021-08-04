from two_sum import two_sum


def test_two_sum():
    arr = []
    target = 2
    assert two_sum(arr, target) == []

    arr = [1,2,3]
    target = 4
    expected = [(0,2)]
    assert two_sum(arr, target) == expected

    arr = []
    target = 2
    expected = []
    assert two_sum(arr, target) == expected

    arr = []
    target = 2
    expected = []
    assert two_sum(arr, target) == expected

    arr = []
    target = 2
    expected = []
    assert two_sum(arr, target) == expected
