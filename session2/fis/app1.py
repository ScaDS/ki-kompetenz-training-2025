import gradio as gr
import pandas as pd
import yaml
import numpy as np
from typing import List

def load_data():
    with open('../data.yml', 'r') as file:
        data = yaml.safe_load(file)
    return pd.DataFrame(data)

from llama_index.embeddings.huggingface import HuggingFaceEmbedding
e = HuggingFaceEmbedding(model_name="intfloat/multilingual-e5-large-instruct")

def embed(text: str) -> List[float]:
    return e.get_text_embedding(text)


def cosine_similarity(v1: List[float], v2: List[float]) -> float:
    v1 = np.array(v1)
    v2 = np.array(v2)
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

def find_similar_topics(query: str, df: pd.DataFrame, top_k: int = 3) -> str:
    # Get query embedding
    query_embedding = embed(query)
    
    # Calculate similarities
    similarities = []
    for idx, row in df.iterrows():
        similarity = cosine_similarity(query_embedding, row['embedding'])
        similarities.append((idx, similarity))
    
    # Sort by similarity (descending)
    similarities.sort(key=lambda x: x[1], reverse=True)
    
    # Get top k results
    top_indices = [idx for idx, _ in similarities[:top_k]]
    results = df.iloc[top_indices]
    
    # Format results
    output = "Top 3 most similar topics:\n\n"
    for idx, row in results.iterrows():
        output += f"Topic: {row.get('topic', 'N/A')}\n"
        output += f"Similarity Score: {similarities[top_indices.index(idx)][1]:.4f}\n"
        output += "-" * 50 + "\n"
    
    return output

# Load the data
df = load_data()

# Create the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# Ein simuliertes Forschungsinformationssystem")
    gr.Markdown("Geben Sie einen Themenbereich ein, um ähnliche Themen aus der Datenbank zu finden.")
    
    with gr.Row():
        query_input = gr.Textbox(label="Themenbereich")
        search_button = gr.Button("Suche")
    
    results_output = gr.Textbox(label="Results", lines=10)
    
    def search(query):
        if not query.strip():
            return "Please enter a topic to search."
        return find_similar_topics(query, df)
    
    search_button.click(
        fn=search,
        inputs=query_input,
        outputs=results_output
    )

if __name__ == "__main__":
    demo.launch() #server_name="127.0.0.1", server_port=7861, share=False)
