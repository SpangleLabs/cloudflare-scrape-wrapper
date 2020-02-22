PROJECT = cloudflare_scrape_wrapper

build:
	docker build -t $(PROJECT) .

run: build
	docker run -e web_domain="$(WEB_DOMAIN)" -p 4999:4999 $(PROJECT)

start:
	docker run -e web_domain="$(WEB_DOMAIN)" -p 4999:4999 -d $(PROJECT)

stop:
	docker stop $(PROJECT)

clean:
	docker kill -s 9 $(DOCKER_TAG) || true
	docker rm $(DOCKER_TAG) || true
	docker rmi -f $(DOCKER_TAG) || true
	rm -rf venv
