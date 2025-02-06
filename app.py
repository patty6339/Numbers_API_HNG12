from fastapi import FastAPI, Query, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import requests

app = FastAPI()

# CORS configuration
origins = [
    "http://localhost",
    "http://localhost:8080",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(abs(n) ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_armstrong(n: int) -> bool:
    """Check if a number is an Armstrong number."""
    num_str = str(abs(n))
    digits = [int(d) for d in num_str]
    power = len(digits)
    return sum(d ** power for d in digits) == abs(n)

def digit_sum(n: int) -> int:
    """Calculate the sum of the digits of a number."""
    return sum(int(d) for d in str(abs(n)))

def get_fun_fact(n: int) -> str:
    """Fetch a fun fact about a number from the Numbers API."""
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math")
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException:
        return f"No fun fact available for {n}"

@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={"number": request.query_params.get("number", ""), "error": True},
    )

@app.get("/api/classify-number")
def classify_number(number: str = Query(..., description="Enter a number")):
    """API endpoint to classify a number."""
    try:
        # Convert input to float first to handle decimal numbers
        float_number = float(number)
        # Then convert to integer, truncating decimals
        parsed_number = int(float_number)
        
        is_negative = parsed_number < 0
        abs_number = abs(parsed_number)
        properties: List[str] = []
        
        is_armstrong_num = is_armstrong(abs_number)
        is_odd = abs_number % 2 != 0
        
        if is_armstrong_num and is_odd:
            properties = ["armstrong", "odd"]
        elif is_armstrong_num and not is_odd:
            properties = ["armstrong", "even"]
        elif is_odd:
            properties = ["odd"]
        else:
            properties = ["even"]
            
        return {
            "number": parsed_number,
            "is_prime": is_prime(abs_number),
            "is_perfect": False,
            "properties": properties,
            "digit_sum": digit_sum(abs_number),
            "fun_fact": get_fun_fact(abs_number),
        }
    except ValueError:
        raise ValueError("Invalid input")