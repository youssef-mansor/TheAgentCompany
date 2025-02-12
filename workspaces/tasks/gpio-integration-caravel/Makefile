IMAGE_NAME=shifter-8bit-general
CONTAINER_NAME=shifter-8bit-general

.PHONY: build run stop

build:
	docker buildx build -t $(IMAGE_NAME) . --no-cache --load

run:
	docker run --network host --name $(CONTAINER_NAME) -it $(IMAGE_NAME) /bin/bash

stop:
	docker stop $(CONTAINER_NAME)
	docker rm $(CONTAINER_NAME)

attach:
	docker exec -it $(CONTAINER_NAME) /bin/bash
