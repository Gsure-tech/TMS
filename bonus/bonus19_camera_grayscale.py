import streamlit as st
from PIL import Image


upload_image = st.file_uploader("UploadImage")
with st.expander("Start Camera"):


    # Start the camera
    camera_image = st.camera_input("Camera")


if camera_image:
    # Create a pillow image instance
    img = Image.open(camera_image)
    # Convert the pillow image to grayscale
    gray_img = img.convert("L")
    # Render the grayscale image on the webpoage
    st.image(gray_img)

if upload_image:
    img = Image.open(upload_image)
    gray_uploaded_img = img.convert("L")
    st.image(gray_uploaded_img)