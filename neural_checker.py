from transformers import pipeline

# Zero-shot classification for fact-checking
classifier = pipeline("zero-shot-classification")

def neural_fact_check(claim, labels=["true", "false"]):
    result = classifier(claim, labels)
    return result['labels'][0], result['scores'][0]
