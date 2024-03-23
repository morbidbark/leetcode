# flake8: noqa
import pytest


def increasing_triplet(nums: list[int]) -> bool:
    lnums = len(nums)

    tracker = 2 ** 31 - 1
    lower = [False] * lnums
    for i, num in enumerate(nums):
        if num <= tracker:
            tracker = num
        else:
            lower[i] = True

    tracker = -2 ** 31
    for i, num in enumerate(reversed(nums)):
        if num >= tracker:
            tracker = num
        elif lower[lnums - 1 - i]:
            return True
    return False


@pytest.mark.parametrize(
    "nums,expected",
    (
        ([1,2,3,4,5], True),
        ([5,4,3,2,1], False),
        ([2,1,5,0,4,6], True),
        ([3,2,6,4,5], True),
        ([1,1,1,1,1,1,1], False),
        ([20,100,10,12,5,13], True),
    ),
)
def test_increasing_triplet(nums, expected):
    assert increasing_triplet(nums) == expected
