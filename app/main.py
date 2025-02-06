from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import httpx
import sys
import os
import math
import re

# Add the parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.utils import is_prime, is_perfect, is_armstrong

app = FastAPI(
    title="Numbers Classification API",
    description="An API to classify numbers based on various mathematical properties",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

NUMBERS_API_URL = "http://numbersapi.com/{number}/math"

@app.get("/")
async def root():
    """
    Root endpoint providing basic API information.
    """
    return JSONResponse(content={
        "message": "Welcome to the Numbers Classification API",
        "endpoints": {
            "/api/classify-number": "Classify a number's mathematical properties",
            "/docs": "Swagger UI for API documentation",
            "/redoc": "ReDoc for API documentation"
        }
    })

@app.get("/api/classify-number")
async def classify_number_api(number: str = Query(..., description="Number to classify")):
    # Validate input format first
    if not re.match(r'^-?\d+$', number):
        return JSONResponse(status_code=400, content={
            "number": number,
            "error": True,
            "message": "Input must be an integer"
        })

    try:
        # Convert to integer
        n = int(number)

        # Prepare properties list
        properties = []
        abs_n = abs(n)
        
        if is_armstrong(abs_n):
            properties.append("armstrong")
        properties.append("odd" if abs_n % 2 else "even")

        # Fetch fun fact asynchronously
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(NUMBERS_API_URL.format(number=abs_n), timeout=5.0)
                fun_fact = response.text if response.status_code == 200 else f"{n} has no interesting fact available"
            except httpx.RequestError:
                fun_fact = f"{n} has no interesting fact available due to network error"

        # Build response
        return JSONResponse(content={
            "number": n,
            "is_prime": is_prime(abs_n),
            "is_perfect": is_perfect(abs_n),
            "properties": properties,
            "digit_sum": sum(int(d) for d in str(abs_n)),
            "fun_fact": fun_fact
        })

    except Exception as e:
        return JSONResponse(status_code=500, content={
            "error": True,
            "message": "Unexpected server error"
        })
