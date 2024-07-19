import streamlit as st
from paddleocr import PaddleOCR
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import cv2

# Helper function to draw OCR results
def draw_ocr(image, boxes, txts, scores):
    image = image.copy()
    for (box, txt, score) in zip(boxes, txts, scores):
        box = np.array(box).astype(np.int32).reshape(-1, 2)
        cv2.polylines(image, [box], True, color=(0, 255, 0), thickness=2)
        for pt in box:
            cv2.putText(image, txt, (pt[0], pt[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
    return image

# Title of the app
st.title('PaddleOCR Text Detection and Recognition')

# File uploader for the image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Displaying the image
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption='Uploaded Image.', use_column_width=True)

    # Convert the image to numpy array
    img = np.array(img)

    # Initialize PaddleOCR
    ocr = PaddleOCR(use_angle_cls=True, lang='en')

    # Perform OCR
    result = ocr.ocr(img, cls=True)

    # Extract and display results
    boxes = []
    texts = []
    scores = []

    for line in result:
        for res in line:
            boxes.append(res[0])
            texts.append(res[1][0])
            scores.append(res[1][1])

    # Display OCR results
    for i, text in enumerate(texts):
        st.write(f"Text: {text}, Score: {scores[i]}")

    # Draw annotations on the image
    annotated_image = draw_ocr(img, boxes, texts, scores)
    st.image(annotated_image, caption='Annotated Image.', use_column_width=True)

    # Display image shape
    st.write("Image shape:", img.shape)
