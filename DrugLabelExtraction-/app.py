import streamlit as st
from paddleocr import PaddleOCR
import cv2
import numpy as np

# Initialize PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang='en')  # Download and load model into memory

# Title of the app
st.title("DETECT THE TEXTS: 👨‍⚕️ ")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Convert the file to an OpenCV image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)  # 1 means load color image in BGR format

    # Display the image
    st.image(image, channels="BGR", caption="Uploaded Image")

    # Perform OCR
    result = ocr.ocr(image, cls=True)

    # Extract text and bounding boxes
    boxes = [line[0] for line in result[0]]
    txts = [line[1][0] for line in result[0]]
    scores = [line[1][1] for line in result[0]]

    # Display results
    st.write("Detected Texts:")
    for (text, score) in zip(txts, scores):
        st.write(f"{text} (Confidence: {score:.2f})")

    # Draw results on the image
    image_with_boxes = image.copy()  # Make a copy of the original image
    ocr.draw_ocr(image_with_boxes, boxes, txts)  # Draw directly on the image

    # Convert the image to RGB (from BGR) for display with Streamlit
    image_with_boxes_rgb = cv2.cvtColor(image_with_boxes, cv2.COLOR_BGR2RGB)

    # Display the result image with bounding boxes
    st.image(image_with_boxes_rgb, caption="OCR Result")

# Instructions
st.write("Upload an image to perform OCR and display detected text along with bounding boxes.")
