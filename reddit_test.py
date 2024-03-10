import requests

url = "https://api.pushshift.io/reddit/search/comment/?q=science"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    comments = data['data']
    for comment in comments:
        print(comment['body'])  # Print or process the comment as needed
else:
    print(f"Failed to download comments from subreddit ")
    print(response.status_code)