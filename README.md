# 🩺 Clinical Decision Tools for Internal Medicine

A collection of practical, evidence-based digital tools designed to support clinical decision-making in internal medicine. This project focuses on accurate dosing, risk stratification, and intuitive, bedside-friendly interfaces for real-world clinical use.

---

## 🚀 Live Demo
👉 

---

## 🎯 Features

- 💉 Drug dose calculators (e.g., Esmolol infusion)
- 📊 Standard titration tables for rapid clinical use
- ⚙️ Real-time conversion to infusion rates (mL/h)
- 📱 Mobile-friendly interface (usable at bedside)
- 🧾 Clinical summary outputs for quick decision-making

---

## 🧠 Current Tools

### Esmolol Infusion Calculator
- Supports:
  - 2.5 g / 10 mL
  - 100 mg / 10 mL
- Dilution options:
  - 100 mL
  - 250 mL
- Calculates:
  - mcg/kg/min → mcg/min → mg/h
  - Infusion rate in mL/h
- Includes:
  - Standard titration tables
  - High-dose warning (>300 mcg/kg/min)
 
---
## ⚠️ Medical Disclaimer

This tool is intended for educational and clinical support purposes only.
It does not replace clinical judgment. The author assumes no responsibility for misuse or clinical decisions based on this tool.

---

## 🛠️ Installation (Local)

```bash
pip install -r requirements.txt
streamlit run app.py
