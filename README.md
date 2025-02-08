# Number Classification API

This is a Flask-based API that classifies a given number and provides interesting mathematical properties, such as whether the number is prime, perfect, or an Armstrong number. It also includes a fun fact about the number using the Numbers API.

## Features

### Number Classification:
- Checks if the number is prime.
- Checks if the number is perfect.
- Checks if the number is an Armstrong number.
- Determines if the number is even or odd.
- Calculates the sum of the digits of the number.

### Fun Fact:
- Retrieves a fun fact about the number using the Numbers API.

### Input Validation:
- Accepts both integer and floating-point numbers.
- Handles negative numbers.
- Returns a `400 Bad Request` for invalid inputs.

## API Endpoint

### **GET** `/api/classify-number?number=<number>`

#### Parameters
- `number`: The number to classify (can be an integer, floating-point, or negative number).

### Response (`200 OK`)
```json
{
    "number": 153,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 9,
    "fun_fact": "153 is the smallest number which can be expressed as the sum of cubes of its digits."
}
```

### Response (`400 Bad Request`)
```json
{
    "number": "abc",
    "error": true
}
```

## How to Run the API

### Prerequisites
- Python 3.x
- Flask (`pip install flask`)
- Requests (`pip install requests`)

### Steps
1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-folder>
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the Flask application:
```bash
python app.py
```
4. The API will be available at:
```bash
http://localhost:5000/api/classify-number?number=<your-number>
```

## Example Requests

### Integer
```bash
curl "http://localhost:5000/api/classify-number?number=153"
```
**Response:**
```json
{
    "number": 153,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 9,
    "fun_fact": "153 is the smallest number which can be expressed as the sum of cubes of its digits."
}
```

### Floating-Point Number
```bash
curl "http://localhost:5000/api/classify-number?number=12.2"
```
**Response:**
```json
{
    "number": 12.2,
    "is_prime": false,
    "is_perfect": false,
    "properties": [],
    "digit_sum": 5,
    "fun_fact": "No interesting fact available."
}
```

### Negative Number
```bash
curl "http://localhost:5000/api/classify-number?number=-371"
```
**Response:**
```json
{
    "number": -371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "-371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371."
}
```

### Invalid Input
```bash
curl "http://localhost:5000/api/classify-number?number=abc"
```
**Response:**
```json
{
    "number": "abc",
    "error": true
}
```

## Deployment

### Local Deployment
Run the Flask application using:
```bash
python app.py
```

### Production Deployment
Use a production-ready server like Gunicorn:
```bash
pip install gunicorn
gunicorn app:app
```
Deploy to a cloud platform like AWS, Heroku, or Render.

## Code Structure
- `app.py`: The main Flask application.
- `classify_number`: The API endpoint that classifies the number.
- `is_prime`: Checks if a number is prime.
- `is_perfect`: Checks if a number is perfect.
- `is_armstrong`: Checks if a number is an Armstrong number.
- `calculate_digit_sum`: Calculates the sum of the digits of a number.
- `get_fun_fact`: Retrieves a fun fact about the number using the Numbers API.

## Dependencies
- **Flask**: Web framework for Python.
- **Requests**: HTTP library for making API requests to Numbers API.

## Contributing
1. Fork the repository.
2. Create a new branch:
```bash
git checkout -b feature/your-feature-name
```
3. Commit your changes:
```bash
git commit -m "Add your feature"
```
4. Push to the branch:
```bash
git push origin feature/your-feature-name
```
5. Open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- **Numbers API** for providing fun facts about numbers.
- **Flask** for the web framework.

