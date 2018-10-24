from urllib import request, parse
from re import findall

url = 'http://pythonprogramming.net'
values = {
    's': 'basics',
    'submit': 'search',
}

data = parse.urlencode(values)
data = data.encode('utf-8')
req = request.Request(url, data)
resp = request.urlopen(req)
respData = resp.read()


print(respData)

regexParagraph = r'<p>(.*?)</p>'
paragraphs = findall(regexParagraph, str(respData))

print('#######################')
print(str(len(paragraphs)) + ':')
print(paragraphs)
