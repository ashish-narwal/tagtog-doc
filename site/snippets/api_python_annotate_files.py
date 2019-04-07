import requests

tagtogAPIUrl = "https://www.tagtog.net/-api/documents/v1"

auth = requests.auth.HTTPBasicAuth(username='yourUsername', password='yourPassword')
params = {'project':'yourProject', 'owner': 'yourUsername', 'output':'ann.json'}
# you can append more files to the list in case you want to upload multiple files
files = [('file', open('files/text.txt', 'rb'))]
response = requests.post(tagtogAPIUrl, params=params, auth=auth, files=files)
print(response.text)
