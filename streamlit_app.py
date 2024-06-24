import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import docx2txt 
import pdfplumber
import re
from model import summarize_text

#----------------a funnction to clean up the text extracted from the files---------
def clean_text(text):

    # removing multiple new line characters if found in the file
    text = re.sub(r'\n+', '\n', text).strip()

    # replacing multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text)  
    
    # removing non-ASCII characters if they are found 
    text = re.sub(r'[^\x00-\x7F]+', ' ', text) 
    
    # removing hyperlinks if they are found 
    text = re.sub(r'http\S+', '', text)

    # removing weblinks if they are found
    text = re.sub(r'www.\S+', '', text)
    
    return text.lower().strip() 

#-------------------------------- main function -----------------------------------
def main (): # main funtion 
    st.set_page_config(page_title="PubMed Summariser", page_icon=":tada:", layout="wide")   
    
    # CSS for styling of the webpage
    st.markdown(
        """
        <style>
            .main-header {
                text-align: center; 
                margin-bottom: 30px;
            }
            .main-header h1 {
                color: #3498db;
                font-size: 3em;
                margin: 0;
            }
            .main-header p {
                font-size: 1.2em;
                color: #7f8c8d;
            }
            .upload-area {
                display: flex; 
                justify-content: center; 
                align-items: left; 
                flex-direction: column;
                margin-bottom: 0px;
            }
            .upload-area label {
                font-size: 1.8em;
                color: #ffffff;
                font-weight: bold;
                margin-bottom: 0px;
            }
            .file-content, .summary-content {
                border: 1px solid #bdc3c7; 
                padding: 20px; 
                border-radius: 5px; 
                background-color: #ecf0f1;
                margin-bottom: 30px;
            }
        </style>
        """,
        unsafe_allow_html=True
    ) 

    # Center-aligned header
    st.markdown(
        """
        <div class='main-header'>
            <h1>PUBMED SUMMARISER</h1>
            <p>Upload a file and get a summarized version</p>
        </div>
        """,
        unsafe_allow_html=True
    ) 

    # file is used to store the uploaded file, and is used for summarization.
    st.markdown(
        """
        <div class='upload-area'>
            <label for='fileUploader'>Upload a file</label>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    file = st.file_uploader("", type=["pdf", "docx", "txt"], key="fileUploader", help="Upload a TXT, PDF, or Word file (max size: 200MB)", label_visibility="collapsed")
    
   
    if file is not None:
        #  a download button to download the original file 
        st.download_button(
            label="Download File",
            data= file,
            file_name=file.name,
            mime=file.type
        )

        #-------------------------------Displaying the original file-------------------------------
        #  processing the data according to the data type in order to display.
        # if its a text file , raw_text is a variable used to process the file 

        st.markdown("### Original File Content")
        content_area = st.empty()
        content_area.markdown("<div class='file-content'></div>", unsafe_allow_html=True)
        
        if file.type == "text/plain":
            raw_text = str(file.read(), "utf-8")
            cleaned_text = clean_text(raw_text)
            content_area.text_area('', cleaned_text, height=300, key="raw_text")

        # if its a pdf file , text is a variable used to process the file 
        elif file.type == "application/pdf":
            try:
                with pdfplumber.open(file) as pdf:
                    text = ""
                    for page in pdf.pages:
                        text += page.extract_text().lower() + "\n"
                    cleaned_text = clean_text(text)
                    content_area.text_area('', cleaned_text, height=300, key="pdf_text")
            except Exception as e:
                st.error(f"Error reading PDF file: {e}")

        # if its a docx file , raw_text is a variable used to process the file
        elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            raw_text = docx2txt.process(file)
            cleaned_text = clean_text(raw_text)
            content_area.text_area('', cleaned_text, height=300, key="docx_text")


        #--------------------------Providing the user with summary options------------------------------ 
        st.markdown("### Summary Options")
    
        # summary style is a variable used to save the style type selected by the user
        # summary length is a variable used to save the length selected by the user
        summary_style = st.selectbox("Select Summary Style", ["Narrative", "Expository", "Argumentative", "Descriptive"])
        summary_length = st.radio("Select Summary Length", ["Brief", "Detailed"])

        #--------------------------Summarising and Displaying the Generated Text------------------------
        if st.button("Summarize"):

            st.markdown("### Summary")
            summary_area = st.empty()
            summary_area.markdown("<div class='summary-content'></div>", unsafe_allow_html=True)

            if file.type == "text/plain":
                summary = summarize_text(raw_text, summary_style, summary_length)

            elif file.type == "application/pdf":
                summary = summarize_text(text, summary_style, summary_length)

            elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                summary = summarize_text(raw_text, summary_style, summary_length)

            summary_area.text_area('',summary, height=300, key="summary")

            

if __name__ == "__main__":
    main()
