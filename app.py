import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Cotizador 3D", page_icon="🖨️", layout="centered")

# CSS para banner + inputs + títulos negros
st.markdown("""
<style>
/* Banner superior */
.banner{
  background:#0b4ea2;              /* Azul Win-Tronic */
  height:120px;                    /* Alto del banner */
  border-radius:12px;
  margin-bottom:20px;              /* Espacio debajo */
  display:flex;
  align-items:center;
  justify-content:center;
  color:white;                     /* Texto blanco */
  font-size:36px;
  font-weight:bold;
  font-family:Arial, sans-serif;
  letter-spacing:2px;
}

/* Inputs de texto y número */
input[type="text"], input[type="number"] {
  border: 2px solid #3b5998;        
  border-radius: 8px;
  padding: 8px 12px;
  font-size: 16px;
  color: #0b2e59;                   
  background-color: #f9f9ff;        
}

/* Hover */
input[type="text"]:hover, input[type="number"]:hover {
  border: 2px solid #5a7fc1;        
}

/* Focus */
input[type="text"]:focus, input[type="number"]:focus {
  border: 2px solid #0b4ea2;        
  box-shadow: 0 0 6px #5a7fc1;      
  outline: none;
}

/* Títulos en negro */
h1, h2, h3, h4, h5, h6 {
  color: #000000 !important;
}
</style>
""", unsafe_allow_html=True)

# Banner Wintronic 3D
st.markdown('<div class="banner">WINTRONIC 3D</div>', unsafe_allow_html=True)

# Título principal
st.title("🖨️ Cotizaciones - Impresión 3D")

# Entradas
pieza = st.text_input("Nombre de la pieza en 3D")
dias = st.number_input("Días de impresión", min_value=0, step=1)
horas = st.number_input("Horas de impresión", min_value=0, step=1)
minutos = st.number_input("Minutos de impresión", min_value=0, step=1)
peso = st.number_input("Peso de la pieza en gramos (g)", min_value=0.0, step=0.1)
extras = st.number_input("Costos extras en pesos ($)", min_value=0.0, step=100.0)

# Parámetros base
costo_filamento_por_g = 85000
costo_energia_por_hora = 300
ganancia = 1  

# Cálculos
tiempo_total_horas = dias*24 + horas + minutos/60
costo_filamento = peso * costo_filamento_por_g
costo_energia = tiempo_total_horas * costo_energia_por_hora
costo_total = costo_filamento + costo_energia + extras
precio_final = costo_total * (1 + ganancia)

# Resultados
if st.button("Calcular"):
    st.subheader("📊 Resultado del cálculo")
    st.write(f"⏱ Tiempo total: {tiempo_total_horas:.2f} horas")
    st.write(f"🧵 Costo filamento: ${costo_filamento:,.0f}")
    st.write(f"⚡ Costo energía: ${costo_energia:,.0f}")
    st.write(f"➕ Extras: ${extras:,.0f}")
    st.write(f"💰 Costo total: ${costo_total:,.0f}")
    st.write(f"📦 Precio final sugerido: ${precio_final:,.0f}")
