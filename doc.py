import requests

url = "https://www.dropbox.com/scl/fi/vnbhfi2eu1ciuwjwzsnnn/QA.docx?rlkey=3dpojwnrpt4f34q9gx461yode&dl=1"
file_path = "docs/QA.docx"

response = requests.get(url)
response.raise_for_status()

with open(file_path, 'wb') as f:
    f.write(response.content)

print(f"Файл успешно скачан и сохранен как {file_path}")
