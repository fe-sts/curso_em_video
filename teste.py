import requests as r

url = 'https://api.covid19api.com/dayone/country/brazil'
resp = r.get(url)

print(resp.status_code)