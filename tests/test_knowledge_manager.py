import pytest
from src.knowledge_manager import KnowledgeManager

@pytest.fixture
def knowledge_manager():
    return KnowledgeManager()

def test_load_knowledge(knowledge_manager):
    knowledge_manager.load_knowledge('knowledge/documents/sample.txt')
    assert len(knowledge_manager.knowledge_base) > 0

def test_retrieve_knowledge(knowledge_manager):
    knowledge_manager.load_knowledge('knowledge/documents/sample.txt')
    response = knowledge_manager.retrieve_knowledge('sample query')
    assert response is not None

def test_update_knowledge(knowledge_manager):
    knowledge_manager.load_knowledge('knowledge/documents/sample.txt')
    initial_count = len(knowledge_manager.knowledge_base)
    knowledge_manager.update_knowledge('knowledge/documents/new_sample.txt')
    assert len(knowledge_manager.knowledge_base) > initial_count

def test_embeddings_creation(knowledge_manager):
    knowledge_manager.load_knowledge('knowledge/documents/sample.txt')
    embeddings = knowledge_manager.create_embeddings()
    assert embeddings is not None
    assert len(embeddings) > 0

def test_knowledge_integrity(knowledge_manager):
    knowledge_manager.load_knowledge('knowledge/documents/sample.txt')
    assert knowledge_manager.check_integrity() is True