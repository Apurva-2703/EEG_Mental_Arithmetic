# Import os, numpy and EDF library
import os
import pyedflib
import numpy as np

# Establish file path to raw data
edf_folder_path = "eeg-during-mental-arithmetic-tasks-1.0.0"
edf_files = [f for f in os.listdir(edf_folder_path) if f.endswith(".edf")]

# Open each file in the folder and ensure proper data composition (Sampling freq. and number of signals)
for edf_file in edf_files:
    edf_path = os.path.join(edf_folder_path, edf_file)
    f = pyedflib.EdfReader(edf_path) #Open the file in Python
    print(f"Processing {edf_file}")
    print(f'Total EEG Channels: {f.signals_in_file}') #21 Signals per EEG recording.
    print(f"Sampling frequency: {f.getSampleFrequencies()}") #Sampling Frequency at 500Hz
    f.close()

#Next up:
# Visualize time-domain EEG data for both conditions of the same participant (create loop to reiterate)
# Determine whether to use single channels or agregated data (across participants/within participant) for the FFT or spectogram.
# Determine what statistical test to us for comparing the two groups (B and G mental arithmetics) 