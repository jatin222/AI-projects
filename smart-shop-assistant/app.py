import gradio as gr
from agent import agent

def chat(message, history):          # Gradio fills these two
    return agent(message)

gr.ChatInterface(fn=chat, title="🛍️ Smart Shop Assistant").launch(share=True)  # ②