#!/usr/bin/python3
"""
Module for querying the Reddit API to get top 10 hot posts
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query

    Returns:
        None: Prints the titles or None if subreddit is invalid
    """
    # Reddit API URL for getting hot posts
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    
    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/alx_student)"
    }
    
    # Add limit parameter to get only 10 posts
    params = {
        "limit": 10
    }
    
    # Make the request to the Reddit API
    response = requests.get(
        url, 
        headers=headers, 
        params=params, 
        allow_redirects=False
    )
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        
        # Print the titles of the first 10 hot posts
        for post in posts:
            print(post.get("data", {}).get("title", ""))
    else:
        # Print None for invalid subreddits
        print(None)
