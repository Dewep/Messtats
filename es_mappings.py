messages = {
    "mappings": {
        "message": {
            "properties": {
                "id": {
                    "type": "string",
                    "index": "not_analyzed"
                },
                "from": {
                    "properties": {
                        "name": {
                            "type": "string",
                            "index": "not_analyzed"
                        },
                        "id": {
                            "type": "long"
                        }
                    }
                },
                "message": {
                    "type": "multi_field",
                    "fields": {
                        "raw": {
                            "type": "string",
                            "index": "not_analyzed"
                        },
                        "analyzed": {
                            "type": "string",
                            "index": "analyzed"
                        },
                        "analyzed_fr": {
                            "type": "string",
                            "index": "analyzed",
                            "analyzer": "french"
                        },
                        "analyzed_en": {
                            "type": "string",
                            "index": "analyzed",
                            "analyzer": "english"
                        }
                    }
                },
                "created_time": {
                    "type": "date"
                }
            }
        }
    }
}
