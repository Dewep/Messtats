import requests
import config
import os
import io
import json

def item_to_key(item):
    id_parts = item['id'].split('_')
    parts = []
    parts.append(id_parts[0])
    parts.append(item['created_time'][0:4])
    parts.append(item['created_time'][5:7])
    parts.append(item['created_time'][8:10])
    parts.append(item['created_time'][11:13])
    parts.append(id_parts[1])
    return '/'.join(parts)

def process_data(data):
    for item in data:
        filename = "data/" + item_to_key(item) + ".json"
        dirname = os.path.dirname(filename)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        with io.open(filename, "w", encoding="utf8") as json_file:
            json_file.write(json.dumps(item))

def get_graph_page(url):
    r = requests.get(url)
    dataResponse = r.json()
    try:
        data = dataResponse['data']
        nextUrl = dataResponse['paging']['next']
        if len(data) == 0:
            raise Exception("Length=0")
    except:
        print('CRAWLING ERROR:')
        print(json.dumps(dataResponse))
        return None
    process_data(data)
    return nextUrl

def get_graph_all_comments():
    url = config.GRAPH_URL + "/" + config.THREAD_ID + "/comments?access_token=" + config.GRAPH_ACCESS_TOKEN
    while url:
        print(url)
        url = get_graph_page(url)

get_graph_all_comments()
