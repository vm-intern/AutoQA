from django.apps import AppConfig
#from demo1.initialization import initialize_app
import sys
sys.path.append('/home/vcp/demo/QA_version_1')
from QA_version_1.agent import *

bot = botv1(max_length=80000, chunk_size=100, chunk_overlap=0, 
                 seperator="。", chain_type="stuff", embedding="bge_zh", model_name="chatglm")

class Demo1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'demo1'
    
