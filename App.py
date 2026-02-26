import streamlit as st
from PIL import Image

st.title("CHRIS FROM TINDER HAS AWAKEN")

st.header("Esta pagina es de prueba para FRAMEMOGGING")
st.write("CLAV GOT MOGGED BY A ASU FRAT LEADER")

image = Image.open('ARCANGEL_ABUSADOL.jpg')
st.image(image,caption='Interfaces Multimodales')

TEXTO = st.text_input('eSCRIbe AlGo')
st.write('eL TexTO EsCRito es',texto)

st.subheader("AHoRa UsARemos DoS CoLUMnas")

with col1:
  st.subheader("TEz az első oszlop")
  st.write("A multimodális interfészek javítják a felhasználói élményt")
  resp = st.checkbox('Estoy de Acuerdo')

with col2:
  st.subheader("Ez a második oszlop")
  modo = st.radio("Melyik mód az elsődleges a kezelőfelületeden?", ('Vizuális','Auditív','Tapintható'))
  if modo == 'Vizuális':
    st.write('A vizuális megjelenés alapvető fontosságú a felhasználói felület szempontjából.')
  if modo =='Auditív':
    st.write('A hallás alapvető fontosságú a felhasználói felületen')
  if modo == 'Tapintható':
    st.write('Az érintés elengedhetetlen a kezelőfelületben')
    Image.open('CHRIS FROM TINDER TEMU.jpeg')
