import requests

answer = {'answer': open("answer.json", "rb")}
r = requests.post(
    'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=b1c78eeadf977279a257799be2ca7842c5360cef', files=answer)

print(r.text)
