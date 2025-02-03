def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_perfect(n: int) -> bool:
    """Check if a number is a perfect number."""
    return sum(i for i in range(1, n) if n % i == 0) == n


def is_armstrong(n: int) -> bool:
    """Check if a number is an Armstrong number."""
    digits = [int(d) for d in str(n)]
    return sum(d ** len(digits) for d in digits) == n


def classify_number(number: int) -> dict:
    """Classifies the number with its mathematical properties."""
    properties = []
    
    if is_armstrong(number):
        properties.append("armstrong")

    properties.append("odd" if number % 2 else "even")

    return {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": sum(int(d) for d in str(number))
    }
