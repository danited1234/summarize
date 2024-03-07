from .reading_pdf import readpdf
from transformers import pipeline


class summarize:
    """
    using transformers (bart-large-cnn) will summarize all the content
    """
    def __init__(self) -> None:
        pass
    @staticmethod
    def ai_summarize(filename):
        """
        
        """
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        page_contents = readpdf.read_pdf_contents(filename)
        chunk_size = 1024
        
        # Initialize summary_string outside the loop
        summary_string = ""

        # Split the input text into smaller chunks
        input_chunks = [page_contents[i:i+chunk_size] for i in range(0, len(page_contents), chunk_size)]
        for i, chunk in enumerate(input_chunks):
            summaries = summarizer(str(chunk), max_length=130, min_length=30, do_sample=False)
            summary_text = summaries[0]['summary_text']
            print(f"Reading Chunk {i}")
            
            # Append summary_text to summary_string
            summary_string += summary_text

        # Output the combined summarized text
        print(summary_string)

        # Write summary_string to a file
        with open("summary.txt", 'w') as f:
            f.write(summary_string)