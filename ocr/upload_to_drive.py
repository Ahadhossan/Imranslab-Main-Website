#!/usr/bin/env python3
import os
import sys
import argparse
import logging
import random
import string
from datetime import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from googleapiclient.errors import HttpError
from io import BytesIO

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


def get_drive_service(key_file: str, scopes: list):
    try:
        creds = service_account.Credentials.from_service_account_file(key_file, scopes=scopes)
        return build('drive', 'v3', credentials=creds)
    except Exception as e:
        logging.error(f"Failed to create Google Drive service: {e}")
        sys.exit(1)

def upload_to_drive(key_file: str, folder_id: str, file_path: str):
    if not os.path.exists(file_path):
        logging.error(f"File not found: {file_path}")
        sys.exit(1)

    service = get_drive_service(key_file, ['https://www.googleapis.com/auth/drive'])
    file_name = os.path.basename(file_path)
    metadata = {'name': file_name}
    if folder_id:
        metadata['parents'] = [folder_id]

    media = MediaFileUpload(file_path, resumable=True)

    try:
        logging.info(f"Uploading '{file_name}' to Google Drive...")
        file = service.files().create(
            body=metadata,
            media_body=media,
            fields='id,name,webViewLink'
        ).execute()

        print(f'Uploaded {file_name} with ID: {file["id"]}')
        print(f'Verified upload: name="{file["name"]}", link={file["webViewLink"]}')
    except HttpError as e:
        logging.error(f"Upload failed: {e}")
        sys.exit(1)


def verify_file(key_file: str, file_id: str, local_path: str):
    service = get_drive_service(key_file, ['https://www.googleapis.com/auth/drive'])
    try:
        # 1) Fetch metadata
        f = service.files().get(fileId=file_id, fields='id,name,webViewLink').execute()
        print(f'id:{f["id"]}')
        print(f'name:{f["name"]}')
        print(f'link:{f["webViewLink"]}')

        # 2) Download remote content
        request = service.files().get_media(fileId=file_id)
        fh = BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while not done:
            _, done = downloader.next_chunk()
        remote_content = fh.getvalue().decode('utf-8')

        # 3) Read local content
        with open(local_path, 'r') as lf:
            local_content = lf.read()

        # 4) Compare
        if remote_content == local_content:
            print('Content matches local file')
        else:
            print('Content mismatch!')
            print('=== Remote Content ===')
            print(remote_content)
            print('=== Local Content ===')
            print(local_content)
            sys.exit(1)

    except HttpError as e:
        logging.error(f"Verification failed: {e}")
        sys.exit(1)

def create_random_file() -> str:
    timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H%M%SZ')
    file_name = f"{timestamp}.txt"
    content = ''.join(random.choices(string.ascii_letters + string.digits, k=100))
    with open(file_name, 'w') as f:
        f.write(content)
    logging.info(f"Created random file: {file_name}")
    return file_name

def main():
    parser = argparse.ArgumentParser(description="Upload, verify, or create a random file")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--upload', action='store_true', help='Upload a file to Drive')
    group.add_argument('--verify', action='store_true', help='Verify a file by ID')
    group.add_argument('--create', action='store_true', help='Create a random .txt file with UTC timestamp')

    parser.add_argument('--key', help='Path to service account JSON key')
    parser.add_argument('--folder', default='', help='Drive folder ID for uploads')
    parser.add_argument('--file', help='Local file path (for upload or verify)')
    parser.add_argument('--id', dest='file_id', help='Drive file ID for verification')

    args = parser.parse_args()

    if args.create:
        name = create_random_file()
        print(f"✅ File created: {name}")

    elif args.upload:
        if not args.key or not args.file:
            parser.error('--upload requires --key <KEY_FILE> and --file <PATH>')
        upload_to_drive(args.key, args.folder, args.file)

    elif args.verify:
        if not args.key or not args.file_id or not args.file:
            parser.error('--verify requires --key <KEY_FILE>, --id <FILE_ID>, and --file <LOCAL_PATH>')
        verify_file(args.key, args.file_id, args.file)

if __name__ == '__main__':
    main()