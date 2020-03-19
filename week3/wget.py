import sys
import requests

print(requests.__file__)

# Have a look at /usr/lib/python3/dist-packages/requests/exceptions.py

url = sys.argv[1]

try:
    response = requests.get(url, timeout = 30)
    response.raise_for_status()
except requests.Timeout:
    print("Request timeout, url: {}".format(url))
except requests.HTTPError as err:
    code = err.response.status_code
    print("URL error url {}, code {}".format(url, code))
except requests.RequestException:
    print("URL downloading error, url: {}".format(url))
else:
    print(response.content)
