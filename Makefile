.PHONY: build run clean

IMAGE_NAME = avengers_app
NETWORK_NAME = avengers_network
ELASTICSEARCH_CONTAINER_NAME = avengers_elasticsearch

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker network create $(NETWORK_NAME)
	docker run -d --network $(NETWORK_NAME) --name $(ELASTICSEARCH_CONTAINER_NAME) -p 9200:9200 elasticsearch:7.10.1
	docker run --network $(NETWORK_NAME) $(IMAGE_NAME)

clean:
	docker stop $(ELASTICSEARCH_CONTAINER_NAME) || true
	docker rm $(ELASTICSEARCH_CONTAINER_NAME) || true
	docker network rm $(NETWORK_NAME) || true
