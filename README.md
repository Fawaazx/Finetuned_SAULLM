# Fine-Tunined SaulLM for Indian Legal AI Applications

## Description
This project involves fine-tuning SaulLM, a legal language model (LLM), on two distinct tasks: semantic segmentation and legal statute identification. The fine-tuning process utilizes an Indian legal data corpus to enhance the model's performance on these tasks. Additionally, a Flask app has been developed to demonstrate and interact with the fine-tuned models.

## Getting Started

### Prerequisites
- Python 3.9 or above
- Required Python packages:
  - Flask
  - llama_cpp
  - huggingface_hub
  - os
  - shutil

### Installation
1. Clone the repository
   ```bash
   git clone https://github.com/Fawaazx/Finetuned_SAULLM.git
   cd your-repository
## Setup Instructions

### Step 1: Run `model_download.py`

First, you need to download the necessary models by running the `model_download.py` script. This script will handle downloading and setting up all required models for the project.

\`\`\`bash
python model_download.py
\`\`\`

### Step 2: Run `app.py`

Once the models have been successfully downloaded, you can start the application by running the `app.py` script.

\`\`\`bash
python app.py
\`\`\`

## Additional Information

- Ensure you have all the dependencies installed before running the scripts. You can install them using:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

- If you encounter any issues, please check the logs for error messages and verify that all dependencies are correctly installed.

## Contact

For any questions or issues, please contact Fawazzx at mohammedfawaz398@gmail.com.
