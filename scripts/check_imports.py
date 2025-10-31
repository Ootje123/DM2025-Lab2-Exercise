modules = [
    ("import dotenv", "dotenv"),
    ("from google import genai", "google-generativeai or google-genai (check Google GenAI SDK)"),
    ("import langextract", "langextract (maybe local or pip name differs)") ,
    ("import gensim", "gensim"),
    ("import tensorflow", "tensorflow or tensorflow-cpu"),
    ("import tensorflow_hub", "tensorflow-hub"),
    ("import keras", "keras"),
    ("import ollama", "ollama (check if you intended Ollama SDK)"),
    ("import langchain", "langchain"),
    ("from langchain_community import utils", "langchain-community"),
    ("from langchain_core import prompts", "langchain-core or langchain_core"),
    ("from langchain_google_genai import chat_models", "langchain-google-genai (community integration)") ,
    ("from bs4 import BeautifulSoup", "beautifulsoup4"),
    ("import chromadb", "chromadb"),
    ("import gradio", "gradio"),
    ("import jupyter", "jupyter"),
    ("import sklearn", "scikit-learn"),
    ("import pandas", "pandas"),
    ("import numpy", "numpy"),
    ("import matplotlib", "matplotlib"),
    ("import plotly", "plotly"),
    ("import seaborn", "seaborn"),
    ("import nltk", "nltk"),
    ("import umap", "umap-learn (import as 'umap' or 'umap.umap_')"),
    ("import pymupdf", "PyMuPDF (import often as 'fitz')"),
]

print('Running import checks...')

for stmt, suggestion in modules:
    try:
        # use exec to run the import statement
        exec(stmt, globals())
        print(f"OK: {stmt}")
    except Exception as e:
        print(f"FAIL: {stmt} -> {e.__class__.__name__}: {e}")
        print(f"   Suggest pip install: {suggestion}\n")

print('\nDone.')
