# Semantic Communication System (SemCom-Project)

## Project Vision & End Goal
You are building a complete **Semantic Communication System** that consists of both encoder and decoder components.  
The system aims to compress natural language into semantic representations (triples) for efficient communication, then reconstruct meaningful information at the receiver end.

**System Architecture Overview:**

```
INPUT TEXT → [ENCODER: Triple Extraction] → SEMANTIC TRIPLES → [DECODER: Text Reconstruction] → OUTPUT TEXT
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

**Integration Goal:**  
- Encoder compresses sentences → triples (bandwidth efficient)  
- Decoder reconstructs triples → sentences (information recovery)  

---

## Current Progress Status

### ✅ ENCODER Stage - Completed
- **Dataset Preparation:** Created `labeled_triples.json` with sentence-to-triple mappings  
- **Environment Setup:** Google Colab with transformers library  
- **Model Selection:** `google/flan-t5-large` for sequence-to-sequence learning  
- **Data Preprocessing:** Tokenized dataset with proper input/label formatting  
- **Training Configuration:** `Seq2SeqTrainingArguments` setup  
- **Model Training:** Successfully completed fine-tuning (5 epochs, ~24 minutes)  
- **Model Saving:** Downloaded to local laptop  
- **Inference Setup:** Created `run_inference.py` script  

### 🔧 ENCODER Stage - Issues
- **Critical Problem:** Model outputs input repetition instead of structured triples  
  - Input: `"this table is green"`  
  - Expected: `"table|has color|green"`  
  - Actual: `"this table is green"`  
- **Likely Causes:**
  - Training data may have sentences in both text and triples fields  
  - Preprocessing function mapping errors  
  - Label formatting issues during tokenization  

### ❌ DECODER Stage - Not Started
- **Architecture Design:** Need to define decoder model approach  
- **Training Data:** Need triples-to-text datasets  
- **Model Selection:** Choose appropriate model for text generation from triples  
- **Integration:** Connect encoder-decoder pipeline  

---

## Technical Stack & Tools

### Current Implementation
- **Framework:** Hugging Face Transformers  
- **Base Model:** `google/flan-t5-large`  
- **Training:** `Seq2SeqTrainer` with `DataCollatorForSeq2Seq`  
- **Environment:** Google Colab → Local Windows laptop  
- **Language:** Python  
- **Version Control:** GitHub  

### Training Configuration
```python
training_args = Seq2SeqTrainingArguments(
    output_dir="./flan_t5_results",
    eval_steps=500,
    learning_rate=3e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    weight_decay=0.01,
    save_total_limit=3,
    num_train_epochs=5,
    predict_with_generate=True,
    logging_dir='./logs',
    logging_steps=10,
    save_strategy="epoch",
    report_to=["none"]
)
```

---

## GitHub Repository Status

### Current State
- **Training notebook:** ✅ Uploaded (metadata rendering issues on GitHub)  
- **Model files:** ❌ Excluded via `.gitignore` (too large for Git)  
- **Scripts:** ✅ Available locally  
- **Documentation:** 🔧 Needs completion  

### Repository Structure
- `src/encoding/` → Encoder components (current work)  
- `src/decoding/` → Decoder components (future work)  
- `src/extraction/` → Entity extraction utilities  
- `model_extraction/` → Current encoder model and training  

---

## Current Critical Issues

### 🚨 Encoder Model Performance
- **Problem:** Fine-tuned model repeating input instead of extracting triples  
- **Likely Causes:**  
  - Training data issues  
  - Preprocessing/label formatting errors  

### 🔧 Technical Challenges
- **Generation Parameters:** Flan-T5 doesn’t support sampling flags (`top_p`, `top_k`)  
- **Data Validation:** Need to verify training data quality  
- **Evaluation Metrics:** No automated assessment of triple extraction quality  

---

## Immediate Next Steps (Encoder Focus)

### Priority 1 - Fix Current Model
- 🔍 Inspect Training Data: Verify `labeled_triples.json` format  
- 🔧 Data Correction: Fix malformed triples  
- 🔄 Retrain Model: If data issues found  
- 🧪 Validation: Test with known good inputs  

### Priority 2 - Encoder Completion
- 📊 Evaluation Pipeline: Implement triple extraction metrics  
- 📝 Documentation: Complete encoder usage guide  
- 🔧 Optimization: Fine-tune generation parameters  
- 🧪 Testing: Comprehensive evaluation suite  

---

## Future Roadmap (Decoder Development)

### Stage 2 Planning
- **Architecture Research:** Survey triple-to-text generation approaches  
- **Data Preparation:** Create/find triples-to-sentence datasets  
- **Model Selection:** Choose decoder architecture (T5, GPT variants, etc.)  
- **Integration Design:** Plan encoder-decoder pipeline  

### System Integration
- **End-to-End Pipeline:** Connect encoder → decoder  
- **Performance Metrics:** Semantic fidelity, compression ratio  
- **Optimization:** Joint training or individual component tuning  
- **Deployment:** Production-ready semantic communication system  

---

## Key File Locations

### Current Encoder Files
- **Training Data:** `model_extraction/data/labeled_triples.json`  
- **Trained Model:** `model_extraction/trained/flan-t5-triple-extraction-final/`  
- **Inference Script:** `model_extraction/scripts/run_inference.py`  
- **Training Notebook:** On GitHub (with rendering issues)  

### Planned Decoder Files
- **Architecture:** `src/decoding/` (to be created)  
- **Training Data:** TBD  
- **Models:** TBD  

---

## System Requirements

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
