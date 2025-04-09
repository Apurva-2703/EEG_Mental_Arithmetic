#Here I use the scripts from the course "Signal processing for Neuroscience" by Ildar Rakhmatulin
#I have adapted the scripts to better suit this dataset.

#Import dependencies
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from utilities import load_filtered_channels  #Helper function from utilities

#Select a subject file
edf_folder = "eeg-during-mental-arithmetic-tasks-1.0.0"
edf_file = os.path.join(edf_folder, "Subject00_1.edf")

#Select which channels you want in the correlation matrix
channels = ['EEG Fz', 'EEG F3', 'EEG F4', 'EEG F7', 'EEG F8', 'EEG Cz', 'EEG C3', 'EEG C4', 'EEG Pz', 'EEG P3', 'EEG P4', 'EEG T3', 'EEG T4', 'EEG T5', 'EEG T6', 'EEG O1', 'EEG O2']

#Perform a bandpass filter on the selected data (ALPHA BAND for example: 8-12Hz)
signals = load_filtered_channels(edf_file, channels, fs=500, lowcut=8.0, highcut=12.0, order=5)

# Step 4: Make correlation matrix
data_matrix = np.array([signals[ch] for ch in signals])  # shape: (channels, time)
correlation_matrix = np.corrcoef(data_matrix)

# Step 5: Visualize correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, xticklabels=signals.keys(), yticklabels=signals.keys(), annot=True, cmap='coolwarm')
plt.title("EEG Channel Correlation Matrix")
plt.tight_layout()
plt.show()