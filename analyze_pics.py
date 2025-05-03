import torch
from torchvision import models, transforms
from PIL import Image
import os

# Load the magic glasses (pre-trained ViT)
model = models.vit_b_16(pretrained=True)
model.eval()  # Set to "look" mode

# Prepare pictures for the glasses
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # Make picture the right size
    transforms.ToTensor(),  # Turn picture into numbers
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # Adjust colors
])

# Load a list of labels (like "sneaker," "cake")
with open("imagenet_labels.txt", "r") as f:
    labels = [line.strip() for line in f.readlines()]  # You’ll need this file!

# Look at each picture
for pic in os.listdir("trending_pics"):
    img_path = os.path.join("trending_pics", pic)
    img = Image.open(img_path).convert("RGB")
    img_t = transform(img)
    batch_t = torch.unsqueeze(img_t, 0)  # Get ready for ViT

    # Ask ViT what it sees
    with torch.no_grad():
        output = model(batch_t)
    probs = torch.nn.functional.softmax(output[0], dim=0)
    top_prob, top_idx = torch.max(probs, dim=0)
    print(f"Picture {pic} is probably a {labels[top_idx]} (confidence: {top_prob.item():.2f})")