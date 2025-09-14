# Semantic Communication System (SemCom-Project)

## Project Vision & End Goal
You are building a complete **Semantic Communication System** that consists of both encoder and decoder components.  
The system aims to compress natural language into semantic representations (triples) for efficient communication, then reconstruct meaningful information at the receiver end.

**Aimed - System Architecture Overview:**

```
[USER INPUT]
"Einstein developed the theory of relativity"
        ↓
[TRIPLE EXTRACTION] ← Your current work
"Einstein|developed|theory of relativity"
        ↓
[SEMANTIC EMBEDDING] ← Next stage
[0.23, -0.45, 0.78, ..., 0.12] (128-dim vector)
        ↓
[VECTOR QUANTIZATION] ← Compression stage
[23, 156, 78, 12] (4 indices instead of 128 floats)
        ↓
[CHANNEL CODING] ← Error protection
[23, 156, 78, 12, 45, 67] (6 bits with redundancy)
        ↓
[TRANSMISSION] ← Over wireless channel
Radio waves/5G/WiFi
        ↓
[CHANNEL DECODING] ← Error correction
[23, 156, 78, 12] (recovered indices)
        ↓
[VECTOR DEQUANTIZATION] ← Decompression
[0.23, -0.45, 0.78, ..., 0.12] (restored vector)
        ↓
[SEMANTIC DECODING] ← Text reconstruction
"Einstein|developed|theory of relativity"
        ↓
[TRIPLE-TO-TEXT] ← Natural language generation
"Einstein developed the theory of relativity"
        ↓
[USER DISPLAY]
Received message

```


- **Current Focus:** Working on the **ENCODER** part (triple extraction stage) to convert natural language sentences into structured semantic triples.

---

## Project Structure & File Organization

**Local Laptop Directory Structure:**

```
SEMANTIC COMMS/
├─ .vscode/
├─ data/
│  ├─ processed/
│  └─ raw/
│     └─ sample-1.json
├─ results/
├─ docs/
├─ logs/
│  └─ logs.md
├─ model_extraction/                    # ← ENCODER STAGE
│  ├─ data/
│  │  └─ labeled_triples.json
│  ├─ scripts/
│  │  └─ run_inference.py
│  └─ trained/
│     └─ flan-t5-triple-extraction-final/
│        ├─ config.json
│        ├─ generation_config.json
│        ├─ model.safetensors
│        ├─ special_tokens_map.json
│        ├─ spiece.model
│        ├─ tokenizer_config.json
│        ├─ tokenizer.json
│        └─ training_args.bin
├─ reports/
├─ src/
│  ├─ decoding/                        # ← DECODER STAGE (Future work)
│  ├─ encoding/                        # ← ENCODER STAGE (Current work)
│  └─ extraction/
│     └─ extracting_entities.py
├─ utils/
├─ tests/
├─ .gitignore
├─ README.md
└─ requirements.txt
```

---

## Complete System Workflow

### Stage 1: ENCODER (Current Work - Triple Extraction)
- **Input:** Natural language sentences  
- **Process:** Extract semantic triples using fine-tuned Flan-T5  
- **Output:** Structured triples (`subject|relation|object`)  
- **Status:** ✅ Model trained, 🚨 Output quality issues  

### Stage 2: DECODER (Future Work - Text Reconstruction)
- **Input:** Semantic triples  
- **Process:** Reconstruct meaningful text from triples  
- **Output:** Natural language sentences  
- **Status:** ❌ Not started yet  


### Development Environment
```
transformers>=4.0
torch>=1.9
datasets
numpy
pandas
```

### Hardware
- **Training:** Google Colab (free tier)  
- **Development:** Local Windows laptop  
- **Inference:** CPU/GPU automatic detection  




