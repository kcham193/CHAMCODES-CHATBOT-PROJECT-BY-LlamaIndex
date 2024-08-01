Chambulilo Chatbot with LlamaIndex
Chambulilo is an AI-powered chatbot that utilizes the OpenAI API and LlamaIndex for enhanced interaction and knowledge-based responses. It can interact with users and provide answers based on a predefined set of documents.

Developed By
Kasim
Features
Conversational AI: Interact naturally with the chatbot using OpenAI's language model.
Knowledge Base Integration: Query specific information from a set of documents using LlamaIndex.
Prerequisites
Python 3.7 or higher
OpenAI Python client library
llama_index library
Installation
Clone the repository

sh
Copy code
git clone https://github.com/your-repo/chambulilo-chatbot-llamaindex.git
cd chambulilo-chatbot-llamaindex
Install dependencies

Use the package manager pip to install the required dependencies.

sh
Copy code
pip install openai llama_index
Set up OpenAI API Key

Replace the placeholder in the script with your actual OpenAI API key. For security reasons, do not hardcode your API key in the code for production environments. Use environment variables or other secure methods to manage your keys.

python
Copy code
openai.api_key = "your_openai_api_key_here"
Usage
Setting Up the Knowledge Base
Prepare Your Documents

Place your documents in a directory named knowledgebase. The SimpleDirectoryReader will load these documents for indexing.

Indexing the Documents

The VectorStoreIndex class from LlamaIndex is used to create an index from the documents. The index allows for efficient querying.

Running the Chatbot
To start the chatbot, execute the script:

sh
Copy code
python main.py
Once running, the chatbot can answer questions based on both its training and the documents in the knowledge base.

Example Interaction
vbnet
Copy code
Human: What's the capital of France?
Bot: The capital of France is Paris.
Customization
System Command
You can customize the initial behavior and responses of the chatbot by modifying the system_command variable in the script.

python
Copy code
system_command = '''
act as a chatbot
your name is chambulilo and you are developed by kasim!
'''
Knowledge Base
To update the knowledge base, simply add or modify documents in the knowledgebase directory and re-run the script.

Contributing
If you have suggestions, improvements, or bug reports, please open a pull request or submit an issue on the GitHub repository.

License
This project is licensed under the MIT License. See the LICENSE file for details.
