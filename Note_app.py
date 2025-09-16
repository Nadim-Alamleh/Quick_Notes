import secrets, re  # Importing secrets for generating random tokens and re for regular expressions
from datetime import datetime  # Importing datetime to get the current date and time
from pathlib import Path  # Importing Path to handle file and folder paths

# Create a folder named 'Notes_Folder' if it doesn't already exist
folder = Path('Notes_Folder')
folder.mkdir(exist_ok=True)

def addnote():
    # Prompt the user to enter a title for the note
    note_title = input('Title: ')

    # If the user doesn't provide a title, generate a random one
    if note_title == '':
        note_title = secrets.token_hex(16)
    
    # Sanitize the title by replacing invalid characters with underscores
    note_title = re.sub(r'[^a-zA-Z0-9_-]', '_', note_title)

    # Prompt the user to enter the content of the note
    note_content = input("Note: ")

    # Get the current date and time
    now = datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M:%S")

    # Define the path for the file that stores all notes
    all_notes_path = 'Notes_Folder/All_Notes.txt'

    # Append the note to the 'All_Notes.txt' file
    with open(all_notes_path, 'a') as notes:
        notes.write(f'\n{time}\nTitle: {note_title}\n{note_content}\n')

    # Define the path for the folder where individual note files will be stored
    Folder_path = Path("Notes_Folder")

    # Check if a file with the same title already exists, and if so, generate a unique title
    for file in Folder_path.glob("*.txt"):
        if file.name == f'{note_title}.txt':
            note_title = f'{note_title}{secrets.token_hex(2)}'

    # Define the path for the individual note file
    note_path = f'Notes_Folder/{note_title}.txt'

    # Write the note to its own file
    with open(note_path, 'w') as note_file:
        note_file.write(f'{time}\nTitle: {note_title}\n{note_content}\n{'-'*40}')

# Infinite loop to allow the user to add multiple notes
while True:
    addnote()  # Call the function to add a new note
    another_note = input('Do you want to add another note (yes/no): ').lower().strip()

    # If the user enters 'no', exit the loop and end the program
    if another_note == 'no':
        break
    else:
        continue  # If the user enters 'yes' or anything else,


