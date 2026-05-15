# 1. Import Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# 2. Data Loading and Preprocessing
# Ensure your CSV file is in the same directory as this script
try:
    df = pd.read_csv('pathogenicity_data.csv')
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: Dataset file not found. Make sure 'pathogenicity_data.csv' is in the same folder.")
    exit()

# Define features (X) and target (y)
# Adjust column names to match your dataset
X = df[['Gene', 'Mutation_Type']]
y = df['Pathogenicity']

# Perform One-Hot Encoding on the categorical features
encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
X_encoded = encoder.fit_transform(X)

# Convert the encoded array back to a DataFrame for readability
feature_names = encoder.get_feature_names_out(X.columns)
X_encoded_df = pd.DataFrame(X_encoded, columns=feature_names)

print("\nFirst 5 rows of the one-hot encoded features:")
print(X_encoded_df.head())

# 3. Handle Class Imbalance with SMOTE
print("\nInitial class distribution:")
print(y.value_counts())

smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_encoded_df, y)

print("\nClass distribution after SMOTE:")
print(y_resampled.value_counts())

# 4. Model Training and Evaluation
# Split the resampled data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)

# Initialize and train the Random Forest Classifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = model.predict(X_test)

# Evaluate the model's performance
print("\n--- Model Evaluation ---")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(f"Precision: {precision_score(y_test, y_pred, pos_label='Pathogenic'):.4f}")
print(f"Recall: {recall_score(y_test, y_pred, pos_label='Pathogenic'):.4f}")
print(f"F1-Score: {f1_score(y_test, y_pred, pos_label='Pathogenic'):.4f}")

# Display the Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))