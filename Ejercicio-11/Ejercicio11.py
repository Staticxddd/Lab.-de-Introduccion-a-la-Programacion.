import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="Escaner de QR", layout="centered")

st.header("Escaner de Codigos")

foto = st.camera_input("Captura una imagen")

if foto:
    imagen = Image.open(foto).convert("RGB")
    frame = np.array(imagen)

    lector = cv2.QRCodeDetector()
    resultado, puntos, _ = lector.detectAndDecode(frame)

    st.image(imagen, caption="Imagen capturada", use_container_width=True)

    if resultado:
        st.info("Codigo encontrado")
        st.code(resultado)
    else:
        st.error("No se encontro ningun codigo o QR")