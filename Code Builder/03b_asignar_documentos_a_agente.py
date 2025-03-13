import requests

def authenticate_codegpt(api_key):
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    return headers

def assign_document_to_agent(headers, document_id, agent_id):
    data = {
        'document_id': document_id
    }
    
    response = requests.post(f'https://api.codegpt.com/v1/agents/{agent_id}/documents', headers=headers, json=data)
    
    if response.status_code == 200:
        print(f'Document {document_id} assigned to agent {agent_id} successfully.')
    else:
        print(f'Failed to assign document {document_id} to agent {agent_id}. Status code: {response.status_code}')
        print(response.json())

if __name__ == "__main__":
    api_key = 'tu_api_key_aqui'  # Reemplaza con tu API key de CodeGPT
    headers = authenticate_codegpt(api_key)
    
    document_id = 'id_del_documento'  # Reemplaza con el ID del documento que quieres asignar
    agent_id = 'id_del_agente'  # Reemplaza con el ID del agente al que quieres asignar el documento
    
    assign_document_to_agent(headers, document_id, agent_id)