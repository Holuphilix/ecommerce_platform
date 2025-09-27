# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)
orders = []

@app.route('/orders', methods=['GET'])
def list_orders():
    return jsonify(orders)

@app.route('/orders', methods=['POST'])
def create_order():
    order = request.json
    orders.append(order)
    return jsonify({"message": "Order created", "orders": orders}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
