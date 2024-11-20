from flask import Flask, request, jsonify
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Parse the incoming JSON request body
        data = request.get_json()

        # Ensure all necessary fields are provided
        num1 = data.get('num1')
        num2 = data.get('num2')
        operator = data.get('operator')

        if num1 is None or num2 is None or operator is None:
            return jsonify({'error': 'Missing required fields'}), 400

        # Ensure the numbers are valid
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            return jsonify({'error': 'num1 and num2 must be integers or floats'}), 400

        # Perform the calculation based on the operator
        if operator == 'add':
            result = num1 + num2
        elif operator == 'subtract':
            result = num1 - num2
        elif operator == 'multiply':
            result = num1 * num2
        elif operator == 'divide':
            if num2 == 0:
                return jsonify({'error': 'Cannot divide by zero'}), 400
            result = num1 / num2
        else:
            return jsonify({'error': 'Invalid operator'}), 400

        # Return the result as a JSON response
        return jsonify({'result': result})

    except Exception as e:
        logging.error(f"Error processing the request: {e}")
        return jsonify({'error': 'An unexpected error occurred'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
