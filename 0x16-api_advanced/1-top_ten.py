#!/usr/bin/python3
"""queries the Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """ returns top 10 hot posts
    @param subreddit (str): subreddit to query
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'MyAPI/0.1'}  # avoid TOO MANY REQUESTS error
    resp = requests.get(url, headers=headers, allow_redirects=False)
    if (resp.status_code == 404):
        print(None)
    else:
        for post in resp.json().get('data').get('children'):
            print(post.get('data').get('title'))
