
import pandas as pd

data = {
    "Employee": ["Aman", "Riya", "Karan", "Neha"],
    "Salary": [35000, 42000, 39000, 45000]
}

df = pd.DataFrame(data)

print(df)
print("\nHighest Salary =", df["Salary"].max())
print("Average Salary =", df["Salary"].mean())



import numpy as np
import matplotlib.pyplot as plt

days = np.array([1, 2, 3, 4, 5])
temperature = np.array([30, 32, 31, 35, 33])

plt.plot(days, temperature, marker='o')
plt.ylabel("Temperature (°C)")
plt.show()



from sklearn.tree import DecisionTreeClassifier

marks = [[35], [45], [55], [65], [75], [85]]
result = ["Fail", "Fail", "Pass", "Pass", "Pass", "Pass"]

model = DecisionTreeClassifier()
model.fit(marks, result)

prediction = model.predict([[50]])
print("Prediction:", prediction[0])



import tensorflow as tf
import numpy as np

x_train = np.array([1, 2, 3, 4, 5], dtype=float)
y_train = np.array([10, 20, 30, 40, 50], dtype=float)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])

model.compile(optimizer='sgd', loss='mean_squared_error')

model.fit(x_train, y_train, epochs=50, verbose=0)

prediction = model.predict(np.array([6.0]), verbose=0)
print("Predicted Price:", prediction[0][0])
