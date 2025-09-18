# Quick Notes App

**Quick Notes** is a lightweight Python notes application that allows you to create, read, delete, and archive notes efficiently. This project demonstrates good Python practices, file handling, and basic CLI interaction.

## Features

- **Add Notes**: Create notes with a custom title or generate a random title if left blank.
- **Read Notes**: View individual notes by title.
- **Delete Notes**: Delete unwanted notes with a confirmation prompt.
- **Archives**: Maintain a history of all notes with timestamps in `archives.txt`.
- **List Notes**: Quickly see all saved notes with their creation dates.
- **Error Handling**: Robust handling for missing files or invalid operations.
- **Interactive Menu**: User-friendly command-line interface for easy navigation.

## Project Structure

Note_app/
├── notes_app_legacy.py # Original version (initial commit)
├── quick_notes.py # Refactored version with full features
├── Notes_Folder/ # Folder where notes and archives are stored
│ ├── archives.txt
│ └── *.txt # Individual note files
└── README.md

bash
Copy code

## Usage

1. Clone the repository:
```bash
git clone https://github.com/Nadim-Alamleh/Quick_Notes.git
cd Quick_Notes
Run the app:

bash
Copy code
python quick_notes.py
Follow the interactive menu to add, read, delete notes, or view archives.

Notes
The notes_app_legacy.py file shows the initial basic version of the app.

The quick_notes.py file contains the fully refactored version with all features.

All notes are stored in the Notes_Folder directory.

License
This project is open for personal portfolio and educational use.