
import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Hugging Face Pipelines", page_icon="🤖")

st.title("🤖 Hugging Face Pipelines")


task = st.selectbox(
    "Choose an NLP Task",
    [
        "Summarization",
        "Translation",
        "Sentiment Analysis",
        "Question Answering"
    ]
)

@st.cache_resource
def load_model(task_name):
    if task_name == "Summarization":
        return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    elif task_name == "Translation":
        return pipeline("translation_en_to_fr", model="Helsinki-NLP/opus-mt-en-fr")
    elif task_name == "Sentiment Analysis":
        return pipeline(
            "sentiment-analysis",
            model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
        )
    else:
        return pipeline(
            "question-answering",
            model="distilbert/distilbert-base-cased-distilled-squad"
        )

if task == "Summarization":
    text = st.text_area("Enter a long paragraph")

    if st.button("Summarize"):
        if text.strip():
            with st.spinner("Loading model and summarizing..."):
                model = load_model(task)
                result = model(
                    text,
                    max_length=100,
                    min_length=20,
                    do_sample=False
                )
            st.subheader("Summary")
            st.write(result[0]["summary_text"])
        else:
            st.warning("Please enter a paragraph.")

elif task == "Translation":
    text = st.text_area("Enter English text to translate into French")

    if st.button("Translate"):
        if text.strip():
            with st.spinner("Translating..."):
                model = load_model(task)
                result = model(text)
            st.subheader("French Translation")
            st.write(result[0]["translation_text"])
        else:
            st.warning("Please enter some text.")

elif task == "Sentiment Analysis":
    text = st.text_area("Enter a sentence or review")

    if st.button("Analyze Sentiment"):
        if text.strip():
            with st.spinner("Analyzing sentiment..."):
                model = load_model(task)
                result = model(text)
            st.subheader("Sentiment Result")
            st.write("Sentiment:", result[0]["label"])
            st.write("Confidence:", round(result[0]["score"] * 100, 2), "%")
        else:
            st.warning("Please enter some text.")

else:
    context = st.text_area("Enter the passage", height=150)
    question = st.text_input("Enter your question")

    if st.button("Get Answer"):
        if context.strip() and question.strip():
            with st.spinner("Finding the answer..."):
                model = load_model(task)
                result = model(question=question, context=context)
            st.subheader("Answer")
            st.write(result["answer"])
            st.write("Confidence:", round(result["score"] * 100, 2), "%")
        else:
            st.warning("Please enter both the passage and question.")
