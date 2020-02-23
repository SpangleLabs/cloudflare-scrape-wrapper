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
	docker kill -s 9 $(PROJECT) || true
	docker rm $(PROJECT) || true
	docker rmi -f $(PROJECT) || true
	rm -rf venv
