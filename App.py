import streamlit as st
from PIL import Image

st.title("CHRIS FROM TINDER HAS AWAKEN")

st.header("Esta pagina es de prueba para FRAMEMOGGING")
st.write("CLAV GOT MOGGED BY A ASU FRAT LEADER")


image = Image.open('ARCANGEL_ABUSADOL.jpg')
st.image(image, caption='Interfaces Multimodales')


texto = st.text_input('eSCRIbe AlGo')
st.write('eL TexTO EsCRito es:', texto)

st.subheader("AHoRa UsARemos DoS CoLUMnas")


col1, col2 = st.columns(2)

with col1:
    st.subheader("TEz az első oszlop")
    st.write("A multimodális interfészek javítják a felhasználói élményt")
    resp = st.checkbox('Estoy de Acuerdo')

with col2:
    st.subheader("Ez a második oszlop")
    modo = st.radio(
        "Melyik mód az elsődleges a kezelőfelületeden?",
        ('Vizuális', 'Auditív', 'Tapintható')
    )

    if modo == 'Vizuális':
        st.write('A vizuális megjelenés alapvető fontosságú a felhasználói felület szempontjából.')

    elif modo == 'Auditív':
        st.write('A hallás alapvető fontosságú a felhasználói felületen')

    elif modo == 'Tapintható':
        st.write('Az érintés elengedhetetlen a kezelőfelületben')
        imagen2 = Image.open('CHRIS FROM TINDER TEMU.jpeg')
        st.image(imagen2, caption='Modo táctil activado')

st.subheader"Gombok használata")
if st.button('nyomja meg a gombot'):
    st.write('Köszönöm a nyomást')
else:
    st.write('PRESIONA EL BOTON')
