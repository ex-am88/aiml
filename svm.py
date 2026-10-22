#python -m pip install pandas matplotlib scikit-learn
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# Load Iris dataset
iris = load_iris()

# Inspect dataset
print(dir(iris))
print(iris.feature_names)
print(iris.target_names)

# Create DataFrame
df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

print(df.head())

# Add target column
df["target"] = iris.target
print(df.head())

# Display flowers belonging to target 1
print(df[df.target == 1].head())

# Add flower names
df["flower_name"] = df.target.apply(
    lambda x: iris.target_names[x]
)

print(df.head())

# Separate flower species
df0 = df[df.target == 0]
df1 = df[df.target == 1]
df2 = df[df.target == 2]

print(df2.head())

# Scatter plot: Sepal Length vs Sepal Width
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")

plt.scatter(
    df0["sepal length (cm)"],
    df0["sepal width (cm)"]
)

plt.scatter(
    df1["sepal length (cm)"],
    df1["sepal width (cm)"],
    color="green",
    marker="*"
)

plt.show()

# Scatter plot: Petal Length vs Petal Width
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")

plt.scatter(
    df0["petal length (cm)"],
    df0["petal width (cm)"]
)

plt.scatter(
    df1["petal length (cm)"],
    df1["petal width (cm)"],
    color="green",
    marker="*"
)

plt.show()

# Import train_test_split
# Separate input and output variables
X = df.drop(["target", "flower_name"], axis="columns")
y = df.target

# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)

# Check training and testing data size
print(len(X_train))
print(len(X_test))

# Create and train SVM model
model = SVC()
model.fit(X_train, y_train)

# Check model accuracy
print(model.score(X_test, y_test))

# Predict flower species
print(model.predict([[4.8, 3.0, 1.5, 0.3]]))
print(model.predict([[6.5, 3.0, 5.5, 2.0]]))
print(model.predict([[5.5, 2.8, 4.2, 1.3]]))

# SVM with C = 100
model_C = SVC(C=100)
model_C.fit(X_train, y_train)
print(model_C.score(X_test, y_test))

# SVM with C = 10
model_C = SVC(C=10)
model_C.fit(X_train, y_train)
print(model_C.score(X_test, y_test))

# SVM with linear kernel
model_linear_kernel = SVC(kernel="linear")
model_linear_kernel.fit(X_train, y_train)

print(model_linear_kernel.score(X_test, y_test))
