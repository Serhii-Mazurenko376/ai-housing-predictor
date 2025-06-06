import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os

# Ladda CSV relativt från src/
csv_path = os.path.join('..', 'data', 'housing.csv')
df = pd.read_csv(csv_path)

# Separera X och y
X = df[['rooms', 'sq_m']]
y = df['price']

# Träna modell
model = LinearRegression()
model.fit(X, y)

# Testa modell med exempeldata
test_data = [[3, 70]]  # 3 rum, 70 kvm
prediction = model.predict(test_data)

# Visa resultat
print(f"💰 Förväntat pris: {int(prediction[0]):,} kr")

# Spara modellen
model_path = os.path.join('..', 'model.pkl')
joblib.dump(model, model_path)
print("✅ Modell sparad som model.pkl")
