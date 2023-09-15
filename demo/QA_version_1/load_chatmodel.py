from langchain.llms import ChatGLM
import sys
import torch
from typing import Any
from transformers import AutoModelForCausalLM, pipeline, AutoTokenizer
from langchain.llms import HuggingFacePipeline

def get_model(model_name: str) -> Any:
    if model_name == "chatglm":
        return load_chatglm_model()
    elif model_name == "baichuan2":
        return load_baichuan2_model()
    else:
        pass

def load_chatglm_model(endpoint_url="http://127.0.0.1:8000", max_length=80000, top_p=0.9):
    # direct access endpoint in a proxied environment
    # os.environ['NO_PROXY'] = '127.0.0.1'

    llm = ChatGLM(
        endpoint_url=endpoint_url,
        max_token=max_length,
        history=[],
        top_p=top_p,
        model_kwargs={"sample_model_args": False},
    )
    return llm

def load_baichuan2_model(model_path="/home/vcp/taoran/baichuan2-7B-base/", max_length=128, temperature=0.8, repetition_penalty=1.1):
    tokenizer = AutoTokenizer.from_pretrained(model_path, use_fast=False,
                                              trust_remote_code=True)
    base_model = AutoModelForCausalLM.from_pretrained(model_path, device_map="auto",
                                                      trust_remote_code=True, torch_dtype=torch.bfloat16)
    pipe = pipeline(
        "text-generation",
        model=base_model,
        tokenizer=tokenizer,
        max_new_tokens=max_length,
        temperature=temperature,
        repetition_penalty=repetition_penalty,
    )
    llm = HuggingFacePipeline(pipeline=pipe)
    return llm
