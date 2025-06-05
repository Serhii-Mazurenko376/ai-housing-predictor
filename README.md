# ai-housing-predictor
# 🏠 AI Housing Price Predictor

Ett enkelt AI-projekt där vi tränar en modell för att förutsäga bostadspriser baserat på antal rum och kvadratmeter.

---

## 🚀 Projektmål

- Förstå grunderna i maskininlärning (ML)
- Använda verklig tabell-data (CSV)
- Träna en `LinearRegression`-modell
- Testa modellen med ny input

---

## 📁 Projektstruktur

```bash
ai-housing-predictor/
├── data/
│   └── housing.csv
├── src/
│   └── train_model.py
├── model.pkl
├── README.md
└── LICENSE

🔧 Använda projektet
	1.	Installera pandas, scikit-learn, joblib
	2.	Kör train_model.py
	3.	Testresultat skrivs ut i terminalen

🔢 Exempel
test = [[3, 70]]
prediction = model.predict(test)
print(f'Förväntat pris: {int(prediction[0]):,} kr')
