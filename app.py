from flask import Flask, jsonify, request
from products import products


app = Flask(__name__)


#first route test
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

@app.route("/products", methods=["POST"])
def addProduct():
	new_product = {
		"name": request.json["name"],
		"price": request.json["price"],
		"quantity": request.json["quantity"]
	}

	products.append(new_product)
	return (request.json)

@app.route("/products/<string:product_name>", methods=["PUT"])
def editProduct(product_name):
	productFound = [product for product in products if product["name"] == product_name]	

	if (len(productFound) > 0):
		productFound[0]["name"] = request.json["name"]
		productFound[0]["price"] = request.json["price"]
		productFound[0]["quantity"] = request.json["quantity"]
		return jsonify({
			"message": "Producto Updated",
			"product": productFound[0]
		})
	return jsonify({
		"message": "Product not Found"
	})

@app.route("/products/<string:product_name>", methods=["DELETE"])
def deleteProduct(product_name):
	productFound = [product for product in products if product["name"] == product_name]	

	if (len(productFound) > 0):
		products.remove(productFound[0])
		return jsonify({
			"message": "Product Deleted!",
			"products": products
		})
	return jsonify({
		"message": "Product not Found"
	})


if __name__ == "__main__":
	app.run(debug=True, port=4000)
