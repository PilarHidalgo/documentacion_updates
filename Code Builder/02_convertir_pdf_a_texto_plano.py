import os
import PyPDF2

def pdf_to_text(pdf_path, txt_path):
    """
    Converts a PDF file to a text file.

    Args:
        pdf_path (str): The path to the PDF file to convert.
        txt_path (str): The path to the text file to save the extracted text.
    """
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text = page.extract_text()
                txt_file.write(text)

if __name__ == "__main__":
    # Reemplaza con la ruta a tu archivo PDF
    pdf_path = r'G:\Mi unidad\Folder_test'
    
    # Reemplaza con la ruta donde quieres guardar el archivo de texto
    txt_path = r'C:\Users\pilar\Documents\GitHub\documentacion_updates\documentos'
    
    pdf_to_text(pdf_path, txt_path)
    print(f'El contenido del archivo PDF se ha guardado en {txt_path}')
