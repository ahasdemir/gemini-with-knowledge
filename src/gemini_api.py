import os
import argparse
import google.generativeai as genai
from dotenv import load_dotenv
from knowledge_manager import KnowledgeManager

def setup_gemini():
    """Gemini API'sini yapılandırır."""
    load_dotenv()  # .env dosyasından API anahtarını yükle
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        print("Hata: GEMINI_API_KEY bulunamadı.")
        print("Lütfen bir .env dosyası oluşturup içine GEMINI_API_KEY=your_key_here ekleyin.")
        exit(1)
    
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-2.0-flash')  

def ask_gemini(model, prompt, knowledge_manager):
    """Gemini'ye sorgu gönderir ve yanıtı alır, bilgi tabanını kullanır."""
    try:
        knowledge = knowledge_manager.retrieve_knowledge(prompt)
        enriched_prompt = f"{knowledge}\n\n{prompt}" if knowledge else prompt
        response = model.generate_content(enriched_prompt)
        return response.text
    except Exception as e:
        return f"Hata oluştu: {str(e)}"

def main():
    parser = argparse.ArgumentParser(description="Gemini API ile sorgu yapın")
    parser.add_argument("prompt", nargs="*", help="Gemini'ye sorulacak soru")
    parser.add_argument("-i", "--interactive", action="store_true", help="Etkileşimli mod")
    parser.add_argument("-m", "--model", choices=["flash", "pro"], default="flash", 
                        help="Kullanılacak model: 'flash' (gemini-2.0-flash) veya 'pro' (gemini-1.5-pro)")
    args = parser.parse_args()
    
    model = setup_gemini()
    knowledge_manager = KnowledgeManager()

    if args.interactive:
        print("Gemini 2.0 Flash API Etkileşimli Mod (çıkmak için 'q' yazın)")
        while True:
            user_input = input("\n> ")
            if user_input.lower() in ["q", "quit", "exit"]:
                break
            if user_input.strip():
                print("\nGemini yanıtlıyor...")
                response = ask_gemini(model, user_input, knowledge_manager)
                print(f"\n{response}")
    elif args.prompt:
        prompt = " ".join(args.prompt)
        print(f"\nSorgu: {prompt}")
        print("\nGemini yanıtlıyor...")
        response = ask_gemini(model, prompt, knowledge_manager)
        print(f"\n{response}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()