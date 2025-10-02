# SMS_Spam_Classification
Dataset from : https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset 
This repository contains the code for an SMS Spam Classification project. The goal of this project is to classify SMS messages into spam or non-spam (ham) using TF-IDF vectorization and the Multinomial Naive Bayes algorithm. The project follows the following steps:

1. Data Cleaning
The dataset used in this project is cleaned to handle any missing values, duplicates, or inconsistencies. Cleaning ensures that the data is ready for exploration and preprocessing.

2. EDA (Exploratory Data Analysis)
Exploratory Data Analysis is performed to gain insights into the dataset. Visualization techniques are used to understand the distribution of spam and non-spam messages, the most common words, and other patterns in the data.

3. Text Preprocessing
Text preprocessing involves cleaning and transforming the raw SMS messages into a format suitable for machine learning. This includes:

-Converting text to lowercase
-Tokenization
-Removing special characters, punctuation, and stop words
-Stemming or Lemmatization

4. Model Building
TF-IDF (Term Frequency-Inverse Document Frequency) vectorization is applied to convert the processed text data into numerical vectors. Then, a Multinomial Naive Bayes classifier is trained on the TF-IDF vectors to classify SMS messages into spam or non-spam.

5. Evaluation
The model's performance is evaluated using metrics such as accuracy, precision and confusion matrix. Evaluation helps in understanding how well the model is performing and if any improvements are needed.
