import es
import json
import glob
import time

es.delete_index("messages")
es.create_index("messages")

nb = 0
for filename in glob.iglob('data/**/*.json', recursive=True):
    nb += 1
    if nb % 500 == 0:
        time.sleep(1)
    with open(filename, encoding="utf8") as f:
        item = json.load(f)
        es.index("messages", "message", item)
