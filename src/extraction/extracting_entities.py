import json
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")

def extract_triples(text):
    prompt = ( f"Extract subject|action|object triples from the sentence. Format as subject|action|object. Sentence: {text} Output:")
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
    outputs = model.generate(
        **inputs,
        max_length=100,
        num_beams=5,
        no_repeat_ngram_size=2,
        early_stopping=True
    )
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return result

# Load input data
with open('data/raw/sample-1.json', 'r') as f:
    data = json.load(f)

# Extract triples and print results
for item in data:
    sentence = item["text"]
    triples = extract_triples(sentence)
    print(f"Sentence: {sentence}")
    print(f"Extracted triples: {triples}")
    print("-" * 50)
