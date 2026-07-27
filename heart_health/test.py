import joblib

model = joblib.load("KNN_heart.pkl")
print("✅ Model Loaded")

scaler = joblib.load("scaler.pkl")
print("✅ Scaler Loaded")

columns = joblib.load("columns.pkl")
print("✅ Columns Loaded")

print(type(model))
print(type(scaler))
print(type(columns))
print(columns[:5])
