from flask import Flask, jsonify, render_template
from flask_pymongo import PyMongo
import os

app = Flask(__name__)

# Load environment variables
app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://localhost:27017/testdb")

# Initialize MongoDB
mongo = PyMongo(app)

# Default route
@app.route("/", methods=["GET"])
def index():
    return render_template("home/index.html")

# Home route
@app.route("/home", methods=["GET"])
def home():
    return render_template("home/index.html")

# Products route
@app.route("/products", methods=["GET"])
def products():
    products = mongo.db.products.find()
    product_list = [{"name": product["name"], "price": product["price"]} for product in products]
    return render_template("products.html", products=product_list)


if __name__ == "__main__":
    app.run(debug=True)
