import secrets ,re
from datetime import datetime
from pathlib import Path

# Create a folder to store all notes (if it doesn't exist, create it)
folder = Path('Notes_Folder')
folder.mkdir(exist_ok=True)

# Regex pattern to match a date in the format YYYY-MM-DD
date_regex = re.compile(r'\d{4}-\d{2}-\d{2}')

# Helper function: returns the full path of a note file
def get_note_path(name: str) -> Path:
    return folder / f'{name}.txt'


# Add a new note
def addnote(name: str):
    # If the user does not provide a title, generate a random one
    if not name.strip():
        name = secrets.token_hex(16)

    # Sanitize the name (remove invalid characters for file names)
    name = re.sub(r'[^a-zA-Z0-9_-]', '_', name)

    # Ask the user for note content
    note_content = input('Note: ')

    # Get the current timestamp
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Path to the archives file (stores a history of all notes)
    archives_path = folder / 'archives.txt'
    try:
        # Append the note entry to archives
        with open(archives_path, 'a', encoding='utf-8') as notes:
            notes.write(f'\n{now}\nTitle: {name}\n{note_content}\n')
    except Exception as e:
        print(f'Error writing to archives: {e}')
        return

    # Check if a note with the same name already exists
    note_path = get_note_path(name)
    if note_path.exists():
        # If it exists, append a random suffix to avoid overwriting
        name += secrets.token_hex(2)
        note_path = get_note_path(name)

    # Write the note content into its own file
    try:
        with open(note_path, 'w', encoding='utf-8') as note_file:
            note_file.write(f'{now}\nTitle: {name}\n{note_content}\n{'-'*40}')
        print(f"Note '{name}' saved successfully.")
    except Exception as e:
        print(f'Error saving note: {e}')


# Read an existing note
def readnote(name: str):
    note_path = get_note_path(name)
    try:
        # Open and print the note content
        with open(note_path, 'r', encoding='utf-8') as read_file:
            print('\n' + read_file.read())
    except FileNotFoundError:
        print(f"Error: The note '{name}' does not exist.")
    except Exception as e:
        print(f'Error reading note: {e}')


# Delete an existing note
def deletenote(name: str):
    note_path = get_note_path(name)
    if note_path.exists():
        # Ask the user to confirm deletion
        confirm = input(f"Are you sure you want to delete '{name}'? (yes/no): ").lower().strip()
        if confirm == 'yes':
            try:
                note_path.unlink()  # Delete the file
                print(f"'{name}' has been deleted.")
            except Exception as e:
                print(f'Error deleting note: {e}')
        else:
            print('Deletion cancelled.')
    else:
        print(f"Error: The note '{name}' does not exist.")


# Show all archives
def archives():
    archives_path = folder / 'archives.txt'
    try:
        # Read and print the archives file
        with open(archives_path, 'r', encoding='utf-8') as arch:
            print('\n' + arch.read())
    except FileNotFoundError:
        print('Error: The file archives does not exist.')
    except Exception as e:
        print(f'Error reading archives: {e}')


# List all notes with their creation date
def list_notes():
    print('\nAll Notes:')
    for f in folder.iterdir():
        # Skip directories and the archives file
        if f.is_file() and f.name != 'archives.txt':
            try:
                # Read only the first line (faster than reading the whole file)
                with open(f, 'r', encoding='utf-8') as file:
                    first_line = file.readline()
                    date_match = date_regex.search(first_line)
                    date = date_match.group(0) if date_match else 'Unknown'
                print(f'- {f.stem} (Created: {date})')
            except Exception as e:
                print(f'- {f.stem} (Error reading file: {e})')


# Main app loop
def start():
    print('Welcome to Quick Note!')
    while True:
        # Display menu options
        print('\nChoose an action:')
        print('1 - Add Note')
        print('2 - Read Note')
        print('3 - Delete Note')
        print('4 - Show Archives')
        print('5 - List Notes')
        print('0 - Exit')

        # Get user choice
        choice = input('Enter choice: ').strip()

        if choice == '1':
            note_title = input('Note Title: ')
            addnote(note_title)

        elif choice == '2':
            list_notes()
            note_title = input('\nEnter Note Title to read: ')
            readnote(note_title)

        elif choice == '3':
            list_notes()
            note_title = input('\nEnter Note Title to delete: ')
            deletenote(note_title)

        elif choice == '4':
            archives()

        elif choice == '5':
            list_notes()

        elif choice == '0':
            print('Goodbye!')
            break

        else:
            print('Invalid choice. Please try again.')


# Entry point of the program
if __name__ == '__main__':
    start()

