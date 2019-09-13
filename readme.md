# Cloudflare-scrape wrapper

This is a simple little webserver to wrap around the [cloudflare-scrape](https://github.com/Anorov/cloudflare-scrape) python library.

Simply set `web_domain` and `port` in `config.json` and then run run.py, and then you can point whatever other application at `http://localhost:{port}` for whichever port you chose.
