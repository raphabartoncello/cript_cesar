import requests

resp = requests.get(
    'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=b1c78eeadf977279a257799be2ca7842c5360cef')
with open ('answer.json','wb') as f:
    f.write(resp.content)
