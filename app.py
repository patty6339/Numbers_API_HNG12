from flask import Flask, jsonify, request
import requests
import math

app = Flask(__name__)

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    num = request.args.get('number')
    
    # Input validation
    try:
        num = float(num)  # Accept floating-point numbers
        is_integer = num.is_integer()  # Check if the number is an integer
        if is_integer:
            num = int(num)  # Convert to integer if it's a whole number
    except (ValueError, TypeError):
        return jsonify({"number": num, "error": True}), 400
    
    # Calculate properties
    properties = []
    if is_integer and num % 2 == 0:
        properties.append("even")
    elif is_integer:
        properties.append("odd")
    
    if is_integer and is_armstrong(num):
        properties.insert(0, "armstrong")
    
    # Prepare response
    response_data = {
        "number": num,
        "is_prime": is_prime(abs(num)) if is_integer else False,  # Primes are only defined for positive integers
        "is_perfect": is_perfect(abs(num)) if is_integer else False,  # Perfect numbers are only defined for positive integers
        "properties": properties,
        "digit_sum": sum(int(d) for d in str(abs(num))),  # Handle negative numbers
        "fun_fact": get_fun_fact(num)
    }
    
    return jsonify(response_data), 200

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    """Check if a number is a perfect number."""
    if n < 2:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

def is_armstrong(n):
    """Check if a number is an Armstrong number."""
    digits = [int(d) for d in str(abs(n))]  # Handle negative numbers
    num_digits = len(digits)
    return sum(d ** num_digits for d in digits) == abs(n)

def get_fun_fact(n):
    """Generate a fun fact about the number."""
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math?json")
        if response.status_code == 200:
            return response.json().get("text", "No interesting fact available.")
    except requests.exceptions.RequestException:
        pass
    return "No interesting fact available."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
