import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Load dataset
data = pd.read_csv("data.csv")

# Define input features and target
X = data[['Fan-in', 'Fan-out', 'Path Length']]
y = data['Logic Depth']

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
error = mean_absolute_error(y_test, y_pred)

print(f"Mean Absolute Error: {error}")

# Save the model
import joblib
joblib.dump(model, "timing_model.pkl")
print("Model saved as timing_model.pkl")
