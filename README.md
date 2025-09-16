# Note App
A simple Python application for creating and managing notes. This program allows users to add notes with unique titles, automatically generates titles if none are provided, and saves all notes in a central file (`All_Notes.txt`) as well as in individual text files. Notes are organized in a dedicated folder (`Notes_Folder`) with unique filenames

## Features
- **Create Notes:** Add notes with a title and content.- **Auto-Generated Titles:** If no title is provided, a random title is generated.- **Centralized Storage:** All notes are logged in a single file (`All_Notes.txt`).- **Individual Files:** Each note is saved in its own text file for easy access.- **Unique Filenames:** Ensures no duplicate filenames by appending random tokens if necessar

## How to Run1.
 Make sure you have Python installed on your system (Python 3.6 or higher is recommended).2. Clone this repository or download the `Note_app.py` file.3. Open a terminal and navigate to the project directory.4. Run the script using the following command:   ```bash   python Note_app.py

How It Works

The program prompts the user to enter a title and content for the note.
If no title is provided, a random title is generated.
The note is saved in two places:
All_Notes.txt: A central file that logs all notes.
Individual Files: Each note is saved as a separate text file in the Notes_Folder directory.
The program ensures that filenames are unique by appending random tokens if a file with the same name already exists.

Folder Structure

Notes_Folder/├── All_Notes.txt       # Central file containing all notes├── <note_title>.txt    # Individual note files
Example
Input:

Title: My First NoteNote: This is the content of my first note.
Output:
Notes_Folder/All_Notes.txt:


2025-09-16 14:30:00Title: My First NoteThis is the content of my first note.
Notes_Folder/My_First_Note.txt:


2025-09-16 14:30:00Title: My First NoteThis is the content of my first note.----------------------------------------

Future Improvements

Add functionality to view, edit, or delete existing notes.
Implement a search feature to find notes by title or content.
Create a graphical user interface (GUI) for easier interaction.

License
This project is open-source and available under the MIT License.

Author
Developed by Nadim Alamleh.