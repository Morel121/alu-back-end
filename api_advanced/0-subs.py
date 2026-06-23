#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API for a specific subreddit's total subscribers.
    Returns 0 if the subreddit is invalid or an error occurs.
    """
    # Target endpoint for subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Custom User-Agent to avoid 'Too Many Requests' (429) errors
    headers = {
        "User-Agent": "linux:com.example.reddit_api_project:v1.0.0 (by /u/sylvain)"
    }
    
    try:
        # allow_redirects=False prevents following search result redirects for fake subreddits
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # If the status code is not 200 (OK), the subreddit is invalid or private
        if response.status_code != 200:
            return 0
            
        # Parse the JSON and pull the total subscribers count
        results = response.json()
        return results.get("data", {}).get("subscribers", 0)
        
    except Exception:
        # Fallback to 0 if anything unexpected happens (network issue, parsing error, etc.)
        return 0
