from summarization.research import get_reserch_papers
from summarization.summarization import summarize
import requests
if __name__=="__main__":
    file_path = fr"E:\code\research papers\downloads\proposalmethods.pdf"
    summarize.ai_summarize(file_path)
    # try:
    #     folder_path = fr"E:\code\research papers\downloads"
    #     query = "psychology research proposals"
    #     url = f"https://scholar.google.com.pk/scholar?q=filetype:pdf+{query}&hl=en&as_sdt=0&as_vis=1&oi=scholart"
    #     get_reserch_papers.get_pdf_links_from_google(10,folder_path,url)
    # except (requests.exceptions.SSLError,requests.exceptions.RequestException):
    #     print("An error occured but still continuing")
    #     pass


# from reading_pdf import *
# from research import *
# from transformers import pipeline


# if __name__ == "__main__":
#     summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
#     page_contents = read_pdf_contents()
#     chunk_size = 1024
    
#     # Initialize summary_string outside the loop
#     summary_string = ""

#     # Split the input text into smaller chunks
#     input_chunks = [page_contents[i:i+chunk_size] for i in range(0, len(page_contents), chunk_size)]
#     for i, chunk in enumerate(input_chunks):
#         summaries = summarizer(str(chunk), max_length=130, min_length=30, do_sample=False)
#         summary_text = summaries[0]['summary_text']
#         print(f"Reading Chunk {i}")
        
#         # Append summary_text to summary_string
#         summary_string += summary_text

#     # Output the combined summarized text
#     print(summary_string)

#     # Write summary_string to a file
#     with open("summary.txt", 'w') as f:
#         f.write(summary_string)


