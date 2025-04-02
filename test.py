# Install Cython using command terminal.
# Install pyEDFLib using command terminal. 
# Load a sample EDF file

import os
import pyedflib

edf_folder = "eeg-during-mental-arithmetic-tasks-1.0.0" #Folder path

sample_edf_path = os.path.join(edf_folder, "Subject01_1.edf")
f = pyedflib.EdfReader(sample_edf_path)
print(f'Processing sample file')
print(f'Signal labels: {f.getSignalLabels()}')
f.close()

#If the output of this code are the 23 channel labels, then the EDF library has been installed properly and we are ready to work!