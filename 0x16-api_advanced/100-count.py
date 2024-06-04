#!/usr/bin/python3
"""Contains the count_words function"""
import requests


def count_words(subreddit, word_list, found_list=[], after=None):
    '''Prints counts of given words found in hot posts of a given subreddit
    '''
    user_agent = {'User-agent': 'test'}
    posts = requests.get('http://www.reddit.com/r/{}/hot.json?after={}'
                         .format(subreddit, after), headers=user_agent)
    if after is None:
        word_list = [word.lower() for word in word_list]

    if posts.status_code != 200:
        return
    else:
        posts = posts.json()['data']
        after = posts['after']
        posts = posts['children']
        for post in posts:
            title = post['data']['title'].lower()
            for word in title.split(' '):
                if word in word_list:
                    found_list.append(word)
        if after is not None:
            count_words(subreddit, word_list, found_list, after)
        else:
            result = {}
            for word in found_list:
                ans = result.get(word.lower(), 0)
                result[word.lower()] = ans + 1
            for key, value in sorted(result.items(), key=lambda item: item[1],
                                     reverse=True):
                print('{}: {}'.format(key, value))
