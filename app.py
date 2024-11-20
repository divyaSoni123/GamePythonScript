from flask import Flask, request, jsonify
from flask_cors import CORS
import logging

# Initialize the Flask app
app = Flask(__name__)
CORS(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Retrieve JSON data from the request (force=True for Python 2 compatibility)
        data = request.get_json(force=True)
        
        if not data:
            logging.error("No data provided in request")
            return jsonify({'error': 'No input data provided'}), 400

        # Validate if all keys exist
        if not all(k in data for k in ('num1', 'num2', 'operator')):
            logging.error("Missing required data in request")
            return jsonify({'error': 'Missing required fields: num1, num2, operator'}), 400

        num1 = data['num1']
        num2 = data['num2']
        operator = data['operator']

        # Check if numbers are valid (should be integers or floats)
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            logging.error("Invalid data types for numbers")
            return jsonify({'error': 'num1 and num2 must be numbers'}), 400

        # Perform the calculation based on the operator
        if operator == 'add':
            result = num1 + num2
        elif operator == 'subtract':
            result = num1 - num2
        elif operator == 'multiply':
            result = num1 * num2
        elif operator == 'divide':
            if num2 == 0:
                logging.error("Division by zero attempted")
                return jsonify({'error': 'Cannot divide by zero'}), 400
            result = num1 / num2
        else:
            logging.error("Invalid operator used")
            return jsonify({'error': 'Invalid operator. Use add, subtract, multiply, or divide.'}), 400

        # Return the result as a JSON response
        return jsonify({'result': result})

    except Exception as e:
        logging.error("Unexpected error occurred: %s", str(e))
        return jsonify({'error': 'An unexpected error occurred'}), 500


if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000, debug=True)
