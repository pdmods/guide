import os
import requests
from urllib.parse import urljoin, urlparse

def download_file(url, output_dir):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        parsed_url = urlparse(url)
        file_path = os.path.join(output_dir, parsed_url.path.lstrip("/"))
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Downloaded: {file_path}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

def download_from_structure(file_path, domain, output_dir):
    try:
        with open(file_path, 'r') as f:
            for line in f:
                relative_path = line.strip().lstrip("/")
                if relative_path:
                    url = urljoin(domain, relative_path)
                    download_file(url, output_dir)
    except Exception as e:
        print(f"Error reading folder structure: {e}")

if __name__ == "__main__":
    domain = input("Enter the domain (e.g., https://example.com): ").strip()
    script_dir = os.getcwd()
    folder_structure_file = os.path.join(script_dir, "folder_structure.txt")
    output_dir = os.path.join(script_dir, "base")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if os.path.exists(folder_structure_file):
        download_from_structure(folder_structure_file, domain, output_dir)
    else:
        print(f"File {folder_structure_file} does not exist.")
