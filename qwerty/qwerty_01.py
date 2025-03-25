import requests


"""this is how we can get information from the web page using URL"""
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(response.status_code)
print(response.json())


params = {"userId": 2}
response = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)
print(response.url)
print(response.json())







"""this is how we work with post requests"""
# data = {
#     "title": "New Post",
#     "body": "This is the content of the post.",
#     "userId": 1
# }
#
# response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)
#
# print(response.status_code)
# print(response.json())




"""this is how we work with put"""
# update_data = {
#     "title": "Updated Post",
#     "body": "Updated content.",
#     "userId": 1
# }
# response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=update_data)
#
# print(response.status_code)
# print(response.json())





