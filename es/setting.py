from elasticsearch import Elasticsearch

# es server setting
elasticsearch = Elasticsearch([{'host': 'localhost', 'port': 9200}])