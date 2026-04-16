import streamlit as st
from openai import OpenAI
import numpy as np

# Initialize OpenAI client
client = OpenAI(api_key="YOUR_API_KEY")

# Dummy in-memory "vector store" (replace with Endee later)
vector_store = []

# Function to create embeddings
def get_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

# Function to add data to vector store
def add_to_store(text):
    embedding = get_embedding(text)
    vector_store.append((text, embedding))

# Function to find most similar text
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def search(query):
    query_embedding = get_embedding(query)
    best_score = -1
    best_text = ""

    for text, emb in vector_store:
        score = cosine_similarity(query_embedding, emb)
        if score > best_score:
            best_score = score
            best_text = text

    return best_text

# Function to generate answer
def generate_answer(question, context):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Answer based only on the given context."},
            {"role": "user", "content": f"Context: {context}\n\nQuestion: {question}"}
        ]
    )
    return response.choices[0].message.content

# Streamlit UI
st.title("📚 AI Question Answering System (RAG)")

st.write("Upload text data and ask questions!")

# Input data
data = st.text_area("Enter your data (knowledge base):")

if st.button("Store Data"):
    add_to_store(data)
    st.success("Data stored successfully!")

# Ask question
question = st.text_input("Ask a question:")

if st.button("Get Answer"):
    if len(vector_store) == 0:
        st.warning("Please add data first!")
    else:
        context = search(question)
        answer = generate_answer(question, context)
        st.write("### Answer:")
        st.write(answer)
