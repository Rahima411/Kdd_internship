import google.generativeai as genai
import os
import PyPDF2

# setting the API Key 
genai.configure(api_key=os.environ["API_KEY"])

# loading the Gemini Model which will then be used for summarisation
model = genai.GenerativeModel('gemini-pro')

# A function which extracts text from the pdf files using PyPDF2
def extract_text_from_pdf(pdf_path):
    pdf_file = open(pdf_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    for page_num in range(len(pdf_reader.pages)):
      text = ""
      page = pdf_reader.pages[page_num]
      text += page.extract_text()
    return text.lower()

# A function which summarises the text extracted using GenAI 
def summarize_text(text, style = None, length = None):
   
    prompt = 'Summarize this text: '

    if style is not None and length is not None:
       prompt = f'Write a {length} {length} summary of: '
       
    response = model.generate_content([
    prompt, text])

    return response.text  

# testing the functions
# change the path before runing this on your local machine
pdf_path = '/Users/rahimamunawar/Downloads/article.pdf'
pdf_text = extract_text_from_pdf(pdf_path)
summary = summarize_text(pdf_text)
# print(summary)