# PubMed Article Summarizer

This project is a web application that allows users to upload PubMed articles and get summarized versions of the text. The application is developed using Streamlit and integrates Google's Gemini Generative AI model for text summarization. This README file provides detailed instructions on setting up and using the application.

### Features
- Upload papers from PubMed in TXT, DOCX, or PDF formats.
- Preprocess and clean up the text in the uploaded files.
- Use Google's Gemini Generative AI model to summarise the text.
- Display the material in its original and summarised versions on the web page. 
- The option of summary length and style.

### Setup Instructions

Follow these steps to set up the application on your local machine.

#### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)
- API key for Google's Generative AI model (Gemini)


### Installation

1. Clone the Respository

   ```
   git clone https://github.com/Rahima411/Kdd_internship.git
   cd Kdd_internship
   ```

2. Set up the environment variable for the API key:

   ```
   export API_KEY='your_google_api_key'
   ```

3. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

### Usage

1. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```
2. To utilise the application, use your web browser and navigate to http://localhost:8501

3. Upload a TXT, DOCX, or PDF file of a PubMed article.

4. Select the length and summary style.

5. To generate and read the summary, click the "Summarise" button.

### Data Preparation

The dataset for this project is Hugging Face's PubMed Summarization dataset. Data preparation comprises the following:

- Loading the data.
- Cleaning and preparing the text.
- Normalising and tokenising the text.
- These tasks are handled by the Python script data_preparation.py.

### Model Integration

The summary is done with Google's Gemini Generative AI model. The model.py script can handle:

- PyPDF2 extracts text from PDF files.
- Text summarization using the Gemini model.
- The model is integrated into the Streamlit application.


### Web Application Development

The web application was made with Streamlit. The streamlit_app.py script includes the following:

- File uploading and text extraction.
- Text cleanup and preprocessing.
- Integration of the Gemini model for summarization using the summarize_text from model.py 
- The user can choose the summary style and length.
- The web interface displays both the original and the summarised text.

### License
This project is licensed under the Apache License Version 2.0. See the LICENSE file for details.




