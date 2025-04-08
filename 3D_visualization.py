#Here I use the scripts from the course "Signal processing for Neuroscience" by Ildar Rakhmatulin
#I have adapted the scripts to better suit this dataset.

# Import dependencies
import os
import pyedflib
import numpy as np
import pandas as pd
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt

# Establish file path for SUBJECT 1, BASELINE data
edf_folder_path = "eeg-during-mental-arithmetic-tasks-1.0.0"
edf_path = os.path.join(edf_folder_path, "Subject00_1.edf") #Subject 1, baseline.
f = pyedflib.EdfReader(edf_path) #Open subject's file in python

#Bandpass filter script adapted to this dataset
def bandpass_filter(data, fs, lowcut=1.0, highcut=40.0, order=5):
    """
    Apply a Butterworth bandpass filter to the data.

    Args:
        data (array-like): The signal to filter.
        fs (float): Sampling rate (Hz).
        lowcut (float): Low cutoff frequency (Hz).
        highcut (float): High cutoff frequency (Hz).
        order (int): Filter order.

    Returns:
        numpy array: The filtered signal.
    """
    nyq = 0.5 * fs  # Nyquist frequency
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return filtfilt(b, a, data)

#Looping bandpass filter script across "x"-number of channels.
channel_names = f.getSignalLabels()
bandpass_signals = {}
number_of_channels_in_graph = 5 #Change this to however many channels you want to graph
selected_channels = channel_names[:number_of_channels_in_graph]

for idx,label in enumerate(selected_channels):
    if label == 'ECG ECG':
        continue
    data  = f.readSignal(idx)
    filtered_signal = bandpass_filter(data, fs=500, lowcut=1.0, highcut=40.0)
    bandpass_signals[label] = filtered_signal.astype(np.float32)

# Close file to avoid access or memory issues
f.close()

#Visualizing filtered data in a 3D time-domain graph
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

sample_channel = list(bandpass_signals.keys())[0]
x = np.arange(len(bandpass_signals[sample_channel_channel])) / 500 # Time in seconds
y = np.arange(len(selected_channels))

for i, channel in enumerate(selected_channels):
    if channel == 'ECG ECG':
        continue
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

#NEXT UP: (1) Reduce numbers of channels being shown. (2) Make correlation matrix and MNE scalp visualization. (3) move on to between group analysis