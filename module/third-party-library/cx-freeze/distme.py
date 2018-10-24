import urllib.request
import urllib.parse

url = 'https://pythonprogramming.net'
paramethers = {
    'q': 'basic',
    'submit': 'search'
}

data = urllib.parse.urlencode(paramethers)
dataEncode = data.encode('utf-8')

request = urllib.request.Request(url, dataEncode)

response = urllib.request.urlopen(request)

responseData = response.read()


print(responseData)
print(len(responseData))

# <http.client.HTTPResponse object at 0x7f8b9d4cc6d0>

# 20181016
