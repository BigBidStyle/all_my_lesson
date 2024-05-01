import requests
import json
my_reg = requests.get('https://swapi.dev/api/people/3/')
# print(my_reg.text)

data = json.loads(my_reg.text)  # <-- Десериализация JSON
print(data)