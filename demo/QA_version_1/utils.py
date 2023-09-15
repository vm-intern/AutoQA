from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain import VectorDBQA
from langchain.document_loaders import DirectoryLoader
from langchain.schema import Document


def load_chroma(chroma_path, embedding):
    return Chroma.from_documents(persist_directory=chroma_path, embedding_function=embedding)


def string2chroma(string, embedding, metadata={"source": "unknown"}, chunk_size=200, chunk_overlap=0, separator="。", db_path="default"):
    # d = Document(page_content=string, metadata=metadata)
    text_splitter = CharacterTextSplitter(separator=separator, chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    texts = text_splitter.split_text(string)
    if db_path == "default":
        database = Chroma.from_texts(texts, embedding, metadatas=[metadata for item in texts])
    else:
        database = Chroma.from_texts(texts, embedding,  metadatas=[metadata for item in texts])
    return database


def txt2chroma(txt_path, embedding, chunk_size=200, chunk_overlap=0, separator="。", db_path="default"):
    loader = DirectoryLoader(path=txt_path, glob="*.txt")
    documents = loader.load_and_split()

    text_splitter = CharacterTextSplitter(separator=separator, chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    texts = text_splitter.split_text(documents)

    if db_path == "default":
        database = Chroma.from_documents(texts, embedding)
    else:
        database = Chroma.from_documents(texts, embedding)
    return database


def get_QA(chat_model, database, chain_type="stuff"):
    qa = VectorDBQA.from_chain_type(llm=chat_model, chain_type=chain_type, vectorstore=database,
                                    return_source_documents=True)
    return qa


def query2QA(qa, query):
    result = qa({"query": query})
    txt = ""
    txt += result["result"] + "\n"
    source = result["source_documents"]
    for item in source:
        txt += "原文：" + item.page_content
        # txt += "出处：" + item.metadata["source"]
    return txt