all: build

build:
	docker build -t semantic_search .

run:
	docker run -p 5000:5000 --name semantic_search -it semantic_search

stop:
	docker stop semantic_search

clean:
	docker rm semantic_search

logs:
	docker logs semantic_search
