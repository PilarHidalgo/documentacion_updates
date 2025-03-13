import os
import json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle

# Ruta del archivo de credenciales
credenciales_file = 'C:/Users/pilar/Downloads/credenciales.json'

# ID de la carpeta de Google Drive
carpeta_id = '1t2Njz8BRs9Lpilg2tL9pOHhLPCsSdXYQ'

# Tipo de archivo que deseas obtener (PDF)
tipo_archivo = 'application/pdf'

# Función para autenticar y obtener el servicio de Google Drive
def obtener_servicio_drive():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credenciales_file, ['https://www.googleapis.com/auth/drive']
            )
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    servicio_drive = build('drive', 'v3', credentials=creds)
    return servicio_drive

# Función para obtener los archivos PDF de la carpeta
def obtener_archivos_pdf(servicio_drive):
    resultados = servicio_drive.files().list(
        q=f"'{carpeta_id}' in parents and trashed=false and mimeType='{tipo_archivo}'",
        fields='nextPageToken, files(id, name)'
    ).execute()

    archivos = resultados.get('files', [])
    return archivos

# Autenticar y obtener el servicio de Google Drive
servicio_drive = obtener_servicio_drive()

# Obtener los archivos PDF de la carpeta
archivos_pdf = obtener_archivos_pdf(servicio_drive)

# Imprimir los resultados
for archivo in archivos_pdf:
    print(f"ID: {archivo['id']}, Nombre: {archivo['name']}")
