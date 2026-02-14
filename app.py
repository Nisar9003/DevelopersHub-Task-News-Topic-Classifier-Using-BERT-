import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

MODEL_PATH = "ag_news_model"

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)

labels = {
    0: "World",
    1: "Sports",
    2: "Business",
    3: "Sci/Tech"
}

st.title("AG News Classification")

text = st.text_area("Enter news text")

if st.button("Predict"):
    if text.strip() == "":
        st.warning("Please enter some text")
    else:
        inputs = tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=512
        )

        with torch.no_grad():
            outputs = model(**inputs)

        pred = torch.argmax(outputs.logits, dim=1).item()
        st.success(f"Prediction: {labels[pred]}")
