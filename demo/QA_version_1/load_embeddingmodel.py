from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from typing import Any
# import torch
# DEVICE = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"


def get_embedding_from_ptah(embedding_path: str) -> Any:
    embeddings = SentenceTransformerEmbeddings(model_name=embedding_path)
    return embeddings

def get_bge_zh_embedding() -> Any:
    return get_embedding_from_ptah("/home/vcp/dingcheng/bge-large-zh/")


def get_openai_embedding() -> Any:
    pass

def get_embedding(embedding_name: str) -> Any:
    if embedding_name == "bge_zh":
        return get_bge_zh_embedding()
    elif embedding_name == "openai":
        get_openai_embedding()
    else:
        pass


