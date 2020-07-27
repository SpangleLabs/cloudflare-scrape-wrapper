PROJECT = cloudflare_scrape_wrapper
DOCKERHUB_TAG = "joshcoales/cloudflare_bypass"
VERSION = "0.1.0"


WEB_DOMAIN:
ifndef WEB_DOMAIN
	@echo Warning: WEB_DOMAIN isn\'t defined\; continue? [Y/n]
	@read line; if [ $$line = "n" ]; then echo aborting; exit 1 ; fi
endif

build:
	docker build -t $(PROJECT) .

run: build WEB_DOMAIN
	docker run -e web_domain="$(WEB_DOMAIN)" -p 4999:80 $(PROJECT)

start: WEB_DOMAIN
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
