import gradio as gr
import pandas as pd
import yaml
import numpy as np
from typing import List
import os
from openai import OpenAI

def load_data():
    with open('../scientists_dataset_curated_embedded.yml', 'r') as file:
        data = yaml.safe_load(file)
    return pd.DataFrame(data)

def find_relevant_topics(query: str, df: pd.DataFrame, top_k: int = 3) -> str:
    # Create a context string containing all topics
    context = "Here are all available research topics:\n"
    for _, row in df.iterrows():
        context += f"Thema: {row.get('topic', 'N/A')}\n"
        context += f"Name: {row.get('name', 'N/A')}\n"
        context += f"Fakultät: {row.get('research_field', 'N/A')}\n"
        context += "-" * 50 + "\n"
    
    # Create the prompt for GPT-4
    prompt = f"""Based on the following query: '{query}', find the {top_k} most relevant research topics from the list below. 
Return the entries in the same format as they are in the list below.
    
{context}
    
Do not add any additional text or explanation or formatting.
Just return the entries in EXACTLY the same format as they are given in the list above.  
"""
    
    # Initialize OpenAI client
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    
    # Get response from GPT-4
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that finds relevant research topics based on user queries."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )
    
    output = response.choices[0].message.content
    
    return output

# Load the data
df = load_data()

# Create the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# Ein simuliertes Forschungsinformationssystem 3")
    gr.Markdown("Geben Sie einen Themenbereich ein, um ähnliche Themen aus der Datenbank zu finden.")
    
    with gr.Row():
        query_input = gr.Textbox(label="Themenbereich")
        search_button = gr.Button("Suche")
    
    results_output = gr.Textbox(label="Suchergebnisse", lines=10)
    
    def search(query):
        if not query.strip():
            return "Bitte geben Sie ein Thema ein."
        return find_relevant_topics(query, df)
    
    search_button.click(
        fn=search,
        inputs=query_input,
        outputs=results_output
    )

if __name__ == "__main__":
    #demo.launch(server_name="172.17.2.211", root_path="/training/fis3", server_port=50002) 
    demo.launch() 