import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Provide the URL of the web page
url = 'https://bulbapedia.bulbagarden.net/wiki/List_of_moves'

# Provide the CSS selector to target the <tbody> element
css_selector = '#mw-content-text > div > table:nth-child(5) > tbody > tr > td > table > tbody'

# Fetch the HTML content of the web page
response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    # Find the <tbody> element using the provided CSS selector
    tbody = soup.select_one(css_selector)

    if tbody:
        # Find all <tr> tags (table rows) within the <tbody>
        rows = tbody.find_all('tr')

        # Extract and print the link from the 2nd <td> in each <tr>
        for row in rows:
            # Find all <td> tags (table cells) within the <tr>
            cells = row.find_all('td')

            if len(cells) > 1:  # Ensure there's a 2nd <td> in the row
                second_td = cells[1]  # Get the 2nd <td>
                link = second_td.find('a')

                if link:
                    name = link.get_text()
                    href = urljoin(url, link.get('href'))  # Convert to full URL
                    print(f"Name: {name}, Full Link: {href}")

        # You can also save these links to a text file if needed
        # Example: Save the names and full hyperlinks to a text file
        with open('links_from_2nd_td.txt', 'w') as file:
            for row in rows:
                cells = row.find_all('td')

                if len(cells) > 1:
                    second_td = cells[1]
                    link = second_td.find('a')

                    if link:
                        name = link.get_text()
                        href = urljoin(url, link.get('href'))
                        file.write(f"Name: {name}, Full Link: {href}\n")

        print(f"Data saved to 'links_from_2nd_td.txt'.")
    else:
        print("Data not found within the provided <tbody> CSS selector.")
else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")
