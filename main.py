import requests
from datetime import datetime

USERNAME = "username"
TOKEN = "password"
GRAPH_ID = "graph-id"
pixela_endpoint = "endpoint"

# Post request for creating a user
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


# Post request for creating a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# Post request to create a pixel
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
graph_insert_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you run? "),
}
response = requests.post(url=pixel_creation_endpoint, json=graph_insert_config, headers=headers)
print(response.text)

# For both PUT and DELETE request we need to give for previous dates variable=datetime(year=,month=,day=)
# Put request to update a pixel
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
graph_update_config = {
    "quantity": "2.6"
}

# response = requests.put(url=pixel_update_endpoint, json=graph_update_config, headers=headers)
# print(response.text)

# Delete request to delete a pixel
# pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)
