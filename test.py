import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split

# Load the data
df = pd.read_csv("dataset.csv")

# Preprocess the data
df = df.drop(["Name", "Ticket", "Cabin", "PassengerId", "Embarked", "SibSp", "Parch", "Fare"], axis=1)  # Drop irrelevant columns
# df = pd.get_dummies(df, columns=["Sex"])  # One-hot encode categorical columns
df["Sex"] = df['Sex'].apply(lambda x: 1 if x == "female" else 0)
df = df.fillna(df.mean())  # Fill missing values with the mean
# Split the data into training, validation, and test sets
train_data, test_data, train_labels, test_labels = train_test_split(df.drop("Survived", axis=1), df["Survived"], test_size=0.5)
train_data, val_data, train_labels, val_labels = train_test_split(train_data, train_labels, test_size=0.5)

# Build the model
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(32, activation="relu", input_shape=(train_data.shape[1],)))
model.add(tf.keras.layers.Dense(16, activation="relu"))
model.add(tf.keras.layers.Dense(1, activation="sigmoid"))

# Compile the model
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# Train the model
history = model.fit(train_data, train_labels, batch_size=32, epochs=100, validation_data=(val_data, val_labels))

# Evaluate the model
test_loss, test_accuracy = model.evaluate(test_data, test_labels)
print("Test Loss:", test_loss)
print("Test Accuracy:", test_accuracy)

def predict_survival(model, Pclass, Sex, Age):
    # Preprocess the input data
    input_data = pd.DataFrame({
        "Pclass": [Pclass],
        "Age": [Age]
    })
    input_data["Sex"] = [1 if Sex == "female" else 0]

    # Make a prediction
    prediction = model.predict(input_data)[0][0]

    # Return the result
    if prediction >= 0.5:
        print(prediction)
        return "Survived"
    else:
        return "Not Survived"


# Example usage
result = predict_survival(model, 1, "male", 5)
print(result)