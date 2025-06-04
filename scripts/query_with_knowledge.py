import os
import argparse
from src.knowledge_manager import KnowledgeManager
from src.gemini_api import setup_gemini, ask_gemini

def main():
    parser = argparse.ArgumentParser(description="Sorgu yapın ve bilgi tabanını kullanın")
    parser.add_argument("query", help="Gemini'ye sorulacak sorgu")
    args = parser.parse_args()

    # Knowledge manager instance
    knowledge_manager = KnowledgeManager()

    # Load knowledge documents
    knowledge_manager.load_knowledge()

    # Prepare the query with knowledge references
    knowledge_references = knowledge_manager.get_references(args.query)
    enriched_query = f"{args.query}\n\nBilgi Referansları:\n{knowledge_references}"

    # Setup Gemini model
    model = setup_gemini()

    # Get response from Gemini
    response = ask_gemini(model, enriched_query)
    print(f"\nGemini yanıtlıyor...\n{response}")

if __name__ == "__main__":
    main()