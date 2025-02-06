# Numbers Classification API

## Overview
This is a FastAPI-based Numbers Classification API that provides interesting mathematical properties about a given number.

## Features
- Classify numbers based on mathematical properties
- Get fun facts about numbers
- Supports various number classifications:
  - Prime numbers
  - Perfect numbers
  - Armstrong numbers
  - Odd/Even numbers

## Endpoint
`GET /api/classify-number?number={number}`

### Response Format (200 OK)
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

### Response Format (400 Bad Request)
```json
{
    "number": "alphabet",
    "error": true,
    "message": "Input must be a valid integer"
}
```

## Setup and Installation

### Prerequisites
- Python 3.8+
- pip

### Installation
1. Clone the repository
```bash
git clone https://github.com/yourusername/Numbers_API_HNG12.git
cd Numbers_API_HNG12
```

2. Create a virtual environment
```bash
python -m venv myenv
source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the application
```bash
uvicorn app.main:app --reload
```

## Deployment
Deployed on Vercel: https://numbers-api-hng-12.vercel.app

## Deployment Troubleshooting
If you encounter deployment issues:
1. Ensure all dependencies are listed in `requirements.txt`
2. Check Vercel configuration in `vercel.json`
3. Verify Python runtime version compatibility
4. Make sure all necessary files are included in the deployment

### Common Deployment Errors
- **Import Errors**: Ensure absolute imports are used
- **Path Issues**: Add parent directory to Python path
- **Missing Files**: Include all necessary files in Vercel config

### Debugging Deployment
- Use Vercel CLI to test deployment locally
- Check Vercel deployment logs for specific error messages

### Recommended Vercel Setup
- Runtime: Python 3.10
- Build Command: `pip install -r requirements.txt`
- Output Directory: Leave blank for Python/FastAPI
- Install Command: `pip install -r requirements.txt`

## Technologies
- FastAPI
- Python
- httpx (for async HTTP requests)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)

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

### Frontend Deployment

The frontend is deployed and accessible at:
- 🌍 Frontend URL: https://numbers-api-frontend-9i9xqtob1-patdevops-projects.vercel.app

### How to Use
1. Visit the frontend URL
2. Enter a number in the input field
3. Click "Classify Number"
4. View detailed number properties and fun facts!

## Testing

- Swagger UI: `/docs`
- ReDoc: `/redoc`