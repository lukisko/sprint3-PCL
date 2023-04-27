from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def indexPage():
    return render_template('index.html')

@app.route("/ProductsList")
def productsListPage():
    return render_template('ProductsList.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)