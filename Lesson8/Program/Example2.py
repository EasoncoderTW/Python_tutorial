import requests

response = requests.get('https://api.github.com')
print(response.json())  # Output: JSON response from the GitHub API