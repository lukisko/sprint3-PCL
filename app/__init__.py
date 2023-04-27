from flask import Flask, render_template

import app.persistance as pers
import app.persistance.products as products

app = Flask(__name__)

@app.route("/")
def indexPage():
    return render_template('index.html')

@app.route("/ProductsList")
def productsListPage():
    return render_template('ProductsList.html')

@app.route("/list")
def getListOfDrinks():
    return render_template('list.html', list=products.getAllDrinks())

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)