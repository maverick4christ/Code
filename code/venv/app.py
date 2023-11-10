from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/products')
def get_products():
    # Replace this with your logic to fetch product data from a database or another source
    products = [
        {'id': 1, 'name': 'Product 1', 'price': 29.99},
        {'id': 2, 'name': 'Product 2', 'price': 39.99},
        # Add more products as needed
    ]
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)
