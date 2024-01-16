import streamlit as st
from streamlit_extras.let_it_rain import rain
from streamlit_extras.colored_header import colored_header
from page_utils import font_modifier, display_image


################### HEADER SECTION #######################
display_image.display_image('https://cdn-images-1.medium.com/max/800/0*vBDO0wwrvAIS5e1D.png')

st.markdown("<h1 style='text-align: center; color: #F5EFE6;'>Mapping Seagrass Meadows with Satellite Imagery and Computer Vision</h1>",
            unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #FFFFD0; font-family: Segoe UI;'>A web-based pixel-level Classification Model for identifying seagrass in sattelite images</h3>", unsafe_allow_html=True)

display_image.display_image('https://upload.wikimedia.org/wikipedia/commons/4/45/Sanc0209_-_Flickr_-_NOAA_Photo_Library.jpg')


################### FILE UPLOAD SECTION #######################
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])





font_modifier.make_font_poppins()