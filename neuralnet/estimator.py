import json
import tensorflow as tf
import pandas as pd
import os

# Load the JSON data into a Python object
with open("jobs.json", "r") as f:
    data = json.load(f)

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Split the data into features (X) and target variable (y)
X = df.drop("budget", axis=1)
y = df["budget"]

# Encode categorical variables
X = pd.get_dummies(X, columns=["building_type", "efficiency_level", "hvac_type"])

# Convert data types to int
X = X.astype(int)
y = y.astype(int)

# Split the data into train and test sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Define the normalization layer
normalizer = tf.keras.layers.experimental.preprocessing.Normalization()
# Fit the normalization layer to the training data
normalizer.adapt(X_train)

# Define the input and output layers
model = tf.keras.Sequential()
model.add(normalizer)
model.add(tf.keras.layers.Dense(units=64, activation='relu', input_shape=(X_train.shape[1],)))
model.add(tf.keras.layers.Dense(units=1))


# Retrieve latest model data
checkpoint_path = "training_1/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)
if len(os.listdir(checkpoint_dir)) > 0:
    print("loading weights...")
    latest = tf.train.latest_checkpoint(checkpoint_dir)
    model.load_weights(latest)
    print("Weights loaded!")
if not os.path.exists(checkpoint_dir):
    os.makedirs(checkpoint_path)

# Create a callback that saves the model's weights
cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                 save_weights_only=True,
                                                 verbose=1)

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(X_train, 
             y_train, 
             epochs=100,
             batch_size=32,
             callbacks=[cp_callback])

# Save the model
model.save("estimator")

# Evaluate the model
loss = model.evaluate(X_test, y_test, verbose=2)
print("model MSE: {:5.2f}".format(loss))