import os

import cfscrape
from flask import Flask, request

app = Flask(__name__)
scraper = cfscrape.create_scraper()

if not os.getenv('web_domain'):
    print("Please set a web_domain environment variable")
    quit()

web_domain = os.getenv("web_domain")


def get_full_cookies():
    cookies = request.cookies
    core_cookies = cfscrape.get_cookie_string(web_domain)
    core_cookie_dict = {x.split("=")[0]: x.split("=")[1] for x in core_cookies[0].split(";")}
    return {**core_cookie_dict, **cookies}


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all_get(path):
    full_path = "{}/{}".format(web_domain, path)
    cookies = get_full_cookies()
    resp = scraper.get(full_path, cookies=cookies)
    return resp.content, resp.status_code


@app.route('/', defaults={'path': ''}, methods=['POST'])
@app.route('/<path:path>', methods=['POST'])
def catch_all(path):
    full_path = "{}/{}".format(web_domain, path)
    cookies = get_full_cookies()
    if request.json:
        data = request.values
        resp = scraper.post(full_path, json=data, cookies=cookies)
        return resp.content, resp.status_code
    data = request.data
    resp = scraper.post(full_path, data=data, cookies=cookies)
    return resp.content, resp.status_code


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.getenv("port", 4999)))
