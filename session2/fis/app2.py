import gradio as gr
import pandas as pd
import yaml
import numpy as np
from typing import List
import random

def load_data():
    with open('../scientists_dataset_curated_embedded.yml', 'r') as file:
        data = yaml.safe_load(file)
    return pd.DataFrame(data)

def find_random_topics(query: str, df: pd.DataFrame, top_k: int = 3) -> str:
    # Select random topics
    random_indices = random.sample(range(len(df)), top_k)
    results = df.iloc[random_indices]
    
    # Format results
    output = ""
    for idx, row in results.iterrows():
        output += f"Thema: {row.get('topic', 'N/A')}\n"
        output += f"Name: {row.get('name', 'N/A')}\n"
        output += f"Fakultät: {row.get('research_field', 'N/A')}\n"
        output += "-" * 50 + "\n"
    
    return output

# Load the data
df = load_data()

# Create the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# Ein simuliertes Forschungsinformationssystem 2")
    gr.Markdown("Geben Sie einen Themenbereich ein, um ähnliche Themen aus der Datenbank zu finden.")
    
    with gr.Row():
        query_input = gr.Textbox(label="Themenbereich")
        search_button = gr.Button("Suche")
    
    results_output = gr.Textbox(label="Suchergebnisse", lines=10)
    
    def search(query):
        if not query.strip():
            return "Bitte geben Sie ein Thema ein."
        return find_random_topics(query, df)
    
    search_button.click(
        fn=search,
        inputs=query_input,
        outputs=results_output
    )

if __name__ == "__main__":
    demo.launch() 