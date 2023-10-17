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
    result = qa({"query": query}, k=10)
    txt = ""
    txt += result["result"] + "\n"
    source = result["source_documents"]
    for item in source:
        txt += "原文：" + item.page_content
        # txt += "出处：" + item.metadata["source"]
    return txt


def dbqa(llm, db, query, k=4, threshold=0):
    query_results = db.similarity_search_with_score(query, k=k)
    reference = []
    question = "根据以下文档：\n"
    reference_id = []
    for i in range(len(query_results)):
        item = query_results[i]
        if item[1] >= threshold:
            reference.append(item[0].page_content)
            question += item[0].page_content + "\n"
            reference_id.append(item[0].metadata["id"])

    question += f"回答问题:{query}"
    result = llm.predict(question)
    for i in range(len(reference)):
        result += f"\n原文:{reference[i]} id:{reference_id[i]} "
    return result



