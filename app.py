import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

@st.cache_resource
def load_brain_tumor_model():
    model = load_model("best_model.keras")
    return model

model = load_brain_tumor_model()

CLASS_NAMES = ['Glioma', 'Meningioma', 'No Tumor', 'Pituitary']


st.set_page_config(page_title="Brain Tumor Detection", page_icon="🧠", layout="centered")

st.title("🧠 Brain Tumor Detection using CNN")
st.markdown(
    """
    Upload an MRI image to detect whether the brain has a **Glioma**, **Meningioma**, **Pituitary tumor**, or **No Tumor**.  
    *(Model trained on combined Figshare, SARTAJ, and Br35H datasets)*.
    """
)

uploaded_file = st.file_uploader("📤 Upload an MRI Image (JPG/PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display uploaded image
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded MRI Image", use_container_width=True)

    img_resized = img.resize((150, 150)) 
    img_array = image.img_to_array(img_resized)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0  # normalize

    # Prediction
    prediction = model.predict(img_array)
    predicted_class = CLASS_NAMES[np.argmax(prediction)]
    confidence = np.max(prediction) * 100


    st.subheader("🩺 Prediction Results")
    st.write(f"**Predicted Class:** {predicted_class}")
    st.write(f"**Confidence:** {confidence:.2f}%")

    # Color-based result
    if predicted_class == "No Tumor":
        st.success("✅ The model predicts **No Tumor**. MRI looks normal.")
    else:
        st.error(f"⚠️ The model predicts **{predicted_class} Tumor**. Please consult a radiologist.")

st.markdown("---")
st.markdown(
    "<p style='text-align: center;'>Developed using TensorFlow + Streamlit • Model: CNN trained on 7023 MRI images</p>",
    unsafe_allow_html=True
)
