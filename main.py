from elasticsearch_connector import ElasticsearchConnector

def main():
    # Create an instance of ElasticsearchConnector
    es_connector = ElasticsearchConnector()

    # Create an index
    es_connector.create_index()

    # Sample document to index
    sample_document = {
        "title": "Sample Document",
        "content": "This is a sample document for Elasticsearch indexing and searching."
    }

    # Index the sample document
    es_connector.index_document(sample_document)

    # Search for documents
    search_query = "Elasticsearch indexing"
    search_results = es_connector.search_documents(search_query)

    # Display search results
    print(f"Search Results for '{search_query}':")
    for result in search_results:
        print(f"Title: {result['_source']['title']}")
        print(f"Content: {result['_source']['content']}")
        print("-----------")

if __name__ == "__main__":
    main()
