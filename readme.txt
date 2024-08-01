FAQ Chatbot

The FAQ Chatbot is designed to provide quick and relevant answers to user queries by searching through a predefined list of FAQs. It uses the sentence_transformers library for generating semantic embeddings of text and Faiss for efficient similarity searching.
Features

    Semantic search through FAQs to find the most relevant answers.
    Simple Flask-based web interface for user interaction.
    Uses vector embeddings and Faiss for efficient and accurate FAQ retrieval.

Prerequisites

Ensure you have the following installed on your machine:

    Python 3.8 or higher
    pip (Python package installer)

Installation

Follow these steps to set up the project locally:

1. Go to 'faq-chatbot' directory: cd faq-chatbot

2. Install the required Python packages: pip install -r requirements.txt

Set up the environment: Ensure you have the correct environment variables set if necessary (e.g., for API keys or database credentials).


Running the Application

    Start the Flask server: python app.py

This will start the local server, typically accessible via http://localhost:5000.

Access the chatbot:Open a web browser and go to http://localhost:5000 to interact with the FAQ chatbot.


Usage

Enter your question in the provided text field on the webpage and click the "Search" button. The chatbot will process your query and display the most relevant FAQ answers based on the content similarity.


Project Structure

    app.py: Main Flask application file.
    faq_manager.py: Handles loading of FAQs and indexing using Faiss.
    templates/: Contains HTML files for the web interface.
    requirements.txt: Lists all the necessary Python libraries.


