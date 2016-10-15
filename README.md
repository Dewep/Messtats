# Messtats (Messenger Stats)

Messenger Stats (insert messages from thread to an elasticsearch database)

## Installation

Install/run an elasticsearch instance:

```shell
$> docker run --name messtats_elasticsearch -p 9200:9200 -p 9300:9300 -d elasticsearch:2.4
```

```shell
$> pip install -r requirements.txt
```

Edit `config.py`.

## Get messages from thread

Run `fetch_thread.py` (and edit url variable if the access token has been expired or your ip temporary banned).

Run `index_messages.py` to index all the messages into the elasticsearch database.

## Statistics

Query the elasticsearch to have statistics about the messages. Some examples are present into the directory `es_searches`:

```shell
$> curl -X POST http://localhost:9200/messages/message/_search -H "Content-Type: application/json" -d @es_searches/texts_per_month.json
```
