from main import generate_next_generations
from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


@app.route("/api/next_generations", methods=["POST"])
def next_generations():
    # Get order from query parameter (default: asc)
    order = request.args.get('order', 'asc').lower()
    
    if order not in ['asc', 'desc']:
        return jsonify({"error": "Invalid order. Use 'asc' or 'desc'"}), 400
    
    if not request.json:
        return jsonify({"error": "Request must be JSON"}), 400
    
    initial_board = request.json.get('initial_board')
    if initial_board is None:
        return jsonify({"error": "Missing 'initial_board' in request body"}), 400
    
    generations_number = request.json.get('generations_number')
    if type(generations_number) is not int or generations_number < 1:
        return jsonify({"error": "'generations_number' must be a positive integer"}), 400
    elif generations_number is None:
        return jsonify({"error": "Missing 'generations_number' in request body"}), 400
    
    result_generations = generate_next_generations(initial_board, generations_number)
    
    if order == 'desc':
        result_generations = result_generations[::-1]

    return jsonify({
        "initial_board": initial_board,
        "generations_number": generations_number,
        "order": order,
        "result": result_generations
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)