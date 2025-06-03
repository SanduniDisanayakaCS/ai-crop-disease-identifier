import streamlit as st
from model_image import predict_disease
from model_symptom import get_disease_by_symptom, disease_info

st.set_page_config(page_title="AI Crop Disease Identifier", layout="centered")

# 🌿 Title with custom style
st.markdown(
    "<h1 style='text-align: center; color: #2E8B57;'>🌱 AI Crop Disease Identifier</h1>",
    unsafe_allow_html=True
)

st.markdown("---")

# 📷 Upload section
st.markdown("### 📤 Upload Plant Leaf Image")
img_file = st.file_uploader("Drag & drop or browse a .jpg/.png image", type=["jpg", "png"])

# 📝 Symptom input section
st.markdown("### 🧾 Enter Observed Symptoms")
symptom_text = st.text_input("e.g., yellow halos with brown spots", placeholder="Describe the symptoms here...")

# 🔍 Analysis button
if st.button("🔍 Analyze", use_container_width=True):
    if img_file and symptom_text:
        with open("temp.jpg", "wb") as f:
            f.write(img_file.read())

        image_diagnosis = predict_disease("temp.jpg")
        symptom_diagnosis = get_disease_by_symptom(symptom_text)

        final_disease = image_diagnosis if image_diagnosis == symptom_diagnosis else symptom_diagnosis
        info = disease_info.get(final_disease, {})

        st.markdown("---")
        st.markdown(f"<h3 style='color:#1E90FF;'>🦠 Disease Detected: {final_disease}</h3>", unsafe_allow_html=True)

        st.markdown(f"""
        <div style='background-color:#f2f2f2; padding:15px; border-radius:10px'>
        <strong>🧪 Treatment:</strong> {info.get('treatment', 'N/A')}<br>
        <strong>⚠️ Risk Level:</strong> <span style='color:orange'>{info.get('risk', 'Unknown')}</span>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error("Please upload an image and enter symptom details.")

# 🔚 Footer
st.markdown("<br><hr style='border:1px solid #ddd'><p style='text-align:center;color:#aaa;'>© 2025 Unsungfields AI • Crop Health AI Assistant</p>", unsafe_allow_html=True)
