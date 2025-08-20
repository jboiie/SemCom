import json
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Initialize tokenizer and model before using them
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")

def extract_entities(text):
    prompt = f"Extract triples from the sentence in the format: subject|predicate|object."
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    outputs = model.generate(**inputs)
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return result

with open('data/raw/sample-1.json', 'r') as f:  # Adjust path if needed
    data = json.load(f)

for item in data:
    sentence = item["text"]
    entities = extract_entities(sentence)
    print(f"Sentence: {sentence}")
    print(f"Entities extracted by Flan-T5-base: {entities}")
    print("-" * 50)
