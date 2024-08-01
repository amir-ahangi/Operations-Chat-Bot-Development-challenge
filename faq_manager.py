import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class FAQManager:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)
        self.index = None
        self.faq_data = []

    def load_faqs(self, directory):
        for root, dirs, files in os.walk(directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                with open(filepath, 'r') as file:
                    question = file.readline().strip()
                    answer = file.read().strip()
                    self.faq_data.append((question, answer))
    
    def build_index(self):
        # Encode all questions
        questions = [faq[0] for faq in self.faq_data]
        question_embeddings = self.model.encode(questions)
        
        # Create and train the index
        dimension = question_embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(question_embeddings.astype('float32'))

    def search(self, query, k=1):
        query_vector = self.model.encode([query])[0]
        _, indices = self.index.search(np.array([query_vector], dtype='float32'), k)
        return [self.faq_data[i] for i in indices[0]]
