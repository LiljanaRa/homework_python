import requests


def get_response(url):
     resp = requests.get(url)
     return resp


url = 'https://example.com'
response = get_response(url)


print("Status Code:", response.status_code)
print("Response Text:", response.text)
print("Response Headers:", response.headers)
