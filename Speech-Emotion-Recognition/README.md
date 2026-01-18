# Speech Emotion Recognition using LSTM

This project is focused on building a deep learning model that can recognize human emotions from speech audio clips using **Long Short-Term Memory (LSTM)** networks and **Mel-Frequency Cepstral Coefficients (MFCCs)**. The goal is to classify speech signals into seven emotional categories based on the Toronto Emotional Speech Set (TESS) dataset.

---

## Dataset

**Dataset Used:** [Toronto Emotional Speech Set (TESS)]  
- Source:https://www.kaggle.com/datasets/ejlok1/toronto-emotional-speech-set-tess
- Contains **2800 audio recordings** spoken by two actresses (aged 26 and 64), each uttering 200 target words in 7 emotional categories:
  - **Angry**, **Disgust**, **Fear**, **Happy**, **Pleasant Surprise**, **Neutral**, **Sad**

---

## Objective

Develop a neural network model capable of:
- Extracting relevant acoustic features from speech signals.
- Learning temporal emotion patterns using LSTM.
- Accurately classifying spoken audio into one of seven predefined emotional states.

---

##  Features & Techniques

- **MFCC (Mel-Frequency Cepstral Coefficients)** for feature extraction (40 coefficients)
- **Spectral features**: Centroid and bandwidth (for extended analysis)
- **Label encoding** and one-hot transformation
- **LSTM-based deep neural network** with fully connected dense layers
- **Dropout regularization** to prevent overfitting
- **Categorical crossentropy** loss with **Adam optimizer**

---

##  Model Architecture

Input Layer (40 MFCCs, reshaped to 40×1)
→ LSTM Layer (256 units)
→ Dropout (0.2)
→ Dense (128, ReLU)
→ Dropout (0.2)
→ Dense (64, ReLU)
→ Dropout (0.2)
→ Dense (7, Softmax)

---

## Performance
Training Accuracy: ~85%.

Validation Accuracy: ~80.7%.

Trained over 50 epochs using an 80-20 train-test split.

---

## Results Visualization
Accuracy vs Epochs plot.

Validation vs Training curve.

Sample audio playback and emotion prediction.
