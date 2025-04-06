#Here I use the scripts from the course "Signal processing for Neuroscience" by Ildar Rakhmatulin
#I have adapted the scripts to better suit this dataset.

# Import os, numpy and EDF library
import os
import pyedflib
import numpy as np
import pandas as pd

# Establish file path to raw data
edf_folder_path = "eeg-during-mental-arithmetic-tasks-1.0.0"
edf_path = os.path.join(edf_folder_path, "Subject00_1.edf") #Subject 1, baseline.
f = pyedflib.EdfReader(edf_path) #Open subject's file in python

# Import dependencies
from scipy.signal import butter, filtfilt

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

#Looping bandpass filter script across all channels.
channel_names = f.getSignalLabels()
bandpass_signals = {}
for idx,label in enumerate(channel_names):
    data  = f.readSignal(idx)
    filtered_signal = bandpass_filter(data, fs=500, lowcut=1.0, highcut=40.0)
    bandpass_signals[label] = filtered_signal
