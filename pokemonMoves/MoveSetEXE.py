import tkinter as tk
from tkinter import filedialog  # Import the filedialog module
import os

# Define the directory where your text files are located
directory = 'K:\Python bot\pokemonMoves\output'

# Define a function to select a directory using the file dialog
def browse_directory():
    global directory  # Use the global variable directory
    directory = filedialog.askdirectory()
    directory_entry.delete(0, tk.END)
    directory_entry.insert(0, directory)

# Function to update the Listbox based on the current input
def update_listbox(event):
    current_text = event.widget.get().lower()
    suggestions = [file for file in file_names if file.lower().startswith(current_text)]
    list_box = list_box_dict[event.widget]
    list_box.delete(0, tk.END)
    if current_text == '':
        return
    for suggestion in suggestions:
        list_box.insert(tk.END, suggestion)

# Function to display the content of a selected .txt file in the big box
def display_file_content(event, list_box):
    selected_indices = list_box.curselection()
    if not selected_indices:
        return  # No selection, nothing to display

    selected_contents = []

    for index in selected_indices:
        selection = list_box.get(index)
        file_name = selection.split(".txt")[0]
        file_path = os.path.join(directory, file_name + ".txt")
        if os.path.exists(file_path) and os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = set(file.read().splitlines())
                selected_contents.append(content)

    if selected_contents:
        common_lines = set.intersection(*selected_contents)

        big_text_box.config(state=tk.NORMAL)  # Enable text box for writing
        big_text_box.delete('1.0', tk.END)  # Clear the existing content
        for line in common_lines:
            big_text_box.insert(tk.END, line + '\n')  # Insert each common line
        big_text_box.config(state=tk.DISABLED)  # Disable text box for reading

# Function to perform the search and select the first item in list_box2
def perform_search():
    big_text_box.config(state=tk.NORMAL)  # Enable text box for writing
    big_text_box.delete('1.0', tk.END)
    big_text_box.config(state=tk.DISABLED)
    
    selected_files = []
    list_box = [list_box1, list_box2, list_box3, list_box4]
    current_text = [text_box1_var.get().lower(),
                    text_box2_var.get().lower(),
                    text_box3_var.get().lower(),
                    text_box4_var.get().lower()
                    ]
    
    for i, text in enumerate(current_text):
        if text:
            suggestions = [file for file in file_names if file.lower().startswith(text)]
            if suggestions:
                list_box[i].select_set(0)
                selected_files.append(suggestions[0])
    
    common_lines = set()
    for file_name in selected_files:
        file_path = os.path.join(directory, file_name + ".txt")
        if os.path.exists(file_path) and os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = set(file.read().splitlines())
                if not common_lines:
                    common_lines = content
                else:
                    common_lines &= content
    
    common_lines = sorted(common_lines)  # Sort the common lines
    
    if common_lines:
        big_text_box.config(state=tk.NORMAL)  # Enable text box for writing
        big_text_box.delete('1.0', tk.END)
        for line in common_lines:
            big_text_box.insert(tk.END, line + '\n')  # Insert each sorted common line
        big_text_box.config(state=tk.DISABLED)  # Disable text box for reading

def reset_text_fields():
    text_box1_var.set('')
    text_box2_var.set('')
    text_box3_var.set('')
    text_box4_var.set('')
    list_box1.delete(0, tk.END)
    list_box2.delete(0, tk.END)
    list_box3.delete(0, tk.END)
    list_box4.delete(0, tk.END)
    big_text_box.config(state=tk.NORMAL)
    big_text_box.delete('1.0', tk.END)
    big_text_box.config(state=tk.DISABLED)

# Create the main application window
app = tk.Tk()
app.title("Autofill Example")

# Add a Label and an Entry widget for directory selection
directory_label = tk.Label(app, text="Directory:")
directory_label.grid(row=5, column=0, padx=5, pady=5)
directory_entry = tk.Entry(app, width=30)
directory_entry.insert(0, directory)  # Set the initial directory in the Entry widget
directory_entry.grid(row=5, column=1, padx=5, pady=5)
browse_button = tk.Button(app, text="Browse", command=browse_directory)
browse_button.grid(row=5, column=2, padx=5, pady=5)

# Get a list of file names in the directory without the .txt extension
file_names = [file[:-4] for file in os.listdir(directory) if file.endswith('.txt')]

# Rest of your code...

# Create Text widgets and Listboxes for typing and suggestions
text_box1_var = tk.StringVar()
text_box1 = tk.Entry(app, textvariable=text_box1_var, width=30)
text_box1.bind('<KeyRelease>', update_listbox)
text_box1.grid(row=0, column=0, padx=5, pady=5)
list_box1 = tk.Listbox(app, height=1, width=30, selectmode=tk.SINGLE)
list_box1.grid(row=0, column=1, padx=5, pady=5)

text_box2_var = tk.StringVar()
text_box2 = tk.Entry(app, textvariable=text_box2_var, width=30)
text_box2.bind('<KeyRelease>', update_listbox)
text_box2.grid(row=1, column=0, padx=5, pady=5)
list_box2 = tk.Listbox(app, height=1, width=30, selectmode=tk.SINGLE)
list_box2.grid(row=1, column=1, padx=5, pady=5)

text_box3_var = tk.StringVar()
text_box3 = tk.Entry(app, textvariable=text_box3_var, width=30)
text_box3.bind('<KeyRelease>', update_listbox)
text_box3.grid(row=2, column=0, padx=5, pady=5)
list_box3 = tk.Listbox(app, height=1, width=30, selectmode=tk.SINGLE)
list_box3.grid(row=2, column=1, padx=5, pady=5)

text_box4_var = tk.StringVar()
text_box4 = tk.Entry(app, textvariable=text_box4_var, width=30)
text_box4.bind('<KeyRelease>', update_listbox)
text_box4.grid(row=3, column=0, padx=5, pady=5)
list_box4 = tk.Listbox(app, height=1, width=30, selectmode=tk.SINGLE)
list_box4.grid(row=3, column=1, padx=5, pady=5)

reset_button = tk.Button(app, text="Reset", command=reset_text_fields)
reset_button.grid(row=4, column=1, padx=5, pady=5)

# Create a dictionary to map text boxes to list boxes
list_box_dict = {
    text_box1: list_box1,
    text_box2: list_box2,
    text_box3: list_box3,
    text_box4: list_box4
}

# Create a big Text widget on the right side with read-only
big_text_box = tk.Text(app, height=6.5, width=50, state=tk.DISABLED)
big_text_box.grid(row=0, column=2, rowspan=4, padx=5, pady=5)

# Create a "Search" button
search_button = tk.Button(app, text="Search", command=perform_search)
search_button.grid(row=4, column=0, padx=5, pady=5)

# Configure grid weights to make the layout expandable
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(2, weight=1)

# Start the Tkinter main loop
app.mainloop()
