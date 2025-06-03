import json

# Load symptom-to-disease knowledge base
with open("disease_info.json") as f:
    disease_info = json.load(f)

def get_disease_by_symptom(symptom_text):
    text = symptom_text.lower()
    for disease, data in disease_info.items():
        for keyword in data['symptoms']:
            if keyword in text:
                return disease
    return "Unknown"
