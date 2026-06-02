import os
import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup

def run_scraper():
    # URL to scrape
    url = "https://gist.githubusercontent.com/sveinho/515822d919321459357b59621c8fa89e/raw/34cdf525bbc8f854feee4b18df694998034f0d84/gistfile1.html"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    
    # Fetch web page content
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch page: {response.status_code}")
        return

    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")
    
    # Prepare data storage
    file_exists = os.path.isfile("scraped_quotes.csv")
    
    with open("scraped_quotes.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Timestamp", "Quote", "Author"]) # Header
            
        for q in quotes:
            text = q.find("span", class_="text").text
            author = q.find("small", class_="author").text
            writer.writerow([datetime.now().isoformat(), text, author])
            
    print("Scraping completed successfully.")

if __name__ == "__main__":
    run_scraper()
