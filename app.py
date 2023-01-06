from flask import Flask, jsonify
from products import products


app = Flask(__name__)

@app.route("/ping")
def ping():
	return jsonify({
		"message": "comenzando mi primera API"
	})

@app.route("/products")
def getProducts():
	return jsonify({
		"message": "Products List",
		"products": products
	})

@app.route("/products/<string:product_name>")
def getProduct(product_name):
	productFound = [
		product for product in products 
			if product["name"] == product_name
		]

	if(len(productFound) > 0):	
		return jsonify({
			"product": productFound[0]
		})
	return jsonify({
		"message": "Product not found!!, try again"

	})


if __name__ == "__main__":
	app.run(debug=True, port=4000)