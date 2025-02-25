#!/usr/bin/python3
"""
Module for recursively querying the Reddit API to count keywords in hot posts
"""
import requests
import re


def count_words(subreddit, word_list, after=None, word_counts=None):
    """
    Queries the Reddit API, parses the title of all hot articles, and prints a
    sorted count of given keywords (case-insensitive, delimited by spaces).

    Args:
        subreddit (str): The name of the subreddit to query
        word_list (list): List of keywords to count
        after (str, optional): Token for pagination. Defaults to None.
        word_counts (dict, optional): Dictionary to store keyword counts.
                                      Defaults to None.

    Returns:
        None: Prints the counts in the specified format
    """
    # Initialize word_counts dictionary if it's the first call
    if word_counts is None:
        # Convert all words to lowercase and create a dictionary
        word_counts = {}
        for word in word_list:
            word_lower = word.lower()
            if word_lower in word_counts:
                continue
            word_counts[word_lower] = 0

    # If word_list is empty, return without doing anything
    if not word_list:
        return

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
        # Return for invalid subreddits without printing anything
        return

    # Parse the JSON response
    data = response.json()
    posts = data.get("data", {}).get("children", [])

    # Process each post title
    for post in posts:
        title = post.get("data", {}).get("title", "").lower()
        # For each word in the word_list, count occurrences in the title
        for word in word_counts:
            # Use regex to find whole word matches only
            matches = re.findall(r'\b{}\b'.format(re.escape(word)), title)
            word_counts[word] += len(matches)

    # Get the 'after' token for the next page
    after = data.get("data", {}).get("after")

    # If there's another page, call the function recursively
    if after:
        return count_words(subreddit, word_list, after, word_counts)
    else:
        # Print results in the required format when all pages are processed
        # Filter out words with no matches
        filtered_counts = {k: v for k, v in word_counts.items() if v > 0}
        
        # Sort by count (descending) and then alphabetically
        sorted_words = sorted(filtered_counts.items(),
                              key=lambda x: (-x[1], x[0]))
        
        # Print the results
        for word, count in sorted_words:
            print("{}: {}".format(word, count))
