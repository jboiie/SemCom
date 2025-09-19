# model_extraction/scripts/run_inference.py
'''
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch

def load_model(model_path):
    model_path = "model_extraction/trained/flan-t5-triple-extraction-final"
    model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    return model, tokenizer

def infer(model, tokenizer, sentence, device="cpu", max_length=64):
    sentence = "Investigating the measures employed to ensure data integrity within blockchain-based e-voting systems."
    model.to(device)
    inputs = tokenizer(sentence, return_tensors="pt").to(device)
    outputs = model.generate(
        **inputs,
        max_length=max_length,
        num_beams=5,          # beam search for better quality
        temperature=1.0,      # default sampling temperature
        top_k=50,             # top-k sampling to limit tokens considered
        top_p=0.95,           # top-p(Nucleus) sampling threshold
        early_stopping=True
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


def main():
    # Path to your saved fine-tuned model directory
    model_path = "model_extraction/trained/flan-t5-triple-extraction-final"

    # Load model and tokenizer
    model, tokenizer = load_model(model_path)

    # Example input sentence
    sentence = "Investigating the measures employed to ensure data integrity within blockchain-based e-voting systems."

    # Detect GPU if available
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Using device: {device}")

    # Run inference
    result = infer(model, tokenizer, sentence, device=device)
    print("Input:", sentence)
    print("Extracted triple:", result)

if __name__ == "__main__":
    main()
