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
- **HTTP Client**: httpx
- **Server**: Uvicorn

## Prerequisites

- Python 3.8+
- pip (Python Package Manager)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/numbers-api.git
   cd numbers-api
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

### Development Mode
```bash
uvicorn app.main:app --reload
```

### Production Mode
```bash
uvicorn app.main:app
```

The API will be available at `http://localhost:8000`

## API Endpoint

### Classify Number
- **Endpoint**: `/api/classify-number`
- **Method**: GET
- **Query Parameter**: `number` (integer)

#### Example Request
```
GET /api/classify-number?number=153
```

#### Example Response
```json
{
  "number": 153,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 9,
  "fun_fact": "153 is an Armstrong number!"
}
```

## Project Structure
```
numbers_api/
│
├── app/
│   ├── main.py        # FastAPI application
│   └── utils.py       # Number classification utilities
│
├── requirements.txt   # Project dependencies
└── README.md          # Project documentation
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Your Name - patty6339@gmail.com

Project Link: [https://github.com/patty6339/numbers-api](See the Project)