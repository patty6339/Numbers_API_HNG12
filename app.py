from flask import Flask, jsonify, request
import requests
import math

app = Flask(__name__)

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    num = request.args.get('number')
    
    try:
        num = float(num)
        if num.is_integer():
            num = int(num)
        else:
            return jsonify({"number": num, "error": True}), 400
    except (ValueError, TypeError):
        return jsonify({"number": num, "error": True}), 400
    
    properties = []
    if num % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")
    if is_armstrong(num):
        properties.insert(0, "armstrong")
    
    fun_fact = get_fun_fact(num)
    
    response_data = {
        "number": num,
        "is_prime": is_prime(num),
        "is_perfect": is_perfect(num),
        "properties": properties,
        "digit_sum": sum(int(d) for d in str(abs(num))),
        "fun_fact": fun_fact
    }
    
    return jsonify(response_data), 200

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    if n <= 0:  # 0 and negative numbers are not perfect numbers
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

def is_armstrong(n):
    return sum(int(d) ** len(str(n)) for d in str(abs(n))) == n

def get_fun_fact(n):
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math?json")
        if response.status_code == 200:
            return response.json().get("text", "No interesting fact available.")
    except requests.exceptions.RequestException:
        pass
    return "No interesting fact available."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
