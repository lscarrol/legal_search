from pydantic import BaseModel
import pprint as pp
from mixpeek.client import Mixpeek
from pymongo import MongoClient
from nomic import embed


load_dotenv()

nomic_key = os.getenv('NOMIC_API_KEY')
openai_key = os.getenv('OPENAI_KEY')
mongo_uri = os.getenv('MONGO_URI')
os.environ["NOMIC_API_KEY"] = nomic_key

def embed_mix(text):
    output = embed.text(
    texts=[text],
    model='nomic-embed-text-v1',
    task_type='search_document'
    )
    print(output)
    return output['embeddings'][0]



        
uri = mongo_uri
# Create a new client and connect to the server
client = MongoClient(uri)

print(client.list_database_names())
db = client["legal_cases_base"]  # Replace with your database name
collection = db["legal_cases_base"]  # Replace with your collection name

# # Specify the field to check
# field_to_check = "embedding"  # Replace with the actual field name

# # Count the number of documents with the specified field
# count = collection.count_documents({field_to_check: {"$exists": True}})

# print(f"Number of documents with the field '{field_to_check}': {count}")


# Iterate over the documents in the collection
for document in collection.find():
    # Check if the "embedding" field exists in the document
    if "embedding" not in document:
        text = document["text"]  # Replace "text" with the field containing the text you want to embed
        embedding = embed_mix(text)
        print("UPDATING WITH EMBEDDING:")
        print(document["_id"])
        print("---------------------------------")
        # Update the document with the embedding
        collection.update_one(
            {"_id": document["_id"]},
            {"$set": {"embedding": embedding}}
        )
    else:
        print("Skipping document (embedding already exists):")
        print(document["_id"])
        print("---------------------------------")

client.close()

