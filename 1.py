
import requests
 
# Making a get request
response = requests.get('https://zoesquad.me')
 
# printing request content
print(response.content)
print(response.status_code)
print(response.headers)
print(response.headers['content-type'])
print(response.encoding)
print(response.text)
print(response.json())
print(response.url)
print(response.history)
print(response.cookies)
print(response.elapsed)
print(response.request)
print(response.connection)
print(response.raw)
print(response.reason)
print(response.history)

