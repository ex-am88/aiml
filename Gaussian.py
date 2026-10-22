#python -m pip install pandas numpy matplotlib seaborn scikit-learn
#curl -L "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data" -o adult.csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    roc_auc_score,
    roc_curve
)

# Load dataset
df = pd.read_csv("adult.csv", header=None, skipinitialspace=True)

df.columns = [
    "age", "workclass", "fnlwgt", "education",
    "education_num", "marital_status", "occupation",
    "relationship", "race", "sex", "capital_gain",
    "capital_loss", "hours_per_week", "native_country",
    "income"
]

print("First five records:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nMissing Values:")
print(df.isnull().sum())

# Replace whitespace and '?' values with missing values
df = df.replace(r"^\s*\?$", np.nan, regex=True)
df = df.replace(r"^\s*$", np.nan, regex=True)

# Remove missing values
df = df.dropna()

# Encode categorical columns
label_encoder = LabelEncoder()

categorical_columns = df.select_dtypes(
    include=["object"]
).columns

for column in categorical_columns:
    df[column] = label_encoder.fit_transform(df[column])

# Separate features and target
# Change 'income' if your target column has a different name
X = df.drop("income", axis=1)
y = df["income"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])

# Create and train model
model = GaussianNB()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy:")
print(accuracy)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

# Classification Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# ROC-AUC
y_probability = model.predict_proba(X_test)[:, 1]
auc = roc_auc_score(y_test, y_probability)

print("\nROC-AUC Score:")
print(auc)

# Confusion Matrix Plot
plt.figure(figsize=(6, 4))
sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues"
)
plt.xlabel("Predicted Class")
plt.ylabel("Actual Class")
plt.title("Confusion Matrix - Naive Bayes")
plt.show()

# ROC Curve
fpr, tpr, thresholds = roc_curve(
    y_test,
    y_probability
)

plt.figure(figsize=(6, 4))
plt.plot(
    fpr,
    tpr,
    label=f"AUC = {auc:.3f}"
)
plt.plot(
    [0, 1],
    [0, 1],
    linestyle="--"
)
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve - Naive Bayes")
plt.legend()
plt.show()
