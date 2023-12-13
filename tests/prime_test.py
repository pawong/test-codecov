from src.prime import check_is_prime


def test_prime_less_than_2():
    assert check_is_prime(1) is None


def test_prime_large_value():
    assert check_is_prime(1001) is False


def test_prime_first_ten():
    assert check_is_prime(2) is True
    assert check_is_prime(3) is True
    assert check_is_prime(4) is False
    assert check_is_prime(5) is True
    assert check_is_prime(6) is False
    assert check_is_prime(7) is True
    assert check_is_prime(8) is False
    assert check_is_prime(9) is False
    assert check_is_prime(10) is False
    assert check_is_prime(11) is True
