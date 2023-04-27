from flask import Flask, render_template, request, redirect, session

import app.persistance as pers
import app.persistance.products as products
import app.model as model

app = Flask(__name__)

@app.route("/")
def indexPage():
    return render_template('index.html')

@app.route("/ProductsList")
def productsListPage():
    return render_template('ProductsList.html', products=products.getAllDrinks())

@app.route("/product", methods=["POST"])
def createProduct():
    if request.method == 'POST':
        title = request.args['Title']
        category = request.args['Category']
        size = request.args['size']
        price = request.args['Price']
        newProduct = model.Product(0,title,category,size,price)
        savedProduct = products.createDrink(newProduct)
        if (savedProduct.id == 0):
            return "can not create the product, please try again later"
        else:
            return redirect('/ProductList',code=302)
        

@app.route("/list")
def getListOfDrinks():
    return render_template('list.html', list=products.getAllDrinks())

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)