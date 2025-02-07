# Number Classification API

A FastAPI-based REST API that analyzes numbers and returns their mathematical properties along with fun facts.

## Features

- Determines if a number is prime
- Determines if a number is perfect
- Identifies Armstrong numbers
- Calculates digit sum
- Provides number properties (odd/even, Armstrong)
- Includes fun mathematical facts about numbers

## API Specification

### Endpoint

```
GET /api/classify-number?number={number}
```

### Success Response (200 OK)

```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

### Error Response (400 Bad Request)

```json
{
    "number": "alphabet",
    "error": true
}
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/number-classifier-api.git
cd number-classifier-api
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install fastapi uvicorn requests
```

## Running Locally

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## Deployment

This API can be deployed to any platform that supports Python applications. Some recommended platforms:

- Heroku
- DigitalOcean
- Railway
- Render

## Testing

You can test the API using curl:

```bash
curl "http://localhost:8000/api/classify-number?number=371"
```

Or using the built-in Swagger UI at `/docs`

## Technologies Used

- Python 3.8+
- FastAPI
- Uvicorn
- Numbers API (for fun facts)

## License

MIT
