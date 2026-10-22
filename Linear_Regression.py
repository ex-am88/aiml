
#curl -L "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv" -o "auto-mpg.csv"
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("auto-mpg.csv")

# Replace '?' with missing values
df.replace("?", pd.NA, inplace=True)

# Convert horsepower to numeric
df["horsepower"] = pd.to_numeric(
    df["horsepower"], errors="coerce"
)

# Remove missing values
df = df.dropna()

# Independent and dependent variables
X = df[["horsepower"]]
Y = df["mpg"]

# Create and train model
model = LinearRegression()
model.fit(X, Y)

# Predict values
Y_pred = model.predict(X)

# Display results
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

# Plot graph
plt.scatter(X, Y, color="green")
plt.plot(X, Y_pred, color="red")
plt.xlabel("Horsepower")
plt.ylabel("MPG")
plt.title("Linear Regression using Auto MPG Dataset")
plt.show()
