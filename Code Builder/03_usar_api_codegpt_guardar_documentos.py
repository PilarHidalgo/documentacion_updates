import requests

def authenticate_codegpt(api_key):
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    return headers

def upload_document(headers, document_path, document_name):
    with open(document_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    data = {
        'name': document_name,
        'content': content
    }
    
    response = requests.post('https://api.codegpt.com/v1/documents', headers=headers, json=data)
    
    if response.status_code == 201:
        print(f'Document {document_name} uploaded successfully.')
    else:
        print(f'Failed to upload document {document_name}. Status code: {response.status_code}')
        print(response.json())

if __name__ == "__main__":
    api_key = 'tu_api_key_aqui'  # Reemplaza con tu API key de CodeGPT
    headers = authenticate_codegpt(api_key)
    
    document_path = 'ruta_al_documento.txt'  # Reemplaza con la ruta a tu archivo de texto
    document_name = 'nombre_del_documento'  # Reemplaza con el nombre que quieres darle al documento en CodeGPT
    
    upload_document(headers, document_path, document_name)