from sort_and_search import binary_search, merge_sort


def test_binary_search():
    arr = []
    arr.sort()
    res = binary_search(arr, 7)
    assert res == -1

    arr = [1]
    arr.sort()
    res = binary_search(arr, 7)
    assert res == -1

    arr = [7]
    arr.sort()
    res = binary_search(arr, 7)
    assert res == 0

    arr = [25, 94, 1, 52, 79, 76, 26, 65, 65, 35, 24, 80, 47, 72, 85, 44, 72, 98, 96, 54]
    arr.sort()
    item_index = 7
    res = binary_search(arr, arr[item_index])
    assert res == item_index

    arr = [25, 94, 1, 52, 79, 76, 26, 65, 65, 35, 24, 80, 47, 72, 85, 44, 72, 98, 96, 54]
    arr.sort()
    res = binary_search(arr, 58)
    assert res == -1

    arr = [25, 94, 1, 52, 79, 76, 26, 65, 65, 35, 24, 80, 47, 72, 85, 44, 72, 98, 96, 54]
    arr.sort()
    item_index = 0
    res = binary_search(arr, arr[item_index])
    assert res == item_index

    arr = [25, 94, 1, 52, 79, 76, 26, 65, 65, 35, 24, 80, 47, 72, 85, 44, 72, 98, 96, 54]
    arr.sort()
    item_index = len(arr) - 1
    res = binary_search(arr, arr[item_index])
    assert res == item_index

    arr = [25, 94, 1, 52, 79, 76, 26, 65, 65, 35, 24, 80, 47, 72, 85, 44, 72, 98, 96, 54]
    arr.sort()
    res = binary_search(arr, 200)
    assert res == -1

    arr = [25, 94, 1, 52, 79, 76, 26, 65, 65, 35, 24, 80, 47, 72, 85, 44, 72, 98, 96, 54]
    arr.sort()
    res = binary_search(arr, -100)
    assert res == -1


def test_merge_sort():
    arr = []
    arr = merge_sort(arr)
    assert arr == []

    arr = [1]
    arr = merge_sort(arr)
    assert arr == [1]

    arr = [1, 2, 3]
    arr = merge_sort(arr)
    assert arr == [1, 2, 3]

    arr = [3, 2, 1]
    arr = merge_sort(arr)
    assert arr == [1, 2, 3]

    arr = [1, 1, 1, 1]
    arr = merge_sort(arr)
    assert arr == [1, 1, 1, 1]

    arr = [1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 2, 2, 2, 1, 2]
    sorted_arr = merge_sort(arr)
    arr.sort()
    assert sorted_arr == arr

    arr = [936, 925, 831, 993, 20, 527, 64, 217, 87, 420, 846, 163, 663, 74, 716, 240, 632, 839, 934, 651]
    sorted_arr = merge_sort(arr)
    arr.sort()
    assert sorted_arr == arr

    arr = [65.2617424133577, 58.16191219090544, 7.791779354128014, 71.64766643282825, 53.36858611924258,
           99.33160372308086, 9.126020414169822, 42.789743016538495, 42.349632204355146, 61.30765991891051]
    sorted_arr = merge_sort(arr)
    arr.sort()
    assert sorted_arr == arr
