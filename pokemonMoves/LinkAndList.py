import os
import requests
from bs4 import BeautifulSoup

# Create an 'output' folder if it doesn't exist
output_folder = 'output'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


# Provide the path to the file containing "Name" and "Full Link" information
input_file = 'MovesAndLinks.txt'

# Initialize a list to store the extracted data
data_list = []

# Read the lines from the input file
with open(input_file, 'r') as file:
    lines = file.readlines()

# Extract "Name" and "Full Link" from each line and store it in data_list
for line in lines:
    parts = line.strip().split(", ")
    name = parts[0].replace("Name: ", "")
    link = parts[1].replace("Full Link: ", "")
    data_list.append((name, link))

# Iterate through the extracted data
for name, url in data_list:
    # Define the output file name based on the "Name"
    file_name = name
    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        # Find the span element with class 'mw-headline' and ID 'Learnset'
        learnset_span = soup.find('span', class_='mw-headline', id='Learnset')

        if learnset_span:
            # Find the parent heading (h2, h3, etc.)
            parent_heading = learnset_span.find_parent(['h2', 'h3'])

            if parent_heading:
                # Find all tables under the parent heading (e.g., <h2> or <h3>)
                tables = parent_heading.find_all_next('table', class_='roundy')

                # Create a list to store the table data
                table_data_list = []

                # Iterate through the tables
                for table in tables:
                    # Extract data from the 1st and 3rd columns of each table with a colon in between
                    for row in table.find_all('tr'):
                        cols = row.find_all(['th', 'td'])

                        # Check if the row has at least three columns
                        if len(cols) >= 3:
                            # Select the 1st and 3rd columns and join them with a colon
                            selected_cols = [cols[0].get_text(strip=True), cols[2].get_text(strip=True)]
                            row_data = ':'.join(selected_cols)

                            # Check if the row starts with a number (digit)
                            if row_data.strip() and row_data[0].isdigit():
                                table_data_list.append(row_data)

                # Add '0' to the front of lines starting with 'A' and remove duplicates
                table_data_list = ['0' + line if line[0] == 'A' else line for line in table_data_list]
                table_data_list = list(dict.fromkeys(table_data_list))

                # Sort the table data
                table_data_list.sort()

                # Save the table data to a single text file in the 'output' folder
                file_name = name.replace(' ', '')  # Replace spaces with nothing in the file name
                file_path = os.path.join(output_folder, f'{file_name}.txt')
                with open(file_path, 'w', encoding='utf-8') as file:
                    for row_data in table_data_list:
                        file.write(row_data + '\n')

                print(f"Table data for '{name}' saved to '{file_path}', sorted and duplicates removed.")
            else:
                print(f"Parent heading (h2, h3, etc.) not found after Learnset span for '{name}'.")
        else:
            print(f"Learnset span not found for '{name}'.")
    else:
        print(f"Failed to retrieve the web page for '{name}'. Status code: {response.status_code}")
