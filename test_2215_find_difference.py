# flake8: noqa
import pytest


def find_difference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    s1, s2 = set(nums1), set(nums2)
    return [
        list(s1.difference(s2)),
        list(s2.difference(s1)),
    ]


@pytest.mark.parametrize(
    "nums1,nums2,expected",
    [
        ([], [], [[], []]),
        ([1,2,3], [2,4,6], [[1,3], [4,6]]),
    ],
)
def test_find_difference(nums1, nums2, expected):
    assert find_difference(nums1, nums2) == expected
