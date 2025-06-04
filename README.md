# Gemini with Knowledge

This project integrates a knowledge management system with the Gemini API, allowing the model to reference a knowledge base when generating responses. 

## Project Structure

```
gemini-with-knowledge
├── src
│   ├── gemini_api.py         # Main application logic for interacting with the Gemini API
│   ├── knowledge_manager.py   # Manages the knowledge base and embeddings
│   ├── config.py             # Configuration settings for the application
│   └── utils.py              # Utility functions for file handling and data processing
├── knowledge
│   ├── documents
│   │   └── sample.txt        # Sample knowledge document for the model
│   ├── embeddings
│   │   └── .gitkeep          # Keeps the embeddings directory in version control
│   └── index
│       └── .gitkeep          # Keeps the index directory in version control
├── scripts
│   ├── ingest_knowledge.py    # Script for ingesting new knowledge documents
│   └── query_with_knowledge.py # Script for querying the model with knowledge references
├── tests
│   ├── test_gemini_api.py    # Unit tests for gemini_api.py
│   ├── test_knowledge_manager.py # Unit tests for knowledge_manager.py
│   └── test_utils.py         # Unit tests for utility functions
├── .env.example               # Example environment variables file
├── .gitignore                 # Specifies files to ignore in version control
├── requirements.txt           # Lists project dependencies
├── setup.py                   # Packaging information for the application
└── README.md                  # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd gemini-with-knowledge
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Copy `.env.example` to `.env` and fill in the required variables.

5. **Run the application:**
   - Use the scripts in the `scripts` directory to ingest knowledge or query the model.

## Usage Examples

- To ingest knowledge:
  ```bash
  python scripts/ingest_knowledge.py
  ```

- To query the model with knowledge references:
  ```bash
  python scripts/query_with_knowledge.py "Your query here"
  ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes. 

## License

This project is licensed under the MIT License. See the LICENSE file for details.