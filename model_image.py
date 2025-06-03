import random

classes = ['Healthy', 'Cercospora Leaf Spot', 'Rust', 'Blight']

def predict_disease(img_path):
    # Simulate prediction by returning a random disease
    return random.choice(classes)

