import streamlit as st
from PIL import Image

camera_image = st.camera_input("Camera")
print(camera_image)

img = Image.open(camera_image)