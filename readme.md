# Cloudflare-scrape wrapper

This is a simple little webserver to wrap around the [cfscrape](https://pypi.org/project/cfscrape/#description) python library.

Simply set the environment variables `web_domain` and `port` and then run run.py, and then you can point whatever other application at `http://localhost:{port}` for whichever port you chose.
