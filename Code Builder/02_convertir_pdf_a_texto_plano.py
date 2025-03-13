import PyPDF2

def pdf_to_text(pdf_path, txt_path):
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfFileReader(pdf_file)
        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            for page_num in range(reader.numPages):
                page = reader.getPage(page_num)
                text = page.extract_text()
                txt_file.write(text)

if __name__ == "__main__":
    pdf_path = 'ruta_al_archivo.pdf'  # Reemplaza con la ruta a tu archivo PDF
    txt_path = 'ruta_al_archivo.txt'  # Reemplaza con la ruta donde quieres guardar el archivo de texto
    pdf_to_text(pdf_path, txt_path)
    print(f'El contenido del archivo PDF se ha guardado en {txt_path}')