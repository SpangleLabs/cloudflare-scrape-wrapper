import json
import cfscrape
from flask import Flask, request

app = Flask(__name__)
scraper = cfscrape.create_scraper()

with open("config.json", "r") as f:
    config = json.load(f)

if not config['web_domain']:
    print("Please set a web_domain in config.json")
    quit()


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all_get(path):
    full_path = "{}/{}".format(config['web_domain'], path)
    cookies = request.cookies
    resp = scraper.get(full_path, cookies=cookies)
    return resp.content, resp.status_code


@app.route('/', defaults={'path': ''}, methods=['POST'])
@app.route('/<path:path>', methods=['POST'])
def catch_all(path):
    full_path = "{}/{}".format(config['web_domain'], path)
    cookies = request.cookies
    if request.json:
        data = request.values
        resp = scraper.post(full_path, json=data, cookies=cookies)
        return resp.content, resp.status_code
    data = request.data
    resp = scraper.post(full_path, data=data, cookies=cookies)
    return resp.content, resp.status_code


if __name__ == '__main__':
    app.run(port=config['port'])
