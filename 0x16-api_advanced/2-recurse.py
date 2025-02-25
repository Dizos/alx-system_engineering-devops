#!/usr/bin/python3
"""
Module for recursively querying the Reddit API to get all hot posts
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query
        hot_list (list, optional): List to store post titles. Defaults to None.
        after (str, optional): Token for pagination. Defaults to None.

    Returns:
        list: List of all hot post titles, or None if subreddit is invalid
    """
    # Initialize hot_list if it's the first call
    if hot_list is None:
        hot_list = []

    # Reddit API URL for getting hot posts
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    
    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/alx_student)"
    }
    
    # Parameters for the API request
    params = {
        "limit": 100  # Maximum allowed by Reddit API
    }
    
    # Add 'after' parameter for pagination if it exists
    if after:
        params["after"] = after
    
    # Make the request to the Reddit API
    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )
    
    # Check if the request was successful (status code 200)
    if response.status_code != 200:
        # Return None for invalid subreddits
        return None
    
    # Parse the JSON response
    data = response.json()
    posts = data.get("data", {}).get("children", [])
    
    # Add post titles to the hot_list
    for post in posts:
        hot_list.append(post.get("data", {}).get("title"))
    
    # Get the 'after' token for the next page
    after = data.get("data", {}).get("after")
    
    # If there's another page, call the function recursively
    if after:
        return recurse(subreddit, hot_list, after)
    
    # Return the complete list when no more pages
    return hot_list
