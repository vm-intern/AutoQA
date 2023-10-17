from typing import Any
import sys
sys.path.append("QA_version_1")
from load_chatmodel import *
from utils import *
from load_embeddingmodel import get_embedding


class botv1(object):
    def __init__(self, max_length: int=80000, chunk_size: int=100, chunk_overlap: int=0, 
                 seperator: str="。", chain_type: str="stuff", embedding: str="bge_zh", 
                 model_name: str="chatglm"):
        self.max_length = max_length
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.separator = seperator
        self.chain_type = chain_type
        self.embedding = get_embedding(embedding)
        self.model = get_model(model_name)
        self.text_splitter = CharacterTextSplitter(separator=self.separator,
                                                   chunk_size=self.chunk_size, 
                                                   chunk_overlap=self.chunk_overlap)

    # get or create new DB
    def updatedb_from_string(self, string: str, ID="default") -> Any:
        metadata = {"id": ID}
        if not hasattr(self, "database"):
            self.database = string2chroma(string=string, 
                                          embedding=self.embedding, 
                                          chunk_size=self.chunk_size,
                                          chunk_overlap=self.chunk_overlap, 
                                          separator=self.separator,
                                          metadata=metadata)
        else:
            texts = self.text_splitter.split_text(string)
            self.database.add_texts(texts, metadatas=[metadata for item in texts])

        self.qa = get_QA(chat_model=self.model, 
                            database=self.database, 
                            chain_type=self.chain_type)
    def delete(self):
        pass

    # chat with file
    def file_based_qa(self, query: str) -> Any:
        # return query2QA(self.qa, query)
        return dbqa(self.model, self.database, query)
    
    # chat with model
    def chat(self, text: str):
        return self.model.predict(text)
    
    def react(self, query: str):
        if "根据文档" in query:
            return self.file_based_qa(query)
        else:
            return self.chat(query)

    def delete_by_id(self, ID: str):
        self.database.delete(self.database.get(where={"source": ID})["ids"])
    
