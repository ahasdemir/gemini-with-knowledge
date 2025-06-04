import os
import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class KnowledgeManager:
    """Manages the knowledge base for the Gemini API."""
    
    def __init__(self):
        self.knowledge_base = []
        self.vectorizer = TfidfVectorizer()
        self.embeddings = None
        self.knowledge_dir = os.path.join(os.path.dirname(__file__), '../knowledge/documents')
        self.embedding_file = os.path.join(os.path.dirname(__file__), '../knowledge/embeddings/embeddings.txt')
    
    def load_knowledge(self, directory=None):
        """Load knowledge documents from the specified directory."""
        if directory is None:
            directory = self.knowledge_dir
        
        self.knowledge_base = load_knowledge_documents(directory)
        return self.knowledge_base
    
    def update_knowledge(self, document_path):
        """Update knowledge base with new document."""
        with open(document_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        self.knowledge_base.append(content)
        return True
    
    def retrieve_knowledge(self, query):
        """Retrieve relevant knowledge for the given query."""
        if not self.knowledge_base:
            self.load_knowledge()
        
        if not self.knowledge_base:
            return None
        
        # Create embeddings if not already done
        if self.embeddings is None:
            self.create_embeddings()
        
        # Vectorize the query
        query_vector = self.vectorizer.transform([query])
        
        # Calculate similarity scores
        similarities = cosine_similarity(query_vector, self.embeddings)
        
        # Get the most relevant document
        most_relevant_idx = np.argmax(similarities)
        
        return self.knowledge_base[most_relevant_idx]
    
    def create_embeddings(self):
        """Create embeddings for the knowledge base."""
        if not self.knowledge_base:
            return None
        
        self.embeddings = self.vectorizer.fit_transform(self.knowledge_base)
        return self.embeddings
    
    def check_integrity(self):
        """Check if the knowledge base is properly loaded."""
        return len(self.knowledge_base) > 0
    
    def add_document(self, content):
        """Add a new document to the knowledge base."""
        self.knowledge_base.append(content)
        self.embeddings = None  # Reset embeddings so they'll be recalculated
        return True
    
    def save_to_file(self):
        """Save the current state of the knowledge base."""
        # Implementation depends on how you want to persist the data
        pass
    
    def get_references(self, query):
        """Get references from the knowledge base for a query."""
        if not self.knowledge_base:
            self.load_knowledge()
            
        if not self.knowledge_base:
            return "No knowledge documents available."
            
        if self.embeddings is None:
            self.create_embeddings()
            
        query_vector = self.vectorizer.transform([query])
        similarities = cosine_similarity(query_vector, self.embeddings)
        
        # Find the top 3 most relevant documents
        top_indices = np.argsort(similarities[0])[-3:][::-1]
        
        references = []
        for idx in top_indices:
            # Take the first 100 characters as a reference snippet
            snippet = self.knowledge_base[idx][:100].replace('\n', ' ') + '...'
            references.append(snippet)
            
        return "\n\n".join(references)


# Keep the existing utility functions
def load_knowledge_documents(directory):
    """Load knowledge documents from the specified directory."""
    knowledge_documents = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                knowledge_documents.append(file.read())
    return knowledge_documents

def update_knowledge_documents(directory, new_document):
    """Update the knowledge base with a new document."""
    with open(os.path.join(directory, f"{new_document['title']}.txt"), 'w', encoding='utf-8') as file:
        file.write(new_document['content'])

def retrieve_knowledge_document(directory, title):
    """Retrieve a specific knowledge document by title."""
    try:
        with open(os.path.join(directory, f"{title}.txt"), 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return f"Document '{title}' not found."

def handle_embeddings(embedding_data, embedding_file):
    """Process and save embeddings for knowledge documents."""
    with open(embedding_file, 'w', encoding='utf-8') as file:
        for data in embedding_data:
            file.write(f"{data}\n")  # Save each embedding on a new line

def load_embeddings(embedding_file):
    """Load embeddings from the specified file."""
    embeddings = []
    try:
        with open(embedding_file, 'r', encoding='utf-8') as file:
            embeddings = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []
    return embeddings