import tensorflow as tf
import json
import pandas as pd

# Load the JSON data into a Python object
with open("data.json", "r") as f:
    data = json.load(f)

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Split the data into features (X) and target variable (y)
X = df.drop("budget", axis=1)
y = df["budget"]

# Encode categorical variablesip3 install pandas
X = pd.get_dummies(X, columns=["building_type", "efficiency_level", "hvac_type"])

# Split the data into train and test sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Normalize the numerical variables
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train[["building_area", "building_volume", "deadline_months"]] = scaler.fit_transform(X_train[["building_area", "building_volume", "deadline_months"]])
X_test[["building_area", "building_volume", "deadline_months"]] = scaler.transform(X_test[["building_area", "building_volume", "deadline_months"]])



# Define the input and output layers
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(units=64, activation='relu', input_shape=(X_train.shape[1],)))
model.add(tf.keras.layers.Dense(units=1))

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(X_train, y_train, epochs=50, batch_size=32)

# Make predictions on the test data
y_pred = model.predict(X_test)