# WORD FOR THOUGHT
## BY~ Naina Bhalla (Roll number: 240674)

## Overview
The project processes audio data from two datasets: CREMA-D & Ravdess in form of .wav using the librosa library. It extracts various features such as Mel-Spectrograms, MFCC, ZCR and RMS energy. Based on these features, it trains a CNN model to detect emotions.

## Dataset Overview
The CREMA-D dataset contains 7,442 original audio clips from 91 actors. Actors spoke from a selection of 12 sentences. The sentences were presented using one of six different emotions (Anger, Disgust, Fear, Happy, Neutral, and Sad).
The Ravdess dataset contains 1440 audio files from 24 actors. Their sentences were presented using one of eight different emotions (Anger, Disgust, Fear, Happy, Neutral, Surprise, Calm, and Sad).
In the final dataset used for training, I have dropped the Surprise and the Calm emotions since very few audio files were available in comparison.
<br>![Screenshot (209)](https://github.com/user-attachments/assets/2b3ce5ab-0168-482c-9a72-ce91c7988d4a)


## Audio Features
Each audio contains various features.

**Waveform of audios**:
<br>![Screenshot (207)](https://github.com/user-attachments/assets/3bfa5a2e-6c69-453a-a587-86512293c50f)


### 1. Time domain features: 
**These features are extracted directly from the waveform of the audio signal.**

   <br>__(a) *Zero-Crossing Rate*__: Zero Crossing Rate is the rate at which the signal changes from positive to negative or vice versa. It provides information about the frequency content of the signal.
   <br>![Screenshot (205)](https://github.com/user-attachments/assets/bbb90ed4-8126-4c97-bf40-9b41d47f3c9b)

   <br>__(b) *Root Mean Square Energy*__: RMS Energy is a measure of the signal’s overall energy or loudness over time. It provides insight into the amplitude variations of the audio signal.
   <br>![Screenshot (206)](https://github.com/user-attachments/assets/d17c0ab2-f147-4a61-8bfd-ed805b08c2e1)

### 2. Time-frequency domain features: 
**These features represent both time and frequency characteristics of the audio.**

   <br>__*MFCCs*__: Mel-frequency Cepstral Coefficients (MFCCs) provide a compact representation of the spectral envelope of a sound that closely relates to how humans perceive pitch and frequency content.
   <br>![Screenshot (210)](https://github.com/user-attachments/assets/1cfc62dd-504a-472a-a2a4-67766d1c3867)

### 3. Mel-Spectrograms: 
**A mel spectrogram shows how the frequency content of the signal changes over time.**
   <br>![Screenshot (208)](https://github.com/user-attachments/assets/358b1425-f02a-48cb-bd42-c636741a8fb8)


## Model Architecture
The model is a CNN (Convolutional Neural Network). It uses various layers such as Conv2D, Dropout, MaxPooling2D, Flatten, Dense etc. There are 6 hidden layers with activation ReLu. The output layer has activation Softmax for categorical classification. The model is fit with Adam optimizer and loss categorical_crossentropy.
<br>![Screenshot (204)](https://github.com/user-attachments/assets/ff493fd6-b51b-49e6-ac13-573913cfc553)

## Accuracy and Loss
The model achieves a training accuracy of 73.49% and loss of 0.7141, a validation accuracy of 54.63% and a loss of 1.2962 and a testing accuracy of 56% and a loss of 1.1627.
<br>![Screenshot (203)](https://github.com/user-attachments/assets/c2a79010-f107-4466-8611-c429dd9d2f47)


## Evaluation and Predictions

**Sample Predictions**
<br>![Screenshot (212)](https://github.com/user-attachments/assets/4c2d6f23-8f9f-443c-8440-5cd490f61270)

**Confusion matrix**
<br>![Screenshot (202)](https://github.com/user-attachments/assets/d9787090-ef3c-4311-8ff1-53aaab686a8e)

**Classification Report**
<br>![Screenshot (211)](https://github.com/user-attachments/assets/031f9889-ebb7-49c0-a144-c09ea40d63d4)



