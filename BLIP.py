from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch
import os

# Load BLIP processor and model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
model.eval()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Directory containing images (change this path)
image_dir = "C:\\Users\\Hp\\CascadeProjects\\vision_transformer\\BLIP\\Images"
image_files = [os.path.join(image_dir, f) for f in os.listdir(image_dir) if f.lower().endswith((".jpg", ".png", ".jpeg"))]

# Print image name and caption
print("\n📷 Image Captions:")
for img_path in image_files:
    image = Image.open(img_path).convert("RGB")
    inputs = processor(images=image, return_tensors="pt").to(device)
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=30)
    caption = processor.decode(outputs[0], skip_special_tokens=True)
    print(f"{os.path.basename(img_path)} → {caption}")
