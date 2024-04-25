import requests
from bs4 import BeautifulSoup
import csv

# Define the URL of the website to scrape
url = 'https://example.com'

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content of the website using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the elements on the website that contain the data you want to scrape
data = []
for item in soup.find_all('div', class_='data-item'):
    data.append({
        'title': item.find('h2').text,
        'description': item.find('p').text
    })

# Save the scraped data to a CSV file
csv_file = open('scraped_data.csv', 'w')
csv_writer = csv.DictWriter(csv_file, fieldnames=['title', 'description'])
csv_writer.writeheader()

for item in data:
    csv_writer.writerow(item)

csv_file.close()
