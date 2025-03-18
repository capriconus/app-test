import os
import yaml

base_path = os.path.dirname(os.path.abspath(__file__))

def readyaml(yamlname):
     yaml_path = os.path.join(base_path,yamlname)
     try:
          with open(yaml_path,'r',encoding='utf-8') as f:
               cases = yaml.safe_load(f)
     except Exception as e:
          raise e
     return cases['LoginCase']