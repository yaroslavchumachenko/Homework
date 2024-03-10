import requests

# Function to download and save robots.txt file
def download_robots_txt(url, save_path):
    robots_url = url + '/robots.txt'
    response = requests.get(robots_url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"robots.txt saved successfully to {save_path}")
    else:
        print(f"Failed to download robots.txt from {url}")

download_robots_txt("https://en.wikipedia.org", "wikirobs.txt")