````markdown
# 🧠 Brain Tumor Detection using CNN

This project uses a **Convolutional Neural Network (CNN)** to detect brain tumors from MRI images.  
The model classifies images into **4 categories**:  
**Glioma**, **Meningioma**, **Pituitary**, and **No Tumor**.

---

## 📂 Dataset
The dataset used for training is available on Kaggle:  
👉 [Brain Tumor MRI Dataset](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset)

This dataset is a combination of:
- Figshare
- SARTAJ Dataset
- Br35H Dataset

---

## ⚙️ Tech Stack
- **TensorFlow / Keras**
- **Streamlit** (for frontend)
- **NumPy, Pillow**
- **Python 3.8+**

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/brain-tumor-detection.git
cd brain-tumor-detection
````

### 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate     # On Windows
# or
source venv/bin/activate  # On macOS/Linux
```

### 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the App

```bash
streamlit run app.py
```

---

## 🧩 Model Info

* File: `best_model.keras`
* Optimizer: Adam (lr = 0.001)
* Input size: 150x150
* Classes: 4
* Trained on ~7000 MRI images

---

## 📸 Demo

Upload an MRI image and the model will predict:

* ✅ **No Tumor**
* ⚠️ **Glioma**
* ⚠️ **Meningioma**
* ⚠️ **Pituitary**

---

## 🏁 Output Example

After uploading an MRI:

```
Predicted Class: Glioma
Confidence: 97.45%
```

---

## 🧑‍💻 Author

Developed by **Hero0P**

---
