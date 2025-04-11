#Here I use the scripts from the course "Signal processing for Neuroscience" by Ildar Rakhmatulin
#I have adapted the scripts to better suit this dataset.

#Import dependencies
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from utilities import load_filtered_channels  #Helper function from utilities

#Select a subject's baseline and test file
edf_folder = "eeg-during-mental-arithmetic-tasks-1.0.0"
baseline_path = os.path.join(edf_folder, "Subject00_1.edf") #Change subject number between 00 to 35
test_path = os.path.join(edf_folder, "Subject00_2.edf") #Change subject number between 00 and 35
selected_channels = ["EEG Fz", "EEG Cz", "EEG Pz", "EEG C3", "EEG C4", "EEG T3", "EEG T4", "EEG Fp1"]

# Clean both files using bandpass filter (Set to 8-12Hz, change in utilities if need another range)
baseline_filtered = load_and_filter(baseline_path, selected_channels)
test_filtered = load_and_filter(test_path, selected_channels)

# Concatenate data across the time-axis
full_filtered = concatenate_bandpass_dicts(baseline_filtered, test_filtered)

# Convert to MNE evoked object
evoked_combined = create_evoked_from_bandpassed(full_filtered)

# Plot Topomaps using a fixed time interval
duration = evoked_combined.times[-1]  # Total duration in seconds
times_to_plot = np.arange(0, duration, 10)
evoked_combined.plot_topomap(times_to_plot, ch_type='eeg', ncols=4,time_unit='s', nrows="auto", show='False')