import joblib
import pandas as pd

# Load trained model
model = joblib.load("timing_model.pkl")

# Example test data (replace with real RTL features)
test_data = pd.DataFrame({
    'Fan-in': [3],
    'Fan-out': [2],
    'Path Length': [4]
})

# Predict Logic Depth
predicted_depth = model.predict(test_data)
print(f"Predicted Logic Depth: {predicted_depth[0]}")
