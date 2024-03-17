import pytest


def reverse_vowels(s: str) -> str:
    vowels = "aeiou"
    indices = []
    arr = [" "] * len(s)
    for i, c in enumerate(s):
        if c.lower() in vowels:
            indices.append(i)
        arr[i] = c
    length = len(indices)
    for i in range(length // 2):
        index1, index2 = indices[i], indices[length - i - 1]
        tmp = arr[index1]
        arr[index1] = arr[index2]
        arr[index2] = tmp
    return "".join(arr)


@pytest.mark.parametrize(
    "s,expected",
    [
        ("hello", "holle"),
        ("Ae", "eA"),
        ("leetcode", "leotcede"),
        ("", ""),
        ("i", "i"),
        ("aei", "iea"),
        ("aEiO", "OiEa"),
    ],
)
def test_reverse_vowels(s, expected):
    assert reverse_vowels(s) == expected
