## PDF-QA with GooglePalm LLM
## Project Overview:
This project harnesses the power of the GooglePalm Large Language Model (LLM) to extract information from uploaded PDF files and deliver precise answers to user queries. Employing Langchain and FAISS libraries enhances the system's capabilities, ensuring a robust question-answering mechanism. The process involves generating instruct embeddings to capture contextual information, with these embeddings stored in a FAISS vector database. When users pose questions, the system efficiently searches the vector database, providing accurate answers by identifying similar matching vectors.

## Key Features:
<strong>GooglePalm LLM Integration: </strong>Utilizes the advanced language modeling capabilities of GooglePalm to understand and process PDF data effectively.

<strong>Langchain and FAISS Integration:</strong> Incorporates Langchain and FAISS libraries to enhance the overall performance and efficiency of the system.

<strong>Instruct Embeddings:</strong> Implements instruct embeddings to capture contextual information, facilitating a nuanced understanding of the text.

<strong>Vector Database:</strong> Stores instruct embeddings in a FAISS vector database, optimizing the retrieval process for user queries.


## Installation:

Ensure required dependencies are installed using the provided requirements.txt.
Set up GooglePalm LLM, Langchain, and FAISS libraries according to their respective documentation.
Configuration:

Adjust configuration files to specify PDF data sources, model parameters, and other settings.
Run the System:

## Dependencies:
GooglePalm LLM
Langchain Library
FAISS Library
Other dependencies specified in requirements.txt
Contribution Guidelines:
We welcome contributions and bug reports. Please follow the established guidelines in the CONTRIBUTING.md file.
