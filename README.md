# Numbers Classification API

A versatile Flask-based API that classifies numbers and provides fun facts about them. It can be deployed locally or on AWS Lambda.

## Project Structure
```
├── .dist/                   # Directory for distribution files
├── app.py                   # Local Flask application
├── lambda_function.py       # AWS Lambda function handler
├── README.md                # Project documentation
└── requirements.txt         # Dependencies for local and cloud deployment
```

## Deployment Options

### 1. Local Flask Deployment

#### Setup and Installation
```sh
# Clone the repository
git clone https://github.com/patty6339/numbers_api.git
cd numbers_api

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Unix/macOS
venv\Scripts\activate     # On Windows

# Install dependencies
pip install -r requirements.txt
```

#### Running the Application
```sh
# Start the Flask development server
flask run
```
Access the API at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

### 2. AWS Lambda Deployment

#### Prerequisites
- AWS Account
- AWS CLI configured
- AWS Lambda function created

#### Deployment Steps
```sh
# Zip the project contents
zip -r deployment.zip . -x '*.git*' '*.venv*'

# Upload to AWS Lambda
aws lambda update-function-code \
    --function-name NumbersClassificationAPI \
    --zip-file fileb://deployment.zip
```

#### Configure Lambda Function
- **Runtime**: Python 3.9+
- **Handler**: `lambda_function.lambda_handler`
- **Trigger**: Add API Gateway as a trigger

---

## API Endpoints

### Classify a Number
- **Endpoint**: `/api/classify-number`
- **Method**: `GET`
- **Query Parameter**: `number` (required)

#### Example Request
```sh
GET http://your-api-endpoint/api/classify-number?number=123
```

#### Example Response
```json
{
  "number": 123,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["odd"],
  "digit_sum": 6,
  "fun_fact": "123 is a fascinating number with unique mathematical properties."
}
```

---

## License
This project is licensed under the MIT License.

🚀 Happy Coding!

