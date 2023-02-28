#!/usr/bin/python3
""" returns a list containing the titles of all hot articles """
import requests


def recurse(subreddit, hot_list=[], at=0):
    """ function to get top hot posts

    Args:
        subreddit (string): subreddit queried
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'MyAPI/0.1'}
    resp = requests.get(url, headers=headers, allow_redirects=False)
    try:  # handling invalid subreddits
        # children is a list of dicts
        children = resp.json().get('data').get('children')
    except AttributeError:
        return None
    # print(children)
    # using loops, sytanx would be:
    # [print(child.get('data').get('title')) for child in children]
    length = len(children)
    title = children[at].get('data').get('title')
    if (resp.json().get('error') == 404):
        return None
    if at < length:
        hot_list.append(title)
        at += 1
        # print(at)
        try:
            return recurse(subreddit, hot_list, at)
        except IndexError:
            return hot_list
    else:
        return hot_list
