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

# Filtering datasets
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

#Filtering for MNE datasets
def load_and_filter(file_path, selected_channels, fs=500, lowcut=8.0, highcut=12.0, order=5):
    f = pyedflib.EdfReader(file_path)
    channel_names = f.getSignalLabels()
    filtered = {}
    for ch in selected_channels:
        if ch not in channel_names:
            continue
        data = f.readSignal(channel_names.index(ch))
        filtered[ch] = bandpass_filter(data, fs, lowcut, highcut, order)
    f.close()
    return filtered

#Combining filtered data for baseline and test files for each subject
def concatenate_bandpass_dicts(dict1, dict2):
    all_channels = dict1.keys()
    concatenated = {}
    for ch in all_channels:
        concatenated[ch] = np.concatenate([dict1[ch], dict2[ch]])
    return concatenated

#Turning MNE info files to Topomap visualization
def create_evoked_from_bandpassed(bandpassed_data, sfreq=500, montage_name='standard_1020'):
    raw_names = list(bandpassed_data.keys())
    clean_names = [name.replace("EEG ", "") for name in raw_names]
    data_array = np.array([bandpassed_data[ch] for ch in raw_names])  # Shape: (n_channels, n_times)

    info = mne.create_info(ch_names=clean_names, sfreq=sfreq, ch_types='eeg')
    montage = mne.channels.make_standard_montage(montage_name)
    info.set_montage(montage, on_missing='ignore')

    evoked = mne.EvokedArray(data_array / 1e6, info) #This scales the data to the right unit
    return evoked