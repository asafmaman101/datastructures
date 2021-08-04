def binary_search(arr: list, item) -> int:
    if not arr: return -1

    left, right = 0, len(arr)

    while left != right - 1:
        middle = (left + right) // 2
        if arr[middle] == item: return middle
        elif arr[middle] > item: right = middle
        else: left = middle

    if arr[left] == item: return left

    return -1


def merge_sort(arr: list) -> list:

    if not arr: return []
    if len(arr) == 1: return arr

    left, right = 0, len(arr)
    middle = (right + left) // 2

    arr[left:middle] = merge_sort(arr[left:middle])
    arr[middle:right] = merge_sort(arr[middle:right])

    i, j = left, middle
    new_arr = []
    while i < middle and j < right:
        if arr[i] <= arr[j]:
            new_arr.append(arr[i])
            i += 1
        elif arr[i] > arr[j]:
            new_arr.append(arr[j])
            j += 1

    if i < middle:
        new_arr += arr[i:middle]
    elif j < right:
        new_arr += arr[j:right]

    return new_arr