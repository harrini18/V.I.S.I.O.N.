import os
import numpy as np
from PIL import Image
import torch
from transformers import ViTFeatureExtractor, ViTForImageClassification
import warnings
warnings.filterwarnings("ignore")

# Paths
PICS_FOLDER = "trending_pics"
TRENDS_FILE = "trends.txt"
IMAGENET_LABELS_FILE = "imagenet_labels.txt"

# Load ViT model and feature extractor
feature_extractor = ViTFeatureExtractor.from_pretrained("google/vit-base-patch16-224")
model = ViTForImageClassification.from_pretrained("google/vit-base-patch16-224")
model.eval()

# Load ImageNet labels
with open(IMAGENET_LABELS_FILE, "r") as f:
    imagenet_labels = [line.strip() for line in f.readlines()]

# Load and preprocess images
image_paths = [os.path.join(PICS_FOLDER, f) for f in os.listdir(PICS_FOLDER) if f.endswith(('.jpg', '.jpeg', '.png'))]
labeled_images = []

for img_path in image_paths:
    try:
        img = Image.open(img_path).convert("RGB")
        img = img.resize((224, 224), Image.Resampling.LANCZOS)
        inputs = feature_extractor(images=img, return_tensors="pt")
        
        with torch.no_grad():
            outputs = model(**inputs)
            logits = outputs.logits
            predicted_label_idx = logits.argmax(-1).item()
            predicted_label = imagenet_labels[predicted_label_idx]
        
        labeled_images.append((os.path.basename(img_path), predicted_label))
    except Exception as e:
        print(f"Error processing {img_path}: {str(e)}")
        continue

# Write to trends.txt without grouping, ensuring a space after the dash
if labeled_images:
    with open(TRENDS_FILE, "w") as f:
        for filename, label in labeled_images:
            f.write(f"- {filename} (labeled as {label})\n")  # Added space after "-"
else:
    print("No images processed successfully.")