import os
import json
from src.knowledge_manager import KnowledgeManager

def ingest_knowledge(document_path):
    """Ingests a new knowledge document into the system."""
    if not os.path.exists(document_path):
        print(f"Hata: {document_path} bulunamadı.")
        return

    with open(document_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Initialize the knowledge manager
    knowledge_manager = KnowledgeManager()

    # Process and update the knowledge base
    knowledge_manager.add_document(content)

    # Optionally, save the updated knowledge base to a file
    knowledge_manager.save_to_file()

    print(f"{document_path} başarıyla yüklendi.")

if __name__ == "__main__":
    # Example usage
    document_path = "knowledge/documents/sample.txt"  # Change this to the path of the document you want to ingest
    ingest_knowledge(document_path)