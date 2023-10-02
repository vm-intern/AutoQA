from django.apps import AppConfig
#from demo1.initialization import initialize_app
import sys
sys.path.append('QA_version_1')
from QA_version_1.agent import *

bot = botv1(max_length=80000, chunk_size=100, chunk_overlap=0, 
                 seperator="。", chain_type="stuff", embedding="m3e_base", model_name="baichuan2_13b")

class Demo1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'demo1'
    
