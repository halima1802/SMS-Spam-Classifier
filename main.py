import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


nltk.download('punkt')
nltk.download('stopwords')
nltk.download('words')


def preprocess_data(message):
    # Converting Data to Lower Case
    message = message.lower()

    # Tokenization
    message = nltk.word_tokenize(message)
    #message = tokenizer.tokenize(message)

    y = []
    # Removing Special Characters,Stop Words and Punctuation Marks
    for i in message:
        if i.isalnum() and i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    message = y[:]
    y.clear()

    # Stemming
    ps = PorterStemmer()
    for i in message:
        y.append(ps.stem(i))

    return " ".join(y)


st.title("SMS Spam Classifier")
input_sms = st.text_input("Enter message to be classified as Spam or Not Spam:")
if st.button('Predict'):
    # Preprocessing the data using the function preprocess_data
    transformed_message = preprocess_data(input_sms)
    # Vectorize the input using tfidf
    vector_input = tfidf.transform([transformed_message])
    # Predict the result using the model
    result = model.predict(vector_input)[0]
    # Display the Result
    if result == 1:
        st.header("Message is Spam!")
    else:
        st.header("Message is Not Spam!")
