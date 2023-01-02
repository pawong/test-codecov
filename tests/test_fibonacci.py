from src.fibonacci import fibonacci


def test_fibonacci_less_than_3():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2


def test_fibonacci_large_value():
    assert fibonacci(100) == 354224848179261915075
