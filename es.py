import requests
import es_mappings
import config

def delete_index(index_name):
    r = requests.delete(config.ELASTICSEARCH_URL + "/" + index_name)
    print(r.json())

def create_index(index_name):
    r = requests.put(config.ELASTICSEARCH_URL + "/" + index_name, json=getattr(es_mappings, index_name))
    print(r.json())

def index(index_name, type_name, data):
    r = requests.post(config.ELASTICSEARCH_URL + "/" + index_name + "/" + type_name + "/" + data['id'], json=data)
    print(r.json())
