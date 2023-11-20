from elasticsearch import Elasticsearch

class ElasticsearchConnector:
    def __init__(self, index_name='my_index'):
        self.es = Elasticsearch()
        self.index_name = index_name

    def create_index(self):
        body = {
            "mappings": {
                "properties": {
                    "title": {"type": "text"},
                    "content": {"type": "text"}
                }
            }
        }
        self.es.indices.create(index=self.index_name, body=body)

    def index_document(self, document):
        self.es.index(index=self.index_name, body=document)

    def search_documents(self, query):
        body = {
            "query": {
                "match": {
                    "content": query
                }
            }
        }
        result = self.es.search(index=self.index_name, body=body)
        return result['hits']['hits']
