🧠 EEG Mental Arithmetic Analysis Pipeline

This project uses an open-source EEG dataset from Zyma et al. (2019) to build a small but versatile EEG signal processing pipeline. It includes tools for spatial, frequency, time-domain, and connectivity analysis—all developed in Python using libraries such as MNE, PyEDFlib, and Matplotlib.

The goal is to practice applied EEG signal processing in a hands-on, reproducible way by analyzing changes in brain activity during mental arithmetic tasks.

📁 Project Structure
* utilities.py
A collection of helper functions for loading, filtering (via Butterworth bandpass), and cleaning EEG data from EDF files.

* Topomap_visual.py
Uses the MNE library to generate scalp topographies (topomaps) at different timepoints for alpha-band EEG (8–12Hz), comparing baseline and task conditions.

* correlation_matrix.py
Computes and visualizes the Pearson correlation matrix across EEG channels to explore spatial connectivity patterns during cognitive tasks.

* 3D_time_domain.py
Creates interactive 3D time-series plots for selected EEG channels, offering a temporal and spatial view of activity changes over time.

🛠️ Dependencies
This project was built in Python 3 and uses the following libraries:

- numpy
- scipy
- matplotlib
- pandas
- mne
- pyedflib
- os
- Cython (via dependencies)

You can install the required libraries using the following code snippet in bash terminal :

pip install numpy scipy matplotlib pandas mne pyedflib

🚀 How to Run

Download the EEG dataset from PhysioNet.

Place the .edf files inside the project folder (eeg-during-mental-arithmetic-tasks-1.0.0).

Open each script and run them individually depending on the type of analysis:

Topomap: Spatial scalp maps across time.

Correlation: Channel-to-channel connectivity map.

3D: Raw EEG waveforms in 3D space.

(Optional) Modify the selected_channels list to focus on specific electrode locations.

📚 Citations
Original Dataset:

Zyma I, Tukaev S, Seleznov I, Kiyono K, Popov A, Chernykh M, Shpenkov O.
Electroencephalograms during Mental Arithmetic Task Performance.
Data. 2019; 4(1):14. https://doi.org/10.3390/data4010014

PyEDFlib Library:

Holger, Simon Kern, Dimitri Papadopoulos Orfanos, et al.
pyEDFlib: Python EDF/BDF file reader/writer.
Zenodo, 2025. https://doi.org/10.5281/zenodo.14957195

PhysioNet Reference:

Goldberger AL, Amaral LAN, Glass L, et al.
PhysioBank, PhysioToolkit, and PhysioNet: Components of a new research resource for complex physiologic signals.
Circulation. 2000;101(23):e215–e220.

🧠 Learning Notes
This project was created while independently completing:

Signal Processing for Neuroscience (Ildar Rakhmatulin)

Neurotechnology Microcredential (Queen’s University)

It serves as a personal milestone in my journey into neurotechnology and BCI systems development.