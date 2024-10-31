import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = 'https://example.com'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find and print the title of the page
    title = soup.find('title').get_text()
    print('Page Title:', title)
    
    # Example: Find and print all paragraph texts
    paragraphs = soup.find_all('p')
    for p in paragraphs:
        print(p.get_text())
else:
    print('Failed to retrieve the webpage')
