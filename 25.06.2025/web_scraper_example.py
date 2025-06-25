# Filename:  web_scraper_example.py
import requests
from bs4 import BeautifulSoup

def scrape_title(url):
    try:
        response = requests.get(url)
        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)

        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string
        return title
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"
    except AttributeError:
        return "Title not found on page."

url = "https://www.example.com"  # Replace with the URL you want to scrape
title = scrape_title(url)
print(title)