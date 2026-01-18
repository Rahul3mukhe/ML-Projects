# AI-Powered Network Anomaly Detection

This project implements a machine learning–based system to detect anomalous and malicious patterns in network traffic data. The goal is to classify normal and attack traffic accurately to support cybersecurity monitoring and analysis.

---

##  Project Overview
- Detects multiple types of network anomalies using supervised learning
- Handles multi-class classification of network traffic
- Evaluates model performance using accuracy, precision, recall, and confusion matrices

---

##  Dataset Description
- Total network flows: **56,661**
- Total features: **78**
- Traffic classes included:
  - BENIGN
  - DoS
  - PortScan
  - Bot
  - BruteForce
  - WebAttack
  - Infiltration

---

##  Methodology
1. Data loading and exploration  
2. Data preprocessing and feature analysis  
3. Train-test split for model evaluation  
4. Model training using ensemble-based classifiers  
5. Performance evaluation using standard classification metrics  

---

##  Models Used
- Gradient Boosting Classifier  
- XGBoost Classifier  

---

##  Model Performance (From Notebook Output)
- Test Accuracy: **0.9661**
- Precision: **0.9662**
- Recall: **0.9661**

Performance was further validated using confusion matrices and class-wise predictions.

---

##  Technologies Used
- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- XGBoost  
- Matplotlib / Seaborn  

---

##  How to Run
1. Clone the repository
2. Open the notebook `Network_anamoly_Detection.ipynb`
3. Run all cells sequentially

---

## 📎 Notebook Link
https://github.com/Rahul3mukhe/ML-Projects/blob/main/Network_anamoly_Detection.ipynb

---

##  Notes
All metrics and results reported in this project are directly taken from the notebook output cells.
