import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

area = np.array([[1800]])
prediction = model.predict(area)

print(f"🏠 Predicted price: {prediction[0]}")