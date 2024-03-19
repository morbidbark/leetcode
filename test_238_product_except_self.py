# flake8: noqa
import pytest


def product_except_self(nums: list[int]) -> list[int]:
    lnums = len(nums)
    prefix = [0] * lnums
    prod = 1
    for i, n in enumerate(nums):
        prod *= n
        prefix[i] = prod
    prod = 1
    suffix = [0] * lnums
    for i in range(lnums-1, -1, -1):
        n = nums[i]
        prod *= n
        suffix[i] = prod
    result = [0] * lnums
    result[0] = suffix[1]
    for i in range(1, lnums - 1):
        result[i] = prefix[i-1] * suffix[i+1]
    result[lnums-1] = prefix[lnums-2]
    return result


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1,2,3,4], [24,12,8,6]),
        ([-1,1,0,-3,3], [0,0,9,0,0]),
    ],
)
def test_product_except_self(nums, expected):
    assert product_except_self(nums) == expected
