# Text-to-Speech Document Reader

## Overview
This Python script reads text aloud from PDF, Word (.docx), and plain text (.txt) files. It uses a text-to-speech engine to read the content and guides you through selecting a file from your computer.

## How It Works
1. **Start the Program:** When you run the script, it will open a file explorer window.
2. **Choose a File:** You can select a PDF, Word document, or text file from your computer.
3. **Read Aloud:** The script will read the content of the file aloud in chunks and print progress updates in the terminal.

## Prerequisites
To run this script, you need to have Python installed on your computer. You also need to install the following Python libraries:
- **pyttsx3:** This library turns text into speech.
- **PyPDF2:** This library helps read PDF files.
- **docx2txt:** This library reads Word documents.

## Setting Up a Virtual Environment
It's a good idea to use a virtual environment to manage your project's dependencies. This helps avoid conflicts with other Python projects or system-wide packages.

1. **Create a Virtual Environment:** Open your terminal or command prompt and navigate to your project folder. Run the following command:
    ```bash
    python -m venv venv
    ```
   This will create a virtual environment named `venv` in your project directory.

2. **Activate the Virtual Environment:**
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

3. **Install Required Libraries:** With the virtual environment activated, install the necessary libraries using pip:
    ```bash
    pip install pyttsx3 PyPDF2 docx2txt
    ```
   If you encounter issues with the `pyttsx3` library, make sure you have the virtual environment activated and try reinstalling the library.

## How to Run the Script
1. **Open Terminal:** Open your terminal (Command Prompt on Windows or Terminal on macOS/Linux).
2. **Navigate to Script Location:** Use the `cd` command to navigate to the folder where `doc_reader.py` is located. 
    ```bash
    cd path/to/your/script
    ```
3. **Activate Virtual Environment (if using):**
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
4. **Run the Script:** Execute the script by running:
    ```bash
    python doc_reader.py
    ```
5. **Select a File:** A file explorer window will pop up. Choose the file you want to be read aloud.

## Features
- **File Handling:** Supports reading from PDF, Word (.docx), and plain text (.txt) files.
- **Text-to-Speech:** Reads the text aloud in chunks.
- **Terminal Output:** Shows which page or file is being read and informs you when reading is complete.

## Known Issues and Limitations
- **Navigation Errors:** Attempted navigation features caused errors. The script currently reads the entire file from start to end without navigation options.
- **No User Interface:** Due to time constraints, no graphical user interface (GUI) was created. The script runs in the terminal and uses file dialogs for file selection.

## Submission Notes
- **Functionality Focus:** The script focuses on functionality and demonstrates how to read text aloud from different file types.
- **Challenges:** Faced challenges with adding navigation and a user interface due to time limitations.

## Additional Tips
- **Be Patient:** If the reading takes a while, the script is processing the text in manageable chunks.
- **Review Output:** The terminal will show progress messages to keep you informed of what’s happening.

## Development Environment
- **IDE:** Developed using Visual Studio Code (VS Code).
- **Operating System:** Windows OS.

## Conclusion
This script is a work in progress and demonstrates basic text-to-speech capabilities. Future enhancements could include navigation features and a more user-friendly interface.
