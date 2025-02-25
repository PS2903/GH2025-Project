# AI Algorithm for Predicting Combinational Logic Depth

## Introduction
This project aims to predict the *combinational logic depth* of signals in an RTL module using *Machine Learning (ML). This helps identify potential **timing violations* early, without requiring full synthesis.

## Problem Statement
Timing analysis is a crucial step in RTL design, but traditional synthesis tools take a long time to generate timing reports. By leveraging ML, we can quickly estimate the logic depth of a signal, enabling faster design iterations.

## Approach
1. *Dataset Creation*
   - Manually created a dataset containing RTL signal properties like *fan-in, fan-out, path length, and logic depth*.
   - Used a CSV file (data.csv) for training.

2. *Feature Engineering*
   - Key features: *Fan-in, Fan-out, Path Length*.
   - Target: *Logic Depth*.

3. *Model Selection & Training*
   - Used a *Random Forest Regressor* for prediction.
   - Split dataset into *training (80%) and testing (20%)*.
   - Evaluated using *Mean Absolute Error (MAE)*.

4. *Prediction & Testing*
   - New signals can be tested using the trained ML model (timing_model.pkl).
   - A separate script (predict.py) loads the model and makes predictions.

## Installation & Running the Code
### Prerequisites
- Python 3.8+
- Required libraries: pandas, scikit-learn, joblib

### Setup
1. Clone the repository:
   bash
   git clone <repo-link>
   cd <repo-folder>
   
2. Install dependencies:
   bash
   pip install -r requirements.txt
   
3. Train the model:
   bash
   python train_model.py
   
4. Predict logic depth for a new signal:
   bash
   python predict.py
   

## Files in the Repository
| File | Description |
|------|-------------|
| data.csv | Sample dataset with logic depth values |
| train_model.py | Trains the ML model and saves it as timing_model.pkl |
| predict.py | Loads timing_model.pkl and predicts logic depth for a new signal |
| README.md | Documentation for the project |

## Future Improvements
- Automate feature extraction using *Yosys synthesis reports*.
- Explore *Graph Neural Networks (GNNs)* for better accuracy.
- Expand dataset with real RTL designs.

## Contributors
- *Prerna Singh*

## License
This project is released under the MIT License.