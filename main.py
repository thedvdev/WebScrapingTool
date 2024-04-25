import csv
import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the elements you want to scrape
    data = soup.find_all('div', {'class': 'product-item'})

    # Create a list to store the scraped data
    scraped_data = []

    # Extract the relevant data from each element (You can change it to whatever you want)
    for item in data:
        title = item.find('h2').text.strip()
        price = item.find('span', {'class': 'price'}).text.strip()
        description = item.find('p', {'class': 'description'}).text.strip()
        image_url = item.find('img')['src']

        # Create a dictionary for each item and append it to the list
        product_data = {
            'Title': title,
            'Price': price,
            'Description': description,
            'Image URL': image_url
        }
        scraped_data.append(product_data)

    return scraped_data

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Title', 'Price', 'Description', 'Image URL']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for item in data:
            writer.writerow(item)

# Example usage
url = 'https://www.example.com'
scraped_data = scrape_website(url)
save_to_csv(scraped_data, 'scraped_data.csv')
