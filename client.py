import requests

end_point = "http://localhost:8080/api/"

get_response = requests.get(end_point)

# print(get_response.json())
print(get_response.text)