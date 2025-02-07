# Numbers API

A simple Flask-based API that classifies numbers and provides fun facts about them.

## Project Structure
```
├── .dist/             # Directory for distribution files
├── app.py             # Main application file containing the Flask API
├── README.md          # Project documentation
└── requirements.txt   # Dependencies required to run the application
```

## Setup and Installation

### **1. Clone the repository**
```sh
git clone https://github.com/yourusername/numbers_api.git
cd numbers_api
```

### **2. Create and activate a virtual environment**
#### On Windows:
```sh
python -m venv venv
venv\Scripts\activate
```
#### On macOS and Linux:
```sh
python3 -m venv venv
source venv/bin/activate
```

### **3. Install dependencies**
```sh
pip install -r requirements.txt
```

## Running the Application

Start the Flask application:
```sh
flask run
```

By default, Flask runs on `http://127.0.0.1:5000/`. You can access the API using a web browser or an API client like Postman.

## API Endpoints

### **1. Classify a number**
- **Endpoint:** `/api/classify-number`
- **Method:** `GET`
- **Description:** Classifies a number and provides fun facts about it.
- **Query Parameter:**
  - `number` (required) → The number to classify.

#### Example Request:
```
GET http://127.0.0.1:5000/api/classify-number?number=123
```

#### Example Response:
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

## License
This project is licensed under the **MIT License**.

---

### 🚀 Happy Coding!

