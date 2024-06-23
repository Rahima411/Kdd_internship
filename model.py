import google.generativeai as genai
import os
import PyPDF2

# Setting the API Key 
genai.configure(api_key=os.environ["API_KEY"])

# Loading the Gemini Model for which will then be used for summarisation
model = genai.GenerativeModel('gemini-pro')

# A function which extracts text from the pdf files using PyPDF2
def extract_text_from_pdf(pdf_path):
    pdf_file = open(pdf_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    for page_num in range(len(pdf_reader.pages)):
      page_text = pdf_reader.pages[page_num].extract_text().lower()
      text = ""
      page = pdf_reader.pages[page_num]
      text += page.extract_text()
    return text

# A function which summarises the text extracted using GenAI 
def summarize_text(text):
    # Use the appropriate method to generate a summary
    response = model.generate_content([
    "Summarize This: ", text])

    return response.text  # Adjust to the correct field from the response

# Testing the functions
pdf_path = '/Users/rahimamunawar/Downloads/article.pdf'
pdf_text = extract_text_from_pdf(pdf_path)
summary = summarize_text(pdf_text)
print(summary)