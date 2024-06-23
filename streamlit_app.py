import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import docx2txt 
#from  PyPDF2  import PdfFileReader
import pdfplumber


# def read_pdf(data):
#     pdfReader = PdfFileReader(data)
#     count = PdfFileReader.numPages
#     all_pages_text = ""
#     for i in range(count):
#         page  = pdfReader.getPage(i)
#         all_pages_text += page.extractText()
#     return all_pages_text

#-------------------------------- main function --------------------------------
def main (): # main funtion 
    st.set_page_config(page_title = "Summarize", page_icon=":tada:",layout = "wide") # set the title to summarize and the layout to wide

    st.subheader("Rahima Munawar :wave:") # a display message 

    st.title("Upload a file")
    file = st.file_uploader("Upload a txt , pdf  or a word file", type =["pdf", "docx","txt"])
  
   
    if file is not None:
        #st.write(dir(text_file))
        #  a download button to download the original file 
        st.download_button(
            label="Download File",
            data= file,
            file_name=file.name
        )

        #------------------------------------ displaying the original file-------------------------------
        # if its a text file , 
        if file.type == "text/plain":
            # st.write(file.read()) # works in bytes 
            raw_text = str(file.read(),"utf-8")
            st.write(raw_text)

        # application or pdf 
        if file.type == "application/pdf":
            try:
                with pdfplumber.open(file) as pdf:
                    text = ""
                    for page in pdf.pages:
                        text += page.extract_text() + "\n"
                    st.write("File Contents\n", text, height=300)
            except Exception as e:
                st.error(f"Error reading PDF file: {e}")
        # reading if the file is a docx       
        elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            raw_test = docx2txt.process(file)
            st.write(raw_test)
        

if __name__ == "__main__":
    main()
