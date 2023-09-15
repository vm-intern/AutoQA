# from load_chatmodel import load_chatglm_model, load_baichuan2_model
# from utils import *
# from load_embeddingmodel import get_embedding, get_bge_zh_embedding
# from langchain.vectorstores import Chroma
#
#
# max_length = 80000
# chunk_size = 200
# chunk_overlap = 0
# separator = "。"
# txt_path = "./精神现象学/"
# chain_type = "stuff"
#
#
# if __name__ == "__main__":
#     embedding = get_bge_zh_embedding()
#     model = load_chatglm_model(max_length=max_length)
#     database = txt2chroma(txt_path=txt_path, embedding=embedding, chunk_size=chunk_size,
#                           chunk_overlap=chunk_overlap, separator=separator)
#     qa = get_QA(chat_model=model, database=database, chain_type=chain_type)
#     query2QA(qa, "运动是什么，它包括什么？")


# import 这个类就行了 询问问题用bot.react(str)如果问题里面有 根据文档 四个字，就会调用数据库，否则就会调用对话回答
# 初始化向量数据库用get_vector_from_string 添加用updatedb_from_string，注意都传字符串
# 使用之前请先激活lc环境，并进入"/home/vcp/taoran/chatglm2-6B/"运行python api.py 会占用127.0.0.1 8000端口
from agent import botv1


if __name__ == "__main__":
    bot = botv1()
    print(bot.react("你是谁？"))
    bot.get_vector_from_string("但事实上人们所以嫌恶中介，纯然是由于不了解中介和绝对知识本身的性质。因为中介不是别的，只是运动着的自身同一，换句话说，它是自身反映，自为存在着的自我的环节，纯粹的否定性，或就其纯粹的抽象而言，它是单纯的形成过程。这个中介、自我、一般的形成，由于具有简单性，就恰恰既是正在形成中的直接性又是直接的东西自身。——因此，如果中介或反映不被理解为绝对的积极环节而被排除于绝对真理之外，那就是对理性的一种误解。正是这个反映，使真理成为发展出来的结果，而同时却又将结果与其形成过程之间的对立予以扬弃；因为这个形成过程同样也是单一的，因而它与真理的形式（真理在结果中表现为单一的）没有区别，它勿宁就是这个返回于单一性的返回过程。诚然，胎儿自在地是人，但并非自为地是人；只有作为有教养的理性，它才是自为的人，而有教养的理性使自己成为自己自在地是的那个东西。这才是理性的现实。但这结果自身却是单纯的直接性，因为它是自觉的自由，它静止于自身，并且它不是把对立置于一边听其自生自灭，而是已与对立取得了和解。")
    print(bot.react("根据文档回答：为什么人们讨厌中介？"))
    bot.updatedb_from_string("你说得对，但是这就是奎桑提，HP4700，护甲329，魔抗201的英雄。有不可阻挡，有护盾，还能过墙。有控制，甚至冷却时间只有1秒，只要15点蓝。转换姿态时甚至可以刷新W的cd，还有真实伤害。然后，护甲和魔抗提升后还能获得技能加速，缩短Q的cd，还缩短释放时间，然后还有攻击力。W就啊啊啊啊啊啊!!!")
    print(bot.react("根据文档回答：奎桑提是什么"))