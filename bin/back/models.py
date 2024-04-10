from pydantic import BaseModel
import pprint as pp
from mixpeek.client import Mixpeek
from pymongo import MongoClient
from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_openai import OpenAIEmbeddings
from nomic import embed
import os
from langchain_nomic.embeddings import NomicEmbeddings
import openai
from dotenv import load_dotenv
from sumy.summarizers.lex_rank import LexRankSummarizer  
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk

nltk.download('punkt')
load_dotenv()

nomic_key = os.getenv('NOMIC_API_KEY')
openai_key = os.getenv('OPENAI_KEY')
mongo_uri = os.getenv('MONGO_URI')
os.environ["NOMIC_API_KEY"] = nomic_key
DB_NAME = "legal_cases_base"
COLLECTION_NAME = "legal_cases_base"
ATLAS_VECTOR_SEARCH_INDEX_NAME = "index_doc"

def generate_summary(page_content, num_sentences=3):
    parser = PlaintextParser.from_string(page_content, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = " ".join([str(sentence) for sentence in summarizer(parser.document, num_sentences)])
    return summary             


def relevance(request, question):
    openai.api_key = openai_key
    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt="Tell me the relevance to the query: " + question,
        max_tokens=1000
    )

    gpt3_response = response.choices[0].text.strip()
    return gpt3_response

def search(query):
    uri = mongo_uri
    # Create a new client and connect to the server
    client = MongoClient(uri)

    MONGODB_COLLECTION = client[DB_NAME][COLLECTION_NAME]

    # insert the documents in MongoDB Atlas with their embedding
    vector_search = MongoDBAtlasVectorSearch(MONGODB_COLLECTION, NomicEmbeddings(model="nomic-embed-text-v1", dimensionality=768),index_name=ATLAS_VECTOR_SEARCH_INDEX_NAME)

    results = vector_search.similarity_search(query)
    client.close()
    return results


def build_output(results, query):
    output = []
    if results:
        for result in results:
            suma = generate_summary(result.page_content)
            rel = relevance(suma, query)
            output.append({
                'summary': suma,
                'relevance': rel,
                'absolute_url': result.metadata['absolute_url'],
                'author': result.metadata['author_name'],
                'case_name': result.metadata['case_name'],
                'date_filed': result.metadata['date_filed'].strftime('%Y-%m-%d')
            })
    return output
    

query = "What is the legal definition of assault?"

ret = search(query)

build_output(ret, query)