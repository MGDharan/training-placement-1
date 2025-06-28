# Filename: web_scraper.py
import requests
from bs4 import BeautifulSoup

def scrape_website(url, target_element):
    response = requests.get(url)
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

    soup = BeautifulSoup(response.content, 'html.parser')
    target_elements = soup.select(target_element)
    data = [element.text.strip() for element in target_elements]
    return data