from setuptools import setup, find_packages

setup(
    name="gemini-with-knowledge",
    version="0.1.0",
    author="Ahmet Hasdemir",
    author_email="ahmet@hasdemir.me",
    description="A project that integrates knowledge management with the Gemini API.",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "google-generativeai",
        "python-dotenv",
        "numpy",  # Add any other dependencies as needed
    ],
    entry_points={
        "console_scripts": [
            "ingest_knowledge=scripts.ingest_knowledge:main",
            "query_with_knowledge=scripts.query_with_knowledge:main",
        ],
    },
)