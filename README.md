# 🏠 Housing Price Prediction – Enkla AI-modellen i Python

Detta projekt är en introduktion till maskininlärning (ML) och visar hur man bygger en **linjär regressionsmodell** för att förutsäga bostadspriser baserat på två faktorer:

- 📐 Bostadens storlek i kvadratmeter  
- 🛏️ Antal rum

Projektet är byggt i **Google Colab** och använder klassiska Python-bibliotek för ML och visualisering.

---

## 🚀 Teknik & Bibliotek

- `numpy` – för att hantera numeriska arrayer
- `scikit-learn` – för att bygga och träna ML-modellen
- `matplotlib` – för att visualisera resultatet (valfritt)

---

## 📈 Modellen

Vi använder `LinearRegression` från `scikit-learn`:

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X, y)

Inmatningsdata (X) består av kvadratmeter och antal rum. Utdata (y) är det faktiska priset (i tusentals kronor).

⸻

🔍 Exempel på förutsägelse

new_apartment = np.array([[70, 3]])
predicted_price = model.predict(new_apartment)
print(predicted_price)

---

💡 Varför det här projektet?

Detta är mitt första AI-projekt och ett steg mot att bli AI Engineer.
Fokus ligger på att förstå grunderna i datainmatning, modellträning och förutsägelser.

⸻

📂 Struktur

📁 housing-price-prediction/
├── housing_prediction.ipynb    # Google Colab-notebook
└── README.md
