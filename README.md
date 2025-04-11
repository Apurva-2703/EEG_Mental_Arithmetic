# 🧠 EEG Mental Arithmetic Analysis Pipeline

This project uses an open-source EEG dataset from **Zyma et al. (2019)** to build a compact EEG signal processing pipeline. It includes tools for:

- ✅ Time-domain visualization  
- ✅ Spatial scalp topographies  
- ✅ Channel connectivity (correlation)  
- ✅ Frequency-domain analysis (planned)

The goal is to practice applied EEG signal processing by analyzing changes in brain activity during mental arithmetic tasks.

---

## 📁 Project Structure

- **`utilities.py`**  
  Helper functions for loading, filtering (via Butterworth bandpass), and cleaning EEG data.

- **`Topomap_visual.py`**  
  Generates scalp topographies (topomaps) at different timepoints using MNE, comparing baseline and task conditions.

- **`correlation_matrix.py`**  
  Computes and visualizes Pearson correlation matrices across EEG channels to explore spatial connectivity.

- **`3D_time_domain.py`**  
  Creates interactive 3D time-series plots for selected EEG channels using Matplotlib.

---

## 🛠️ Dependencies

This project was built in Python 3. You can install all dependencies with:

```bash
pip install numpy scipy matplotlib pandas mne pyedflib
```

## 🚀 How to Run

Download the EEG dataset from PhysioNet.

Place the .edf files inside the project folder (eeg-during-mental-arithmetic-tasks-1.0.0).

Open each script and run them individually depending on the type of analysis:

Topomap: Spatial scalp maps across time.

Correlation: Channel-to-channel connectivity map.

3D: Raw EEG waveforms in 3D space.

(Optional) Modify the selected_channels list to focus on specific electrode locations.

## 📚 Citations
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

## 🧠 Learning Notes
This project was created while independently completing:

Signal Processing for Neuroscience (Ildar Rakhmatulin)

Neuroelectronic Recording and Processing - Neurotechnology Microcredential (Queen’s University)

It serves as a personal milestone in my journey into neurotechnology and BCI systems development.
