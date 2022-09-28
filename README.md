# pythia
# Author: Cole Johnston
# co-authors: Nora Eisner

## Contributors: Dominic Bowman


Modules and routines for time-series analysis of astronomical data sets.


timeseries/periodograms -- library containing functions for time-series analysis

To install, use miniconda3 or anaconda3, and run:
```
conda create -n pythia python=3.7
conda activate pythia
```

Then install pythia from GitHub:
```
pip install git+https://github.com/astrobatty/pythia.git
```
or if you don't have pip, download the package as a zip file (unde the `CODE` menu), extract it, and type in the extracted directory:
```
pip install .
```

To use the Kepler test file, go the /timeseries/ directory and type:
```
python test_kepler.py
```


### TO DO:
  - Generalize handling of priors
  - Include GUI support
  - Include Gaussian Processes
  - Expand to multiple filters (long term)
