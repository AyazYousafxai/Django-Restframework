import requests

end_point = "http://localhost:8000/api/Products/1/"

# get_response = requests.post(end_point,json={'title':"hello xylexa"})
get_response = requests.get(end_point)


# print(get_response.json())
print(get_response.text)