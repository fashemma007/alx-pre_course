#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers
for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers to a subreddit
    or 0 if invalid
    @param subreddit(str): the subreddit to query
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    # print(url)
    headers = {'User-Agent': 'MyAPI/0.1'}  # avoid TOO MANY REQUESTS error
    resp = requests.get(url, headers=headers)
    if (resp.json().get('error') is not None):
        return 0
    elif resp.json().get('data').get('subscribers') is None:
        return 0
    else:
        return resp.json().get('data').get('subscribers')
