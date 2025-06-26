# Blip-image-captioning
A simple and effective Python script using the BLIP model (Salesforce/blip-image-captioning-base) for generating captions for images. The script processes all images in a specified folder and prints their auto-generated descriptions using Hugging Face Transformers and PyTorch.
Create a file named `README.md` with the following content:
# 🖼️ BLIP Image Captioning

This project demonstrates the use of the [BLIP model](https://huggingface.co/Salesforce/blip-image-captioning-base) from Hugging Face Transformers to generate natural language captions for images.

## 💡 Overview

Using BLIP (Bootstrapped Language-Image Pretraining), this script processes all images in a specified folder and outputs relevant captions. It is ideal for quick captioning experiments or integrating image understanding into other applications.

## ✨ Features
- 🤖 BLIP image captioning model by Salesforce
- ⚡ PyTorch GPU acceleration
- 📂 Directory-based batch image processing
- 🔄 Automatic caption generation

## 🚀 How to Use
1. Install dependencies:
    pip install transformers torch pillow
   
2. Set your image directory path in the script:
    image_dir = "your/image/folder/path"
   
3. Run the script:
    python BLIP.py
 
## 🖼️ Output Example
cat.jpg → A cat sitting on a sofa
sunset.jpg → A beautiful sunset over the mountains

## 📁 Folder Structure
blip-image-captioning/
├── BLIP.py
├── Images/
├── README.md
└── requirements.txt
