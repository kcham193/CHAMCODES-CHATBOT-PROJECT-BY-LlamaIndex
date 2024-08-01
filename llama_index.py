import llama_index

from llama_index import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader('knowledgebase').load.data()
index=VectorsStoreIndex.form_documents(documents)


def respond(text: str) -> str:
    query_engine = index.as_query_engine()
    return query_engine.query(text)

if __name__ == '__main__':
    while True:
        user_input = input('Human; ')
        print(f'Bot: {respond(user_input)}')