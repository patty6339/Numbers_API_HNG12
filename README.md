# Numbers API

## Project Overview

Numbers API is a FastAPI-powered microservice that provides comprehensive number classification and interesting mathematical insights. This API allows you to explore the unique properties of any integer while fetching an entertaining mathematical fact.

## Features

- 🔢 Number Classification
  - Determine if a number is:
    - Prime
    - Perfect
    - Armstrong number
  - Identify number properties (even/odd)
  - Calculate digit sum

- 🧠 Fun Facts
  - Retrieve an interesting mathematical fact about the number using the Numbers API

## Technologies Used

- **Framework**: FastAPI
- **Language**: Python 3.8+
- **Dependencies**: 
  - fastapi
  - uvicorn
  - httpx
  - pydantic

## API Endpoint

**GET** `/api/classify-number`

### Query Parameters
- `number`: Integer to classify (required)

### Response Format

**Success (200 OK)**:
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

**Error (400 Bad Request)**:
```json
{
    "number": "alphabet",
    "error": true,
    "message": "Input must be a valid integer"
}
```

## Local Setup

1. Clone the repository
```bash
git clone https://github.com/yourusername/numbers-api.git
cd numbers-api
```

2. Create virtual environment
```bash
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the server
```bash
uvicorn app.main:app --reload
```

## Deployment

- **Platform**: Vercel
- **Base URL**: https://numbers-api-hng-12.vercel.app
- **Endpoints**:
  - Classify Number: `GET /api/classify-number?number=371`
  - Swagger Docs: `/docs`
  - ReDoc: `/redoc`

### Example API Calls

1. Classify Number 371:
```bash
curl https://numbers-api-hng-12.vercel.app/api/classify-number?number=371
```

2. Browser Access:
- Open https://numbers-api-hng-12.vercel.app/api/classify-number?number=371
- Or visit https://numbers-api-hng-12.vercel.app/docs for interactive documentation

## Frontend Demo

A simple, interactive frontend has been created to demonstrate the Numbers Classification API.

### Features
- Responsive design
- Real-time number classification
- Loading spinner
- Error handling
- Displays detailed number properties

### Technologies Used
- HTML5
- CSS3
- Vanilla JavaScript

### How to Use
1. Enter a number in the input field
2. Click "Classify Number"
3. View the number's mathematical properties and fun fact

### Deployment
The frontend can be easily deployed on platforms like Vercel, Netlify, or GitHub Pages.

### Screenshots
[Add screenshots of your frontend demo here]

## Testing

- Swagger UI: `/docs`
- ReDoc: `/redoc`

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[Choose an appropriate license, e.g., MIT]