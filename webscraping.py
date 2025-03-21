import requests
from bs4 import BeautifulSoup
from bs4 import Comment
import re
url = "http://127.0.0.1:8000/victima.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

comments = soup.find_all(string=lambda text: isinstance(text, Comment))
print("Comentarios: ")

#Rafael Alejandro Díaz Rangel

for c in comments:
	print(c)
	print("=============")
	c.extract()

email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')

emails = soup.find_all(string=email_pattern)

print("Correos: ")

for email in emails:
	print(email)
	print("----------------")
