# 🌱 AI Crop Disease Identifier (Image + Text Hybrid)

An intelligent Streamlit-based web application that helps farmers and agronomists identify plant diseases using a **hybrid AI approach** — combining leaf image classification and natural language symptom analysis.

---

## 🚀 Features

- 📷 Upload a leaf image (JPG/PNG)
- ✍️ Enter observed symptoms (e.g., "yellow halos, brown lesions")
- 🧠 Uses a simulated or trained CNN model for image-based diagnosis
- 📚 Matches symptoms to diseases using rule-based logic or LLM
- 💊 Provides treatment advice and shows risk level

---

## 🛠 Tech Stack

- **Frontend/UI**: Streamlit  
- **Image Classification**: TensorFlow (Mock or `.h5` model)  
- **Text Matching**: Symptom keyword logic (GPT ready)  
- **Styling**: HTML + Emoji + Container UI enhancements

---

## 📂 Folder Structure

crop-disease-app/
├── app.py # Main Streamlit interface
├── model_image.py # Image prediction (mock or model)
├── model_symptom.py # Symptom-to-disease matcher
├── utils.py # Reserved for future enhancements
├── disease_info.json # Knowledge base (symptoms, treatments)
├── models/ # Trained CNN model (.h5)
├── sample_leaf.jpg # Test image
├── requirements.txt
└── README.md


---

## 🧪 How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py

If TensorFlow fails (Python 3.13 issue), you can use the included mock model to simulate predictions.

📊 Sample Output
Disease: Cercospora Leaf Spot
Treatment: Apply chlorothalonil or copper-based fungicides
Risk Level: Moderate

🔮 Future Enhancements

✅ Integrate real CNN .h5 trained on PlantVillage
🤖 Use OpenAI GPT for advanced symptom understanding
🌐 Add real-time location-based risk mapping
📱 Mobile camera upload interface
🌍 Multi-language support (Sinhala, Tamil, Hindi)

