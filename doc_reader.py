import pyttsx3  # Import the library that turn text into speech
import docx2txt  # Import the library for reading Word documents
import PyPDF2  # Import the library for reading PDF files
import os  # Import library for handling files and directories
import time  # Import library to use time-related functions

# Setting up the text-to-speech engine
engine = pyttsx3.init()

# here are variables to keep track of what is going on
current_page = 0  # This will tell  which page we're on
text = ""  # this stores the text we want to read aloud
reading_in_progress = False  # this is  to make sure we're not reading multiple things at once

#this function reads text out loud in chunks
def read_aloud_in_chunks(text, page_num):
    global current_page, reading_in_progress
    
    if reading_in_progress:  # this just means if  we’re already reading, just stop and do nothing
        return
    
    reading_in_progress = True  # Mark that reading has started
    chunk_size = 1000  # How big each chunk of text should be
    current_page = page_num  

    # here , go through the text and read it in chunks
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]  # gets a part of the text
        engine.say(chunk)  # Add this chunk to the speech queue
        print(f"Reading page {page_num}...")  # shows which page is being read
        engine.runAndWait()  # actually speak out the text we just added

    print(f"Finished reading page {page_num}.")  # confirm the read aloud is  done with this page
    reading_in_progress = False  # reading is done, so reset the flag

# this function deals with PDF files
def read_pdf(file_path):
    global current_page, text
    
    try:
        with open(file_path, 'rb') as file:  # opens the PDF file in read-binary mode
            pdf_reader = PyPDF2.PdfReader(file)  # creating a PDF reader object
            text = ""
            # goes  through each page and extract text
            for page in pdf_reader.pages:
                text += page.extract_text()

        print("Instructions:")
        print("Reading PDF file...")

        # Starts reading from the first page
        read_aloud_in_chunks(text, 1)
        
    except Exception as e:
        print(f"Oops! Something went wrong with the PDF: {e}")

# this function deals with Word documents
def read_word(file_path):
    global current_page, text
    
    try:
        text = docx2txt.process(file_path)  # extracts text from the Word file
        lines = text.splitlines()  # breaks the text into lines

        print("Instructions:")
        print("Reading Word file...")

        # joining the lines back into a single string and start reading
        text_to_read = "\n".join(lines)
        read_aloud_in_chunks(text_to_read, 1)
        
    except Exception as e:
        print(f"Oops! Something went wrong with the Word file: {e}")

# this function deals with plain text files
def read_text(file_path):
    global current_page, text
    
    try:
        with open(file_path, 'r') as file:  # opens the text file
            text = file.read()  
            lines = text.splitlines()  #break the text into lines

        print("Instructions:")
        print("Reading text file...")

        # join the lines into a single string and start reading
        text_to_read = "\n".join(lines)
        read_aloud_in_chunks(text_to_read, 1)
        
    except Exception as e:
        print(f"Oops! Something went wrong with the text file: {e}")

# this function lets you pick a file and then reads it
def open_file():
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename

    Tk().withdraw()  # Hide the Tkinter window
    file_path = askopenfilename()  # opens a file dialog to pick a file

    #checks what type of file it is and call the right function
    if file_path.lower().endswith('.pdf'):
        read_pdf(file_path)  
    elif file_path.lower().endswith('.docx'):
        read_word(file_path) 
    elif file_path.lower().endswith('.txt'):
        read_text(file_path) 
    else:
        print("Sorry, I can't handle this file format!")  #lets the user know if the file type isn’t supported

# start the whole process of selecting a file and reading it
open_file()
