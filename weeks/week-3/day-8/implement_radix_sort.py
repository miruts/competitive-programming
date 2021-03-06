from typing import List
from functools import cmp_to_key


def radix_sort(nums: List[int]) -> List[int]:
    mx = len(str(max(nums)))
    for i in range(1, mx + 1):
        nums = sorted(nums, key=cmp_to_key(predicate_to_compare(i)))
    return nums


# Method generates compare function based on radix
def predicate_to_compare(r):
    def compare(x, y):
        if x % (10 ** r) > y % (10 ** r):
            return 1
        elif x % (10 ** r) < y % (10 ** r):
            return -1
        return 0

    return compare


print(radix_sort([4, 3, 5, 66, 777, 88, 90, 100]))


def radix(nums: List[int]) -> List[int]:
    temp = [[]] * 10
    mx = len(str(max(nums)))
    for i in range(1, mx + 1):
        for n in nums:
            i_d = n % (10 ** i)
            i_d = int(str(i_d)[0])
            print(i_d)
            temp[i_d].append(n)
        print(temp)


print(radix([1, 5, 5, 5, 555]))
