from src.strings_for_digits import strings_for_digits


def test_empty():
    assert strings_for_digits([]) == []


def test_one_digit():
    assert strings_for_digits([0]) == ["-0-"]
    assert strings_for_digits([1]) == ["-1-"]
    assert strings_for_digits([2]) == ["A", "B", "C"]
    assert strings_for_digits([3]) == ["D", "E", "F"]
    assert strings_for_digits([4]) == ["G", "H", "I"]
    assert strings_for_digits([5]) == ["J", "K", "L"]
    assert strings_for_digits([6]) == ["M", "N", "O"]
    assert strings_for_digits([7]) == ["P", "Q", "R", "S"]
    assert strings_for_digits([8]) == ["T", "U", "V"]
    assert strings_for_digits([9]) == ["W", "X", "Y", "Z"]


def test_comfy():
    assert "COMFY" in strings_for_digits([2, 6, 6, 3, 9])
