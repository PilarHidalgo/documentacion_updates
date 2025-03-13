"""
Module for converting PDF files to text and copying them to a destination folder.

This module provides functions for listing PDF files in a directory, converting them to text,
saving the text to a file, and copying the PDF files to a destination folder.
"""

import os
import shutil
import PyPDF2

def list_pdf_files(directory: str) -> list:
    """
    Lists all PDF files in the specified directory.

    Args:
        directory (str): The path to the directory to list PDF files from.

    Returns:
        list: A list of PDF file names in the directory.
    """
    pdf_files = [f for f in os.listdir(directory) if f.endswith('.pdf')]
    return pdf_files

def convert_pdf_to_text(pdf_path: str) -> str:
    """
    Converts a PDF file to text.

    Args:
        pdf_path (str): The path to the PDF file to convert.

    Returns:
        str: The text extracted from the PDF file.
    """
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def save_text_to_file(text: str, output_path: str) -> None:
    """
    Saves the given text to a file.

    Args:
        text (str): The text to save.
        output_path (str): The path to the file to save the text to.
    """
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(text)

def copy_pdf_to_folder(pdf_path: str, destination_folder: str) -> None:
    """
    Copies a PDF file to a destination folder.

    Args:
        pdf_path (str): The path to the PDF file to copy.
        destination_folder (str): The path to the folder to copy the PDF file to.
    """
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    shutil.copy(pdf_path, destination_folder)
    print(f'Copied {pdf_path} to {destination_folder}')

def main() -> None:
    """
    The main function that coordinates the conversion and copying of PDF files.
    """
    source_directory = r'G:\Mi unidad\Folder_test'
    destination_directory = r'C:\Users\pilar\Documents\GitHub\documentacion_updates\documentos'
    
    pdf_files = list_pdf_files(source_directory)
    
    for pdf_file in pdf_files:
        pdf_path = os.path.join(source_directory, pdf_file)
        
        # Convert PDF to text and save
        text = convert_pdf_to_text(pdf_path)
        output_text_path = os.path.splitext(pdf_path)[0] + '.txt'
        save_text_to_file(text, output_text_path)
        print(f'Converted {pdf_file} to text and saved to {output_text_path}')
        
        # Copy PDF to destination folder
        copy_pdf_to_folder(pdf_path, destination_directory)

if __name__ == "__main__":
    main()
