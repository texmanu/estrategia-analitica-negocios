import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración inicial
st.set_page_config(page_title="Análisis de Segmentos - Banco ML", layout="centered")
st.title("📊 Análisis de Segmentación de Clientes - Banco ML")

# Cargar datos
@st.cache_data
def load_data():
    return pd.read_csv("clientes_segmentados.csv")

df = load_data()

# Distribución de clientes por segmento
st.header("Distribución de Clientes por Segmento")
segment_counts = df['segmento_nombre'].value_counts()
fig1, ax1 = plt.subplots(figsize=(6, 6))
ax1.pie(segment_counts, labels=segment_counts.index, autopct='%1.1f%%', startangle=140)
ax1.axis('equal')
st.pyplot(fig1)

# Tasa de conversión por segmento
st.header("Tasa de Conversión por Segmento")
conversion = df.groupby('segmento_nombre')['deposit'].apply(lambda x: (x == 'yes').mean()).sort_values(ascending=False)
fig2, ax2 = plt.subplots(figsize=(8, 5))
sns.barplot(x=conversion.values, y=conversion.index, palette='Blues_d', ax=ax2)
ax2.set_xlabel("Tasa de Conversión")
st.pyplot(fig2)

# Balance promedio por segmento
st.header("Balance Promedio por Segmento")
avg_balance = df.groupby('segmento_nombre')['balance'].mean().sort_values()
fig3, ax3 = plt.subplots(figsize=(8, 5))
sns.barplot(x=avg_balance.values, y=avg_balance.index, palette='Greens_d', ax=ax3)
ax3.set_xlabel("Balance Promedio (escalado)")
st.pyplot(fig3)

# Footer
st.markdown("---")
st.markdown("Desarrollado por el equipo de analítica para el proyecto Banco ML ✨")
