import os
import base64
import streamlit as st

from utils import save_upload_file, delete_file, download_model
from models.yolov10.detector import inference
from config.model_config import Detector_Config
from components.streamlit_footer import footer

@st.cache_data(max_entries=1000)
def process_inference(image_path):
    result_img = inference(
        image_path,
        weight_path=Detector_Config().weight_path
    )

    return result_img

def main():
    st.set_page_config(
        page_title="YOLOv10 Detection Demo - AI VIETNAM",
        page_icon='static/aivn_favicon.png',
        layout="wide"
    )

    col1, col2 = st.columns([0.8, 0.2], gap='large')
    
    with col1:
        st.title(':sparkles: :blue[YOLOv10] Detection Demo')
        st.text('Model: Pre-trained YOLOv10n')

    with col2:
        logo_img = open("static/aivn_logo.png", "rb").read()
        logo_base64 = base64.b64encode(logo_img).decode()
        st.markdown(
            f"""
            <a href="https://aivietnam.edu.vn/">
                <img src="data:image/png;base64,{logo_base64}" width="full">
            </a>
            """,
            unsafe_allow_html=True,
        )

    uploaded_img = st.file_uploader('__Input your image__', type=['jpg', 'jpeg', 'png'])
    example_button = st.button('Run example')

    st.divider()

    if example_button:
        result_img = process_inference('static/example_img.jpg')
    elif uploaded_img:
        result_img = process_inference(uploaded_img)
    else:
        result_img = None

    if result_img is not None:
        st.markdown('**Detection result**')
        st.image(result_img)

    footer()


if __name__ == '__main__':
    if not os.path.exists(Detector_Config.weight_path):
        download_model()
    main()