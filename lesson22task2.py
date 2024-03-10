import requests


subreddit = "announcement"

def download_comms(subreddit, auth ={"user", "pass"}):
    # url = f"https://api.pushshift.io/reddit/comment/search/?subreddit={subreddit}"
    url = "https://api.pushshift.io/reddit/search/comment/?q=science"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        comments = data['data']
        for comment in comments:
            print(comment['body'])  # Print or process the comment as needed
    else:
        print(f"Failed to download comments from subreddit '{subreddit}'")
        print(response.status_code)

download_comms(subreddit=subreddit, auth= {"LuckUp", "yub19102"})