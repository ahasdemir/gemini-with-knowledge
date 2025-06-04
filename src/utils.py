def read_file(file_path):
    """Reads the content of a file and returns it as a string."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_file(file_path, content):
    """Writes the given content to a file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def list_files_in_directory(directory_path):
    """Returns a list of files in the specified directory."""
    import os
    return [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

def load_knowledge_documents(knowledge_directory):
    """Loads all knowledge documents from the specified directory."""
    documents = {}
    for file_name in list_files_in_directory(knowledge_directory):
        file_path = os.path.join(knowledge_directory, file_name)
        documents[file_name] = read_file(file_path)
    return documents

def process_query_with_knowledge(query, knowledge_documents):
    """Processes a query using the provided knowledge documents."""
    # This is a placeholder for the actual processing logic
    response = "Processed query: " + query
    for doc_name, content in knowledge_documents.items():
        response += f"\nReferenced from {doc_name}: {content[:50]}..."  # Show a snippet of the content
    return response