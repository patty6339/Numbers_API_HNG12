from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import httpx
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
    return {
        "message": "Welcome to the Numbers Classification API",
        "endpoints": {
            "/api/classify-number": "Classify a number's mathematical properties",
            "/docs": "Swagger UI for API documentation",
            "/redoc": "ReDoc for API documentation"
        }
    }

@app.get("/api/classify-number")
async def classify_number_api(number: str = Query(..., description="Number to classify")):
    try:
        # Validate input is a valid integer
        try:
            n = int(number)
        except ValueError:
            raise HTTPException(status_code=400, detail={
                "number": number,
                "error": True,
                "message": "Input must be a valid integer"
            })

        # Prepare properties list
        properties = []
        if is_armstrong(n):
            properties.append("armstrong")
        properties.append("odd" if n % 2 else "even")

        # Fetch fun fact asynchronously
        async with httpx.AsyncClient() as client:
            response = await client.get(NUMBERS_API_URL.format(number=n))
            fun_fact = response.text if response.status_code == 200 else f"{n} has no interesting fact available"

        # Build response
        return {
            "number": n,
            "is_prime": is_prime(n),
            "is_perfect": is_perfect(n),
            "properties": properties,
            "digit_sum": sum(int(d) for d in str(n)),
            "fun_fact": fun_fact
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail={
            "error": True,
            "message": str(e)
        })
