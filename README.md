# DevelopersHub-Task-News-Topic-Classifier-Using-BERT-
To fine-tune a transformer-based model for multi-class text classification and deploy it for real-time news topic prediction.
📊 Dataset

AG News

Contains 3 news categories:

World

Sports

Sci/Tech

Source: Hugging Face Datasets Library

⚙️ Methodology
1️⃣ Data Preprocessing

Tokenization using Hugging Face tokenizer

Padding and truncation

Train-test split

Label encoding

2️⃣ Model Fine-Tuning

Pretrained model: BERT

Framework: Hugging Face Transformers

Optimizer: AdamW

Cross-Entropy Loss for multi-class classification

3️⃣ Model Evaluation

Accuracy

F1-Score (Macro & Weighted)

Confusion Matrix (optional)

🚀 Deployment

The trained model is deployed using:

Streamlit (or)

Users can enter a news headline and instantly receive a predicted topic category.

🛠 Tech Stack

Python

PyTorch

Hugging Face Transformers

Datasets Library

Streamlit

Scikit-learn

📈 Skills Demonstrated

Natural Language Processing (NLP)

Transformer-based architectures

Transfer Learning & Fine-Tuning

Text Classification

Model Evaluation Metrics

Lightweight Model Deployment

📌 Results

The fine-tuned BERT model achieves strong classification performance on the AG News dataset with competitive Accuracy and F1-score, demonstrating the effectiveness of transformer-based transfer learning for text classification tasks.
