import os

class Config:
    """Configuration settings for the application."""
    
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.knowledge_base_path = os.path.join(os.path.dirname(__file__), '../knowledge/documents')
        self.embeddings_path = os.path.join(os.path.dirname(__file__), '../knowledge/embeddings')
        self.index_path = os.path.join(os.path.dirname(__file__), '../knowledge/index')

    def validate(self):
        """Validate the configuration settings."""
        if not self.api_key:
            raise ValueError("API key is not set. Please set the GEMINI_API_KEY environment variable.")
        if not os.path.exists(self.knowledge_base_path):
            raise ValueError(f"Knowledge base path does not exist: {self.knowledge_base_path}")
        if not os.path.exists(self.embeddings_path):
            raise ValueError(f"Embeddings path does not exist: {self.embeddings_path}")
        if not os.path.exists(self.index_path):
            raise ValueError(f"Index path does not exist: {self.index_path}")