from fastapi import FastAPI, Query
import httpx
from app.utils import classify_number

app = FastAPI()

NUMBERS_API_URL = "http://numbersapi.com/{number}/math"


@app.get("/api/classify-number")
async def classify_number_api(number: int = Query(..., description="Number to classify")):
    try:
        # Get number properties
        classification = classify_number(number)

        # Fetch fun fact asynchronously
        async with httpx.AsyncClient() as client:
            response = await client.get(NUMBERS_API_URL.format(number=number))
            fun_fact = response.text if response.status_code == 200 else "No fun fact available"

        # Build response
        classification["fun_fact"] = fun_fact
        return classification

    except Exception as e:
        return {"error": True, "message": str(e)}


