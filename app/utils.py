def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    n = abs(int(n))  # Ensure positive integer
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_perfect(n: int) -> bool:
    """Check if a number is a perfect number."""
    n = abs(int(n))  # Ensure positive integer
    return sum(i for i in range(1, n) if n % i == 0) == n


def is_armstrong(n: int) -> bool:
    """Check if a number is an Armstrong number."""
    n = abs(int(n))  # Ensure positive integer
    digits = [int(d) for d in str(n)]
    return sum(d ** len(digits) for d in digits) == n
