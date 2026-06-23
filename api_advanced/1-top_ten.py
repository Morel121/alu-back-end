#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.
    If not a valid subreddit, prints None.
    """
    # Target endpoint for hot posts with a limit parameter
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    
    # Custom User-Agent to prevent 429 Too Many Requests errors
    headers = {
        "User-Agent": "linux:com.example.reddit_api_project:v1.0.0 (by /u/sylvain)"
    }
    
    # Send request limiting the data to 10 entries
    params = {"limit": 10}
    
    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )
        
        # If the subreddit is invalid, private, or redirects, print None
        if response.status_code != 200:
            print(None)
            return
        
        # Parse the JSON response
        results = response.json()
        data = results.get("data", {})
        children = data.get("children", [])
        
        # If the subreddit exists but has no posts
        if not children:
            print(None)
            return
            
        # Loop through the children and print each post's title
        for post in children:
            print(post.get("data", {}).get("title"))
            
    except Exception:
        # Fallback in case of any network or parsing error
        print(None)
