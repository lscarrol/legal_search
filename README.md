# LegalSearch

LegalSearch is a chatbot project that aims to provide an efficient and user-friendly way to search through a large dataset of court cases and answer legal questions. By leveraging cutting-edge technologies such as Nomic embeddings, Atlas vector search, and natural language processing, LegalSearch enables users to find relevant court cases, citations, and legal information based on their queries and engage in a conversational interaction.

## Dataset and Embeddings

The project utilizes a dataset of 26,000 court cases. To enable efficient searching, we created embeddings for all the court cases using Nomic embeddings v1. These embeddings capture the semantic meaning of the text and allow for accurate similarity comparisons.

## Atlas Vector Search Index

We created an Atlas vector search index using the generated embeddings. The index uses cosine similarity as the distance metric, enabling fast and accurate retrieval of similar court cases based on the user's query.

## Chatbot Interface

LegalSearch provides a chatbot interface built using the MongoDB framework. Users can interact with the chatbot by entering their legal questions and engaging in a conversational exchange. The chatbot leverages Retrieval Augmented Generation (RAG) to provide semantic and contextual answers based on the legal datasets and embeddings. It also provides relevant citations and legal data to support its responses.

## Backend Processing

When a user interacts with the chatbot, the backend performs the following steps:

1. Vector Search: The user's query is sent to the Atlas vector search index using the Langchain library. This step retrieves the most similar court cases based on the query's embedding.

2. Summarization: The retrieved court cases are summarized using the Sumy library's LSA (Latent Semantic Analysis) summarization technique. This step extracts the most important information from each court case, providing concise summaries for the user.

3. Relevance Assessment: The summarized court cases are then processed using the GPT-3.5-turbo-instruct language model. The model is prompted to assess the relevance of each summary to the user's query and provide a relevance statement.

4. Retrieval Augmented Generation (RAG): The chatbot uses the RAG approach to generate responses based on the retrieved and summarized court cases. By combining the semantic and contextual information from the legal datasets with the language generation capabilities of the model, the chatbot provides informative and relevant answers to the user's legal questions, along with citations and relevant legal data.

## Example Usage

![alt text](https://github.com/lscarrol/legal\_search/blob/main/pic1.png)

![alt text](https://github.com/lscarrol/legal\_search/blob/main/pic2.png)
