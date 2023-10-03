# AutoQA
AI chat-bot for question answering based on langchain.
This project has been tested on python3.10.

# Installation
`
pip install -r requirements.txt
`
or use the mirrow to download
`
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
`

# Quick start
1. Specialize the method to load the chat model and the embedding model in demo/QA_version_1/load_chatmodel.py and demo/QA_version_1/load_embeddingmodel.py
2. Specialize the model you want to use in demo/demo1/apps.py
3. Input the command bellow
`
python manage.py runserver 127.0.0.1:8000
`

# Problem
1. warnings about VectorDBQA can be ignore.
