import pytest


def remove_stars(s: str) -> str:
    arr = []
    count = 0
    for i, c in enumerate(reversed(s)):
        if c == "*":
            count += 1
        elif count:
            count -= 1
        else:
            arr.append(c)
    return "".join(reversed(arr))


@pytest.mark.parametrize(
    "s,expected",
    [
        ("leet**cod*e", "lecoe"),
        ("erase*****", ""),
        ("", ""),
        ("ab*", "a"),
    ],
)
def test_remove_stars(s, expected):
    assert remove_stars(s) == expected
