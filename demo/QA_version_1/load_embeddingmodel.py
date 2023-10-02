from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from typing import Any
from langchain.embeddings import OpenAIEmbeddings
# import torch
# DEVICE = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"


def get_embedding_from_ptah(embedding_path: str) -> Any:
    embeddings = SentenceTransformerEmbeddings(model_name=embedding_path)
    return embeddings

def get_bge_zh_embedding() -> Any:
    return get_embedding_from_ptah("/home/vcp/dingcheng/bge-large-zh/")


def get_openai_embedding() -> Any:
    pass


def get_m3e_base_embedding() -> Any:
    return OpenAIEmbeddings(openai_api_base="xxx", openai_api_key="xxx", model_name="m3e-base")


def get_embedding(embedding_name: str) -> Any:
    if embedding_name == "bge_zh":
        return get_bge_zh_embedding()
    elif embedding_name == "openai":
        return get_openai_embedding()
    elif embedding_name == "m3e_base":
        return get_m3e_base_embedding()
    else:
        pass


