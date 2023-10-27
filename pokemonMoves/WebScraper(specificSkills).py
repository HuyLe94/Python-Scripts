import requests
from bs4 import BeautifulSoup

# Provide the URL of the web page you want to scrape
url = 'https://bulbapedia.bulbagarden.net/wiki/Super_Fang_(move)'  # Replace with the actual URL

# Define a name for the text file
file_name = 'Super Fang'

# Fetch the HTML content of the web page
response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    # Define a list of span IDs
    span_ids = ['By_leveling_up', 'By_TM', 'By_TM.2FHM.2FTR' , 'By_TM.2FHM' , 'By_TM.2FTR' , 'By_HM.2FTR' , 'By_breeding']

    # Define the common span class
    span_class = 'mw-headline'

    # Create a list to store the table data
    table_data_list = set()  # Use a set to remove duplicates

    # Iterate through the span IDs and corresponding tables
    for span_id in span_ids:
        # Find the span with the specific class and ID
        span = soup.find('span', class_=span_class, id=span_id)

        if span:
            # Find the next table element with the specified class
            table = span.find_next('table', class_='roundy')

            if table:
                # Extract data from the 1st and 3rd columns of the table with a colon in between
                for row in table.find_all('tr'):
                    cols = row.find_all(['th', 'td'])

                    # Check if the row has at least three columns
                    if len(cols) >= 3:
                        # Select the 1st and 3rd columns and join them with a colon
                        selected_cols = [cols[0].get_text(strip=True), cols[2].get_text(strip=True)]
                        row_data = ':'.join(selected_cols)

                        # Check if the row starts with a number (digit)
                        if row_data.strip() and row_data[0].isdigit():
                            table_data_list.add(row_data)

            else:
                print(f"No table with class 'roundy' found after the specified span.")
        else:
            print(f"Span with class '{span_class}' and ID '{span_id}' not found.")

    # Sort the lines by their starting numbers
    sorted_data = sorted(table_data_list, key=lambda line: int(line.split(':')[0]) if line.strip() and line[0].isdigit() else float('inf'))

    # Save unique table data (1st and 3rd columns with a colon) to a single text file with the specified name
    file_path = f'{file_name}.txt'
    with open(file_path, 'w', encoding='utf-8') as file:
        for row_data in sorted_data:
            file.write(row_data + '\n')

    print(f"Table data (1st and 3rd columns with a colon) saved to '{file_path}', sorted by starting numbers, and duplicates removed.")
else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")
