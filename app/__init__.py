from flask import Flask, render_template, request, redirect, session

import app.persistance as pers
import app.persistance.products as products
import app.model as model

app = Flask(__name__)

class Product:
    def __init__(self, name, category, size, price):
        self.name = name
        self.category = category
        self.size = size
        self.price = price
    
    def __getitem__(self, key):
        return getattr(self, key)

@app.route("/")
def indexPage():
    return render_template('index.html')


product_categories = ["Coffee","Tea","Soda"]

@app.route("/Menu")
def menuPage():
    grouped_products = {}
    for product in sorted(products, key=lambda p: p['size']):
        if product['category'] not in grouped_products:
            grouped_products[product['category']] = []
        grouped_products[product['category']].append(product)
    return render_template("Menu.html",products=grouped_products,product_categories=product_categories)

@app.route("/ProductsList")
def productsListPage():
    return render_template('ProductsList.html', products=products.getAllDrinks())

@app.route("/EditProduct/<string:product_name>")
def product_detail(product_name):
    product = None
    for obj in products:
        if obj.name == product_name:
            product = obj
            break
    return render_template('EditProduct.html', product=product)

#update product endpoint
@app.route('/update/<string:product_name>', methods=['GET', 'POST'])
def update_product(product_name):
    for product in products:
        if product.name == product_name:
            if request.method == 'POST':
                product.name = request.form['name']
                product.category = request.form['category']
                product.size = request.form['size']
                product.price = int(request.form['price'])
                return redirect('/ProductsList')
            else:
                return render_template('EditProduct.html', product=product)
    return 'Product not found'

#delete product endpoint
@app.route("/product/<id>", methods=["DELETE","GET"])
def removeProduct(id):
    if (request.method == "DELETE"):
        products.removeDrink(id)
    return redirect('/ProductsList')


# create product endpoint

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        size = request.form['size']
        price = int(request.form['price'])
        newProduct = model.Product(0,name,category,size,price)
        savedProduct = products.createDrink(newProduct)
        if (savedProduct.id == 0):
            return "can not create the product, please try again later"
        else:
            return redirect('/ProductList') # after creating of drink forward user to the list of all drinks

@app.route("/product/<id>", methods=["DELETE","GET"])
def removeProduct(id):
    if (request.method == "DELETE"):
        products.removeDrink(id)
        return redirect('/ProductsList')
    if (request.method == "GET"): # this is product detail
        product = products.getDrink(id)
        return render_template('EditProduct.html', product=product)

order = []
#add to cart method
@app.route('/cart', methods=['POST'])
def add_to_cart():
    # get product information from form submission
    # product_name = request.form.get('product_name', '')
    # product_size = request.form.get('product_size', '')
    product_id = request.form.get(product_id,'')
    product_quantity = int(request.form.get('product_quantity', '0'))


    # find product in list of products
    product = products.getDrink(product_id)

    # add product to order
    if product:
        order.append({'name': product['name'], 'size': product['size'], 'price': product['price'], 'quantity': product_quantity})

    return redirect("/checkout")

@app.route('/cart', methods=['GET'])
def checkout():
    total_price = sum([item['price']*item['quantity'] for item in order])
    return render_template('Checkout.html', order=order, total_price=total_price)

#@app.route('/update/product/<id>', method=['POST'])
#def update_product(id):
#    return "Would you like some tea?", 418

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
