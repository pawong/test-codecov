def check_is_prime(integer: int):
    """Check if the number is prime endpoint"""
    if integer == 2:
        return True
    if integer > 2:
        for i in range(2, int(integer ** (1 / 2)) + 1):
            if integer / i == float(integer // i):
                return False
        return True
    return None
