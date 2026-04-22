import pandas as pd
import streamlit as st

st.set_page_config(page_title="Calculadora de Esmolol", page_icon="💉")

PRESENTACIONES = {
    "2.5 g en 10 mL": {"mg_totales": 2500},
    "100 mg en 10 mL": {"mg_totales": 100},
}

VOLUMENES = [100, 250]
DOSIS_ESTANDAR = [25, 50, 100, 150, 200, 250, 300]

def calcular(presentacion, volumen, peso, dosis):
    mg_totales = PRESENTACIONES[presentacion]["mg_totales"]
    concentracion = mg_totales / volumen

    mcg_min = dosis * peso
    mg_h = (mcg_min / 1000) * 60
    ml_h = mg_h / concentracion

    return concentracion, mcg_min, mg_h, ml_h

st.title("💉 Calculadora de Esmolol")

with st.sidebar:
    presentacion = st.selectbox("Presentación", list(PRESENTACIONES.keys()))
    volumen = st.selectbox("Volumen (mL)", VOLUMENES)
    peso = st.number_input("Peso (kg)", value=70.0)
    modo = st.radio("Modo", ["Individual", "Tabla"])

if modo == "Individual":
    dosis = st.number_input("Dosis (mcg/kg/min)", value=50.0)

    conc, mcg_min, mg_h, ml_h = calcular(presentacion, volumen, peso, dosis)

    st.subheader("Resultado")
    st.write(f"Concentración: {conc:.2f} mg/mL")
    st.write(f"Dosis: {mcg_min:.2f} mcg/min")
    st.write(f"💉 Bomba: {ml_h:.2f} mL/h")

else:
    filas = []
    for d in DOSIS_ESTANDAR:
        conc, mcg_min, mg_h, ml_h = calcular(presentacion, volumen, peso, d)
        filas.append([d, mcg_min, mg_h, ml_h])

    df = pd.DataFrame(filas, columns=["mcg/kg/min", "mcg/min", "mg/h", "mL/h"])
    st.dataframe(df)
