from flask import Flask,  render_template
import json
import os

app = Flask(__name__)


def read_json(path):
    with open(path,"r") as f:
        return json.load(f)

@app.route('/')
@app.route('/index')
def index():
    products=read_json("app\data\products.json")
    return render_template('main.html', products=products)
@app.route('/products')
def products():
    products=read_json("app\data\products.json")
    return render_template('index.html', products=products)


@app.route('/products/id=<int:product_id>', methods=['GET'])
def get_products_by_id(product_id):
    products=read_json("app\data\products.json")

    product = products[product_id - 1]

    return render_template('by_id.html',product = product)

# @app.route('/products?category_id=1', methods=['GET'])
# def get_products_by_category_id():
#     products=get_products("app\data\products.json")
#     productsByCat = []
#     for product in products:
#         if product["category_id"] == 1:
#             productsByCat.append(product)
#     return render_template('by_cat.html',products = productsByCat)

if __name__ == '__main__':
    app.run(debug=True)