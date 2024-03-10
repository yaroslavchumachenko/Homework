import requests
import json

def get_data(url, params):
    r = requests.get(url, params=params)
    print ("Requests sent to: ", r.url)
    return r.json()

base_url = "https://api.pushshift.io/reddit/comment/search/"
subreddit = "askscience"


comments = get_data(base_url, {"subreddit" : "python"}) #or subbredit

with open('askscience_comments.json', 'w') as file:
    json.dump(comments, file, indent=4)

# for comment in comments:
#     print(comment['body'])