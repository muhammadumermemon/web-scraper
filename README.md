# Web Scraping Script

This repository contains a simple web scraping script written in Python. The script uses the `requests` library to fetch the content of a webpage and `BeautifulSoup` to parse the HTML content.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. **Install the required libraries:**

    ```bash
    pip install requests beautifulsoup4
    ```

## Usage

1. **Update the URL:**

    Open the `script.py` file and update the `url` variable with the URL of the website you want to scrape.

    ```python
    url = 'https://example.com'
    ```

2. **Run the script:**

    Execute the script using Python:

    ```bash
    python script.py
    ```

3. **Output:**

    The script will print the title of the page and all paragraph texts found on the webpage.

## Example

Here's an example of how the script works:

```python
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
