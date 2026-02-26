import streamlit as st
from PIL import Image

st.title("EEz egy kísérleti oldal")

st.header("Ez az oldal egy teszt")
st.write("CLAVICULAR")

image = Image.open('ARCANGEL_ABUSADOL.jpg')
st.image(image, caption='Interfaces Multimodales')

texto = st.text_input('eSCRIbe AlGo')
st.write('eL TexTO EsCRito es:', texto)

st.subheader("AHoRa UsARemos DoS CoLUMnas")

col1, col2 = st.columns(2)

with col1:
    st.subheader("TEz az első oszlop")
    resp = st.checkbox('Estoy de Acuerdo')

with col2:
    st.subheader("Ez a második oszlop")
    modo = st.radio(
        "Melyik mód az elsődleges?",
        ('Vizuális', 'Auditív', 'Tapintható')
    )


st.subheader("Modalidad seleccionada:")
st.success(modo)


if modo == "Tapintható":
    imagen2 = Image.open('CHRIS FROM TINDER TEMU.jpeg')
    st.image(imagen2, caption="Modo Haptico Activado")
    st.info("Simulación de respuesta háptica activada")

st.subheader("Gombok használata")
if st.button('nyomja meg a gombot'):
    st.write('Köszönöm a nyomást')
else:
    st.write('PRESIONA EL BOTON')


st.subheader("SelectBox")
in_mod = st.selectbox(
    "აირჩიეთ მოდალობა",
    ("Audio", "Visual", "Haptico")
)

st.write("Seleccionaste:", in_mod)


if in_mod == "Haptico":
    st.warning("Modo háptico secundario activado")
