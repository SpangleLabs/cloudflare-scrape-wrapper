PROJECT = cloudflare_scrape_wrapper
DOCKERHUB_TAG = "joshcoales/cloudflare_bypass"
VERSION = "0.1.0"

build:
	docker build -t $(PROJECT) .

run: build
	docker run -e web_domain="$(WEB_DOMAIN)" -p 4999:80 $(PROJECT)

start:
	docker run -e web_domain="$(WEB_DOMAIN)" -p 4999:80 -d $(PROJECT)

stop:
	docker stop $(PROJECT)

publish: clean build
	docker tag $(PROJECT) $(DOCKERHUB_TAG):$(VERSION)
	docker push $(DOCKERHUB_TAG):$(VERSION)
	docker tag $(PROJECT) $(DOCKERHUB_TAG):latest
	docker push $(DOCKERHUB_TAG):latest

clean:
	docker kill -s 9 $(PROJECT) || true
	docker rm $(PROJECT) || true
	docker rmi -f $(PROJECT) || true
	rm -rf venv
