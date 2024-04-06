from pydantic import BaseModel
import pprint as pp
from mixpeek.client import Mixpeek
from pymongo import MongoClient
from nomic import embed
#mixpeek = Mixpeek(api_key="sk-mfW_dyra260ecDvS8ay415Ubxo5Lwp2rQ7qoXd_1JxC1hObJL8SM0B2j4gJ5CMRB85Y")


def embed_mix(text):
    output = embed.text(
    texts=[text],
    model='nomic-embed-text-v1',
    task_type='search_document'
    )
    print(output)
    return output['embeddings'][0]

embed_mix("This is a test")




