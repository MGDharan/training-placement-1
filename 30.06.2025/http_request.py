# Filename:  http_request.py
import requests
def make_http_request(url):
    """Makes an HTTP GET request to a given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"