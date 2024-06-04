# File path: download_gguf_models.py

# Step 1: Install the huggingface_hub library
# You can install it via pip if it's not already installed
# !pip install huggingface_hub

# Step 2: Import necessary libraries
from huggingface_hub import hf_hub_download
import os
import shutil

# Step 3: Define the function to download multiple models
def download_models(models, save_dir="model"):
    # Check if the "model" directory exists, if not, create it
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    # Download each model
    for model_id, model_file_name in models:
        try:
            # Download the model
            downloaded_file_path = hf_hub_download(repo_id=model_id, filename=model_file_name)
            
            # Save the model file in the "model" directory
            destination_path = os.path.join(save_dir, model_file_name)
            shutil.move(downloaded_file_path, destination_path)
            
            print(f"Model {model_id} downloaded and saved to {destination_path}")
        except Exception as e:
            print(f"Failed to download {model_id}: {e}")

# Step 4: List of models to download
models_to_download = [
    ("Fawazzx/SaulLM_semantic_finetuned-7b-v0.1.gguf", "SaulLM_semantic_finetuned-7b-v0.1.gguf"),
    ("Fawazzx/Finetuned-saulLM-7b-v1.5.gguf", "Finetuned-saulLM-7b-v1.5.gguf")  # Replace with your second model details
]

# Step 5: Call the download_models function with the list of models
download_models(models_to_download)