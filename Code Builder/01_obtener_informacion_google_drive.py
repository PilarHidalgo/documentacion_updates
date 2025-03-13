from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def authenticate_drive():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()  # Creates local webserver and auto handles authentication.
    drive = GoogleDrive(gauth)
    return drive

def list_files_in_drive(drive):
    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    for file in file_list:
        print(f'Title: {file["title"]}, ID: {file["id"]}')

def download_file(drive, file_id, output_path):
    file = drive.CreateFile({'id': file_id})
    file.GetContentFile(output_path)
    print(f'File {file["title"]} downloaded to {output_path}')

if __name__ == "__main__":
    drive = authenticate_drive()
    list_files_in_drive(drive)
    # Example usage: download a file by its ID
    # download_file(drive, 'your_file_id_here', 'output_path_here')