import json
import tensorflow as tf
import pandas as pd
import os

# Load the JSON data into a Python object
with open("5klastjobs", "r") as f:
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


# Retrieve latest model data
checkpoint_path = "training_1/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)
if not os.path.exists(checkpoint_dir):
    os.makedirs(checkpoint_path)
if(len(os.listdir(checkpoint_dir)) > 0):
    latest = tf.train.latest_checkpoint(checkpoint_dir)
    model.load_weights(latest)

# Create a callback that saves the model's weights
cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                 save_weights_only=True,
                                                 verbose=1)

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(X_train, 
            y_train, 
            epochs=1000,
            batch_size=32,
            callbacks=[cp_callback])

# Evaluate the model
loss = model.evaluate(X_test, y_test, verbose=2)
print("model MSE: {:5.2f}".format(loss))