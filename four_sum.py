from collections import defaultdict
from typing import List


def four_sum(nums: List[int], target: int) -> List[List[int]]:

    sums = defaultdict(list)
    result = set()
    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums[i + 1:]):
            sums[num1 + num2].append((i, i+j+1))

    for sum1, i_list in list(sums.items()):
        j_list = sums[target - sum1]
        for tup1 in i_list:
            for tup2 in j_list:
                if len(set(tup1 + tup2)) == 4:
                    res = list(tup1 + tup2)
                    res.sort()
                    res = tuple(res)
                    result.add(res)

    new_res = []
    for i1, i2, i3, i4 in list(result):
        new_res.append([nums[i1], nums[i2], nums[i3], nums[i4]])

    new_res = set(map(lambda x: tuple(x), new_res))
    new_res = list(map(lambda x: list(x), new_res))

    return list(new_res)


