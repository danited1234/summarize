from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os

class selenium_headless:
    """Class That Intilizas Selenium
    #### Argument
        * `folder_path` ( str ) add folder path where you want the user to files to download
    """


    def __init__(self,folder_path:str) -> None:
        self.folder_path = folder_path
        chrome_options = Options()
        chrome_options.add_experimental_option('prefs', {
"download.default_directory":f"{self.folder_path}", #Change default directory for downloads
"download.prompt_for_download": False, #To auto download the file
"download.directory_upgrade": True,
"plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
})
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)


    def get_pdfs(self,max_files_to_write:int,url:str):
        """Main object that downloads all the pdf files from the web
        #### Arugments
            * `max_files_to_write` ( int ) Number of file that the user wants to download
            * `url` ( str ) takes an argument of url from where the pdfs will be downloaded
        """
        file_counter = 0
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

        self.driver.get(url)
        source_code = self.driver.page_source
        soup = BeautifulSoup(source_code,'html.parser')
        pdf_links = []
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and href.endswith('.pdf'):
                pdf_links.append(href)
        for link in pdf_links:
            filename =link.split('/')[-1]
            self.driver.get(link)
            print(f"Downloading {filename}")
            file_counter += 1  # Increment the file counter
                
                # Check if the maximum number of files to write has been reached
            if file_counter >= max_files_to_write:
                print(f"Maximum number of files ({max_files_to_write}) reached. Stopping further downloads.")
                break  

