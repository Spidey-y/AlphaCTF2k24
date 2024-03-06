from flask import Flask, request
from urllib.request import urlopen
import re


app = Flask(__name__)

blacklist = ["127.0.0.1",
             "0.0.0.0", "::1", "0:0:0:0:0:0:0:1", "127", "[::]:80"]


@app.route('/', methods=['GET'])
def api():
    url_to_fetch = request.args.get('url')
    if not url_to_fetch:
        return "No url provided\nsee"
    if not re.match(re.compile(r'^(https?):\/\/(?:(?:\d{1,3}\.){3}\d{1,3})(?::\d{1,5})?(?:/?|[/?]\S+)$',
                               re.IGNORECASE), url_to_fetch):
        return "Boom Bam Bop Badabop boomp"
    for blacklisted in blacklist:
        if blacklisted in url_to_fetch:
            return f"{blacklisted} is blacklisted"
    try:
        with urlopen(url_to_fetch, timeout=3.0) as response:
            return response.read()
    except:
        return "404 Not Found"


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
