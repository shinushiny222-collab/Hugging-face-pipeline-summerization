# Hugging-face-pipeline-summerization

## Project Overview

Hugging Face Pipelines is a Natural Language Processing (NLP) application built using Python, Streamlit, and Hugging Face Transformers.

This application allows users to perform different NLP tasks through a simple and interactive web interface. It uses pre-trained transformer models to process text and generate results.

## Features

This application supports four NLP tasks:

### 1. Text Summarization

* Accepts a long paragraph as input.
* Generates a shorter summary of the given text.
* Uses the `sshleifer/distilbart-cnn-12-6` model.

### 2. English to French Translation

* Accepts English text as input.
* Translates the text into French.
* Uses the `Helsinki-NLP/opus-mt-en-fr` model.

### 3. Sentiment Analysis

* Analyzes sentences, reviews, or other text.
* Identifies the sentiment as POSITIVE or NEGATIVE.
* Displays the prediction confidence percentage.
* Uses the `distilbert/distilbert-base-uncased-finetuned-sst-2-english` model.

### 4. Question Answering

* Accepts a passage and a question from the user.
* Extracts an answer based on the provided passage.
* Displays the answer and prediction confidence.
* Uses the `distilbert/distilbert-base-cased-distilled-squad` model.

## Technologies Used

* Python
* Streamlit
* Hugging Face Transformers
* PyTorch
* Pre-trained NLP Models

## Project Structure

```text
Hugging-Face-Pipelines/
│
├── app.py
├── requirements.txt
└── README.md
```

## Installation and Setup

### Step 1: Clone the Repository

```bash
git clone <your-github-repository-url>
```

Navigate to the project directory:

```bash
cd Hugging-Face-Pipelines
```

Replace `<your-github-repository-url>` with your actual GitHub repository URL.

### Step 2: Install Dependencies

Install the required Python libraries:

```bash
pip install streamlit transformers torch sentencepiece
```

The `sentencepiece` package supports tokenization required by some translation models.

### Step 3: Run the Application

Run the following command in your terminal:

```bash
streamlit run app.py
```

The application will open in your default web browser.

If it does not open automatically, use the local URL displayed in your terminal.

## Requirements

The project requires:

* Python 3.10 or a compatible Python version
* Streamlit
* Transformers
* PyTorch
* SentencePiece

The pre-trained models are downloaded automatically from Hugging Face when they are first loaded. An internet connection is required for the initial model download.

Model loading may take some time depending on your internet speed and system resources.

## How to Use

1. Start the Streamlit application.
2. Select an NLP task from the dropdown menu.
3. Enter the required text.
4. Click the corresponding action button.
5. View the generated output.

For Question Answering, enter both a passage and a question before clicking the button.

## Implementation Details

The application uses the Hugging Face `pipeline()` function to simplify NLP model loading and inference.

The `@st.cache_resource` decorator caches loaded models so they can be reused instead of being loaded again unnecessarily.

A loading indicator is displayed while models process the input. Input validation ensures that users provide the required text before submitting a request.

## Applications

* Automatic text summarization
* Language translation
* Customer review analysis
* Sentiment classification
* Reading comprehension
* Extractive question answering

## Future Enhancements

* Support for additional languages.
* Summarization for uploaded documents.
* Sentiment analysis for multiple reviews.
* Support for PDF and text file uploads.
* Improved interface and output visualization.
* Additional NLP tasks using Hugging Face models.

## Conclusion

The Hugging Face Pipelines project demonstrates how pre-trained transformer models can be integrated into a Streamlit application to perform multiple Natural Language Processing tasks.

It provides a simple way to explore text summarization, translation, sentiment analysis, and question answering through an interactive interface.

## Author

**Aseniya Shiny A**

B.Sc. Computer Science with Artificial Intelligence

