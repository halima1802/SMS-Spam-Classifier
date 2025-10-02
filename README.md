# SMS_Spam_Classification

The **SMS Spam Classification** project is a machine learning pipeline built to classify SMS messages as either **Spam** or **Ham (Non-Spam)**. It leverages **TF-IDF vectorization** for text representation and the **Multinomial Naive Bayes algorithm** for classification.

This project uses the [SMS Spam Collection Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset), which contains a collection of labeled SMS messages for supervised learning.

---

## Features

* 📊 **Data Cleaning** – Handles missing values, duplicates, and inconsistencies in the dataset.
* 🔎 **Exploratory Data Analysis (EDA)** – Visualizes class distribution, common words, and message patterns.
* 📝 **Text Preprocessing** – Includes lowercasing, tokenization, stopword removal, punctuation cleaning, and stemming/lemmatization.
* 🧮 **Model Building** – Transforms SMS text into TF-IDF vectors and applies Multinomial Naive Bayes classification.
* ✅ **Evaluation Metrics** – Accuracy, Precision, and Confusion Matrix are used to measure model performance.

---

## Project Workflow

1. **Dataset Loading**

   * Dataset sourced from Kaggle’s [SMS Spam Collection Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset).

2. **Data Cleaning**

   * Remove duplicates and handle missing values.

3. **Exploratory Data Analysis (EDA)**

   * Analyze spam vs. ham distribution.
   * Visualize frequent words in both classes.

4. **Text Preprocessing**

   * Convert text to lowercase.
   * Tokenize sentences.
   * Remove punctuation, special characters, and stopwords.
   * Apply stemming or lemmatization.

5. **Model Building**

   * Vectorize cleaned text using **TF-IDF**.
   * Train a **Multinomial Naive Bayes** classifier.

6. **Evaluation**

   * Test performance using Accuracy, Precision, and Confusion Matrix.
   * Assess improvements if required.

---

## Installation and Local Setup

### Clone the repository

```bash
git clone https://github.com/YourUsername/SMS_Spam_Classification.git
```

### Install Dependencies

It’s recommended to create a virtual environment before installing packages.

```bash
pip install -r requirements.txt
```

### Run the Project

Execute the main script to train and evaluate the model:

```bash
python sms_spam_classifier.py
```

---

## Example Usage

* Input: `"Congratulations! You've won a free ticket. Call now!"`

* Output: **Spam**

* Input: `"Hey, are we still meeting tomorrow at 5?"`

* Output: **Ham**

---

## Tech Stack

* **Language:** Python
* **Libraries:** Pandas, NumPy, Matplotlib, Scikit-learn, NLTK
* **Model:** Multinomial Naive Bayes
* **Vectorization:** TF-IDF

