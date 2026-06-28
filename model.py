from transformers import pipeline

classifier = pipeline("sentiment-analysis")

def predict(text):
    result = classifier(text)
    return result