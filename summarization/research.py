import requests
from bs4 import BeautifulSoup
import os 

class get_reserch_papers:
    """
    No Instance of a class
    #### One Object Static
        * `get_pdf_links_from_google`
    """

    def __init__(self) -> None:
        pass


    @staticmethod
    def get_pdf_links_from_google(max_files_to_write:int,folder_path:str,url:str) -> None:
        """function that downloads files from google and google scholar
        #### Arguments
            * `max_files_to_write` ( int ) number of files the user wants to download
            * `folder_path` ( str ) folder path where the user wants to save these downloaded pdfs
            * `url` ( str ) google scholar and google url will be passed here
        """

        max_files_to_write = 10  # Set the maximum number of files to write
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Format the Google search query
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for unsuccessful HTTP requests

        # Parse the HTML content of the response
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract PDF links from the search results
        
        pdf_links = []
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and href.endswith('.pdf'):
                pdf_links.append(href)
        file_counter = 0  # Initialize the file counter
        for link in pdf_links:
            filename = os.path.basename(link)
            valid_filename = ''.join(char for char in filename if char.isalnum() or char in ('_', '.', '-'))
            file_path = os.path.join(folder_path, valid_filename)
            response = requests.get(link, headers=headers)
            if response.status_code != 200:
                print(f"Unable To Download File {filename}\n{link}")
            else:
                with open(file_path, 'wb') as f:
                    print(f"Writing File {valid_filename}")
                    f.write(response.content)
                    file_counter += 1  # Increment the file counter
                    
                    # Check if the maximum number of files to write has been reached
                    if file_counter >= max_files_to_write:
                        print(f"Maximum number of files ({max_files_to_write}) reached. Stopping further downloads.")
                        break  # break the loop once the max number of pdf files is reached



# def main():
#     query = input("Enter your Query: ")
#     folder_name = input ("Enter Folder Name To Save PDFs To: ")
#     max_file_number = input("Enter the Number of Research pdfs that you want to download: ")
#     query = '+'.join(query.split())
#     proxy_list = proxies.get_proxies()

#     try:
#         url = f"https://scholar.google.com.pk/scholar?q=filetype:pdf+{query}&hl=en&as_sdt=0&as_vis=1&oi=scholart"
#         get_pdf_links_from_google(int(max_file_number),folder_name,url,proxy_list)
#         for i in range(1,11):
#             url = f"https://scholar.google.com.pk/scholar?start=10&q=filetype:pdf+{query}&hl=en&as_sdt=0,5&as_vis={i}"
#             get_pdf_links_from_google(int(max_file_number),folder_name,url,proxy_list)
#         url = f"https://www.google.com/search?q=filetype:pdf+{query}&num=100"
#         get_pdf_links_from_google(int(max_file_number),folder_name,url,proxy_list)
#     except requests.exceptions.SSLError as e:
#         print(f"An error occured\n{e}")
#         pass
#     except requests.exceptions.RequestException as e:
#         print(f"An error occured\n{e}")
#         pass
# if __name__=="__main__":
#     main()