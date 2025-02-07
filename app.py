from flask import Flask, request, jsonify
from flask_cors import CORS
import math

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Numbers API!"}), 200

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

def digit_sum(n):
    """Calculate the sum of the digits of a number."""
    return sum(int(d) for d in str(abs(n)))  # Handle negative numbers

def get_fun_fact(n):
    """Generate a fun fact about the number."""
    if is_armstrong(n):
        return f"{n} is an Armstrong number because {' + '.join(f'{d}^{len(str(abs(n)))}' for d in str(abs(n)))} = {abs(n)}"
    return f"{n} is a fascinating number with unique mathematical properties."

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')
    
    # Input validation
    try:
        # Convert the input to a float first, then to an integer if it's a whole number
        number = float(number)
        if number.is_integer():
            number = int(number)
    except (ValueError, TypeError):
        return jsonify({
            "number": number if number else "None",
            "error": True
        }), 400
    
    # Calculate properties
    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    if number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")
    
    # Prepare response
    response = {
        "number": number,
        "is_prime": is_prime(abs(number)) if isinstance(number, int) else False,  # Primes are only defined for integers
        "is_perfect": is_perfect(abs(number)) if isinstance(number, int) else False,  # Perfect numbers are only defined for integers
        "properties": properties,
        "digit_sum": digit_sum(number),
        "fun_fact": get_fun_fact(number)
    }
    
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)