from datasets import load_dataset
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string

def normalize(text, lemmatizer, stopwords, punctuation):
    tokens = []
    for token in word_tokenize(text):
        token = token.lower()
        token = lemmatizer.lemmatize(token)
        if token not in stopwords and token not in punctuation:
            tokens.append(token)
    return tokens

def create_token_column(df, lemmatizer, stopwords, punctuation):
    tokenizedText = []
    for article in df['article']:
        tokens = normalize(article, lemmatizer, stopwords, punctuation)
        tokenizedText.append(' '.join(tokens))
        
    df['tokens'] = tokenizedText

def main():
    
#    loading the dataset
    ds = load_dataset("ccdv/pubmed-summarization", "document")
    
#   dividing the dataset 
    df_train = pd.DataFrame(ds['train'])
    df_validation = pd.DataFrame(ds['validation'])
    df_test = pd.DataFrame(ds['test'])
    
#   replacing the white spaces with NaN and then dropping the NaN columns
    df_train.replace(r'^\s*$', float('NaN'), regex=True, inplace=True)
    df_train_cleaned = df_train.dropna(how='any')
    
#   declaring nltk variables which will be used to clean the articles in the dataset 
    lemmatizer  = WordNetLemmatizer()
    stopwords   = set(nltk.corpus.stopwords.words('english'))
    punctuation = string.punctuation
    
    test_df_train = df_train_cleaned.head(10)
    test_df_test = df_test.head(10)
    test_df_validation = df_validation.head(10)

    create_token_column(test_df_train, lemmatizer, stopwords, punctuation)
    create_token_column(test_df_test, lemmatizer, stopwords, punctuation)
    create_token_column(test_df_validation, lemmatizer, stopwords, punctuation)

    test_df_train.to_csv('/Users/rahimamunawar/Documents/GitHub/Kdd_internship/test_df_train.csv')
    test_df_test.to_csv('/Users/rahimamunawar/Documents/GitHub/Kdd_internship/test_df_test.csv')
    test_df_validation.to_csv('/Users/rahimamunawar/Documents/GitHub/Kdd_internship/test_df_validate.csv')

    
if __name__ == "__main__":
    main()