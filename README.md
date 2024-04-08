# LegalSearch

LegalSearch is a project developed for the MongoDB 2024 Hackathon that aims to provide an efficient and user-friendly way to search through a large dataset of court cases. By leveraging cutting-edge technologies such as Nomic embeddings, Atlas vector search, and natural language processing, LegalSearch enables users to find relevant court cases based on their queries.

## Dataset and Embeddings

The project utilizes a dataset of 26,000 court cases. To enable efficient searching, we created embeddings for all the court cases using Nomic embeddings v1. These embeddings capture the semantic meaning of the text and allow for accurate similarity comparisons.

## Atlas Vector Search Index

We created an Atlas vector search index using the generated embeddings. The index uses cosine similarity as the distance metric, enabling fast and accurate retrieval of similar court cases based on the user's query.

## Frontend

LegalSearch provides a basic frontend interface that allows users to input their queries. The frontend is designed to be intuitive and user-friendly, making it easy for users to search for relevant court cases.

## Backend Processing

When a user submits a query, the backend performs the following steps:

1. **Vector Search**: The query is sent to the Atlas vector search index using the Langchain library. This step retrieves the most similar court cases based on the query's embedding.

2. **Summarization**: The retrieved court cases are summarized using the Sumy library's LSA (Latent Semantic Analysis) summarization technique. This step extracts the most important information from each court case, providing concise summaries for the user.

3. **Relevance Assessment**: The summarized court cases are then processed using the GPT-3.5-turbo-instruct language model. The model is prompted to assess the relevance of each summary to the user's query and provide a relevance statement.


## Example Usage

![alt text](https://github.com/lscarrol/legal_search/blob/main/pic1.png)
![alt text](https://github.com/lscarrol/legal_search/blob/main/pic2.png)
