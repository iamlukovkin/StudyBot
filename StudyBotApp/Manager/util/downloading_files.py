import os
import re
import requests
from doc2docx import convert
import config.settings as settings
from bs4 import BeautifulSoup


# исключенные названия файлов
excluded_files = ['vecherniki', 'zaochniki', '011']

def download_files(url: str, dst: str):
    """
    Downloads exams from https://rsreu.ru/

    Args:
        url (str): url of the file
        dst (str): destination path

    Returns:
        bool: True if files downloaded successfully.
    """  
    response: requests = requests.get(url)
    html: str = response.text
    soup: BeautifulSoup = BeautifulSoup(html, 'html.parser')
    tables: list[BeautifulSoup] = soup.find_all('table')
    captions: list[str] = [
        table.caption.text for table in tables if table.caption]
    folders: list[str] = []
    
    for caption in captions:
        
        table: BeautifulSoup = tables[captions.index(caption)]
        files: list[BeautifulSoup] = table.find_all(
            'a', href=re.compile('/component/docman/doc_download/'))
        caption: str = caption.replace('/', '_')
        folder_name: str = dst + caption.replace(' ', '_').lower()
        folder_name.replace('\xa0', '')
        folders.append(folder_name)
        
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
        
        span: str = str(files[0].find('span')).split('docman ')[1]
        span: str = span.split('"')[0]
        
        if span == 'xls': extension: str = '.xlsx'
        elif span == 'doc': extension: str = '.doc'
        else: extension: str = '.pdf'
        
        for file in files:
            
            filename: str = file.find_parent('td').find('a').text
            path: str = folder_name + '/' + filename + extension
            path: str = path.replace(" ", "")
            path: str = path.replace("\xa0", "")
            url = 'https://rsreu.ru' + file['href']
            response = requests.get(url)
            with open(path, 'wb') as f:
                f.write(response.content)
            
            if extension == '.doc':
                converted_path = folder_name + '/' + filename + '.docx'
                convert(path, converted_path)
                os.remove(path)
    
    return folders