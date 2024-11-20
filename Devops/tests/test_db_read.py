import pymongo

def test_mongo_connection():
    try:
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        client.admin.command("ping")
        assert True
    except Exception as e:
        assert False, f"MongoDB connection failed: {e}"
