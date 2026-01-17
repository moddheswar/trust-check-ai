# TRUST CHECK AI

## Project Overview
TRUST CHECK AI is a terminal-based Python program that classifies statements—usually terms & conditions, delivery policies, or service agreements—as SAFE or RISKY.  
It uses a Naive Bayes model built from scratch and can handle multiline paragraphs, providing an **overall classification**, a **confidence score**, and highlights **risky sentences** in the input.

---

## Features
- Naive Bayes classifier implemented from scratch  
- Text preprocessing: lowercase conversion, punctuation removal, and tokenization  
- Terminal interface with multiline input support  
- Paragraph-level analysis: overall SAFE/RISKY classification  
- Confidence score indicating the proportion of risky statements  
- Lists risky sentences within a paragraph for easy identification  
- Easily extendable to include bigram/trigram features or GUI

---

## Folder Structure
project_root/
│
├─ data/
│ └─ raw_statements.txt # Dataset of SAFE and RISKY statements
│
├─ utils/
│ └─ preprocessing.py # Text cleaning functions
│
├─ model/
│ └─ naive_bayes.py # Naive Bayes model class and training/prediction
│
├─ core/
└─ main.py # Terminal interface for paragraph input


---

## Setup & Installation
1. Clone the repository:
    git clone github.com/moddheswar/trust-check-ai

2. Navigate to the project folder:
    cd trust-check-ai

3. Run the program:
    python core/main.py


---

## Usage
1. Enter or paste your statement or paragraph (multiple lines allowed)  
2. End your input with `END` on a new line  
3. The program will output:  
   - **Overall classification:** SAFE or RISKY  
   - **Confidence level:** proportion of risky statements  
   - **List of risky sentences** (if any)  
4. Type `exit` to quit the program

---

## How It Works
1. Statements are preprocessed: lowercase, punctuation removed, tokenized  
2. The Naive Bayes classifier is trained on labeled SAFE and RISKY statements  
3. For a new paragraph, the program splits it into sentences and calculates probabilities for each sentence  
4. The overall classification is based on the number of risky sentences  
5. A confidence score is calculated as `risky_count / total_sentences`  
6. Risky sentences are highlighted for easy identification

---

## Potential Improvements
- Add more advanced **text tokenization** (handle abbreviations, punctuation properly)  
- Add **bigrams/trigrams** for more precise classification  
- Provide **detailed confidence for each sentence**  
- Integrate with a **GUI or web interface** for easier user experience  

---

## Author
- MODDHESWAR S P
