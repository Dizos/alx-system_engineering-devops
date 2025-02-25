#!/usr/bin/python3
"""
Module for querying the Reddit API to get subscriber count
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query

    Returns:
        int: The number of subscribers if the subreddit exists, 0 otherwise
    """
    # Reddit API URL for getting subreddit information
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    
    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/alx_student)"
    }
    
    # Make the request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response and extract subscriber count
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    else:
        # Return 0 for invalid subreddits or other errors
        return 0
