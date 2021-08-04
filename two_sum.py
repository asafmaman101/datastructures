from itertools import product
from collections import defaultdict


def two_sum(arr, target):
    if not arr: return []
    assert isinstance(target, int)

    result = set()
    hash_table = defaultdict(list)

    for i, num in enumerate(arr):
        hash_table[num].append(i)

    for i, num in enumerate(arr):
        for j in hash_table[target - num]:
            if i != j:
                found = [i, j]
                found.sort()
                found = tuple(found)
                result.add(found)

    return list(result)


