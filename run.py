import os

import cfscrape
from flask import Flask, request, Response

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
    full_cookies = dict()
    for key, val in core_cookie_dict.items():
        full_cookies[key] = val
    for key, val in cookies.items():
        full_cookies[key] = val
    return full_cookies


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all_get(path):
    full_path = "{}/{}".format(web_domain, path)
    cookies = get_full_cookies()
    resp = scraper.get(full_path, cookies=cookies)
    return Response(
        resp.content,
        status=resp.status_code,
        mimetype=resp.headers["Content-Type"]
    )


@app.route('/', defaults={'path': ''}, methods=['POST'])
@app.route('/<path:path>', methods=['POST'])
def catch_all(path):
    full_path = "{}/{}".format(web_domain, path)
    cookies = get_full_cookies()
    headers = {
        "Content-Type": request.headers["Content-Type"],
        "Origin": request.headers["Origin"],
        "Referer": request.headers["Referer"],
        "Accept": request.headers["Accept"],
        "User-Agent": request.headers["User-Agent"]
    }
    if request.json:
        data = request.json
        resp = scraper.post(full_path, json=data, headers=headers, cookies=cookies)
    else:
        if request.form:
            data = "&".join(f"{x}={y}" for x, y in request.form.to_dict().items())
        else:
            data = request.data
        resp = scraper.post(full_path, data=data, headers=headers, cookies=cookies)
    return Response(
        resp.content,
        status=resp.status_code,
        mimetype=resp.headers["Content-Type"]
    )


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.getenv("port", 4999)))
