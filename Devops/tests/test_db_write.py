from app import app
from flask_pymongo import PyMongo

def test_mongo_write():
    mongo = PyMongo(app)
    with app.app_context():
        # Insert a test document
        test_doc = {"name": "Test Product", "price": 99.99}
        mongo.db.products.insert_one(test_doc)
        
        # Verify insertion
        result = mongo.db.products.find_one({"name": "Test Product"})
        assert result is not None
        assert result["name"] == "Test Product"
