import PyPDF2
import re


class readpdf:
    def __init__(self) -> None:
        pass
    @staticmethod
    def read_pdf_contents(filename:str):
        text = ''
        pdf_reader = PyPDF2.PdfReader(filename)
        
        pages = pdf_reader.numPages
        for x in range(0, int(pages)):
            pageObj = pdf_reader.getPage(x)
            extract_text = pageObj.extractText()
            text = text + extract_text
        result_string = re.sub(r'\n', ' ', text)
        return result_string


