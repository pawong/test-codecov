"""
Given a sequence of number, find all the strings that could be made by pressing
those numbers on an (old) phone's keypad.

As a reference, this is the list of characters you can get for each key:

+-----+------------+
| Key |  Letters   |
+-----+------------+
|   0 | N/A        |
|   1 | N/A        |
|   2 | A, B, C    |
|   3 | D, E, F    |
|   4 | G, H, I    |
|   5 | J, K, L    |
|   6 | M, N, O    |
|   7 | P, Q, R, S |
|   8 | T, U, V    |
|   9 | W, X, Y, Z |
+-----+------------+

Feel free to use this to save you some time:
{
    2: ["A", "B", "C"],
    3: ["D", "E", "F"],
    4: ["G", "H", "I"],
    5: ["J", "K", "L"],
    6: ["M", "N", "O"],
    7: ["P", "Q", "R", "S"],
    8: ["T", "U", "V"],
    9: ["W", "X", "Y", "Z"],
}
"""
from itertools import product


def strings_for_digits(digits):
    b = {
        0: ["-0-"],
        1: ["-1-"],
        2: ["A", "B", "C"],
        3: ["D", "E", "F"],
        4: ["G", "H", "I"],
        5: ["J", "K", "L"],
        6: ["M", "N", "O"],
        7: ["P", "Q", "R", "S"],
        8: ["T", "U", "V"],
        9: ["W", "X", "Y", "Z"],
    }

    if len(digits) == 0:
        return []

    p = []
    for d in digits:
        p.append(b[d])

    words = []
    for c in list(product(*p)):
        if len(c):
            words.append("".join(c))

    return words
