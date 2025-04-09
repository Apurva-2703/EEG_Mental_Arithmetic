# Import os, numpy and EDF library
import os
import pyedflib
import numpy as np
import pandas as pd
from scipy.signal import butter, filtfilt

# Establish file path to raw data
edf_folder_path = "eeg-during-mental-arithmetic-tasks-1.0.0"
edf_files = [f for f in os.listdir(edf_folder_path) if f.endswith(".edf")]

# Butterworth filter
def bandpass_filter(data, fs, lowcut, highcut, order):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return filtfilt(b, a, data)

# Filtered datasets
def load_filtered_channels(edf_path, selected_channels, fs=500, lowcut=8.0, highcut=12.0, order=5):
    f = pyedflib.EdfReader(edf_path)
    channel_names = f.getSignalLabels()
    bandpass_signals = {}

    for label in selected_channels:
        if label == 'ECG ECG':
            continue
        try:
            idx = channel_names.index(label)
            data = f.readSignal(idx)
            filtered = bandpass_filter(data, fs, lowcut, highcut, order)
            bandpass_signals[label] = filtered.astype(np.float32)
        except ValueError:
            print(f"Channel '{label}' not found in {edf_path}")
    f._close()
    return bandpass_signals