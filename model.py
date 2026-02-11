import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle   

# Sample data
data = pd.DataFrame({
    "area": [1000, 1500, 2000],
    "price": [50, 75, 100]
})

X = data[["area"]]
y = data["price"]

model = LinearRegression()
model.fit(X, y)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("✅ Model trained & saved")
