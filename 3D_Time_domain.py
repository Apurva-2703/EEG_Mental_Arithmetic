#Here I use the scripts from the course "Signal processing for Neuroscience" by Ildar Rakhmatulin
#I have adapted the scripts to better suit this dataset.

# Import dependencies
import os
import pyedflib
import numpy as np
import pandas as pd
from utilities import bandpass_filter
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt

# Establish file path for SUBJECT 1, BASELINE data
edf_folder_path = "eeg-during-mental-arithmetic-tasks-1.0.0"
edf_path = os.path.join(edf_folder_path, "Subject00_1.edf") #Subject 1, baseline. (Change first 2 digits for subject number and last digit to 1 or 2 for baseline or test)
f = pyedflib.EdfReader(edf_path) #Open subject's file in python

#Select EEG channels for visualization (check f.getSignalLabels() to see available channels)
channel_names = f.getSignalLabels()
bandpass_signals = {}
selected_channels = ['EEG Cz', 'EEG Pz', 'EEG Fz']  # <- Change this list to your needs

#Bandpass filter selected channels
for label in selected_channels:
    if label == 'ECG ECG':
        continue
    try:
        idx = channel_names.index(label)
        data = f.readSignal(idx)
        filtered_signal = bandpass_filter(data, fs=500, lowcut=8.0, highcut=12.0, order = 5)
        bandpass_signals[label] = filtered_signal.astype(np.float32)
    except ValueError:
        print(f"Channel '{label}' not found in this EDF file.")
# Close file to avoid access or memory issues
f._close()

#Sanity check: Ensure filtered and raw data differ by plotting a 2D visual.
plt.figure()
plt.plot(data[:1000], label='Raw')
plt.plot(filtered_signal[:1000], label='Filtered')
plt.title(f"Check Filtering: {label}")
plt.legend()
plt.grid(True)
plt.show()

#Visualizing filtered data in a 3D time-domain graph
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

sample_channel = list(bandpass_signals.keys())[0]
x = np.arange(len(bandpass_signals[sample_channel])) / 500 # Time in seconds
y = np.arange(len(selected_channels))

for i, channel in enumerate(bandpass_signals.keys()):
    ax.plot(x, np.full_like(x, i), bandpass_signals[channel], label=channel)

# Add labels and title
ax.set_xlabel('Time')
ax.set_ylabel('Channels')
ax.set_zlabel('Signal Amplitude (µV)')
ax.set_title('3D Visualization of Filtered EEG Signals')

# Set y-ticks as channel names for easier reading
ax.set_yticks(np.arange(len(selected_channels)))
ax.set_yticklabels(selected_channels)
# Show the plot
plt.show()