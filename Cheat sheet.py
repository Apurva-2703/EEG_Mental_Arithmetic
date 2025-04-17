#Import dependencies

import os
import pyedflib

#Select a subject (baseline or test file) and a channel
edf_folder = "eeg-during-mental-arithmetic-tasks-1.0.0"
baseline_path = os.path.join(edf_folder, "Subject00_1.edf") #Change subject number between 00 to 35
f = pyedflib.EdfReader(baseline_path)

#Get signal labels
labels = f.getSignalLabels()
fz_index = labels.index("EEG Cz")

f.getSampleFrequency(fz_index)


