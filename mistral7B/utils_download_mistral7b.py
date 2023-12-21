import os
from huggingface_hub import hf_hub_download


def download_model_files(model_id, model_revision=None, save_path='model_files'):
    os.makedirs(save_path, exist_ok=True)
    # List of files to download
    mistral_7b_files = [
        "config.json",
        "generation_config.json",
        "model-00001-of-00002.safetensors",
        "model-00002-of-00002.safetensors",
        "model.safetensors.index.json",
        "pytorch_model-00001-of-00002.bin",
        "pytorch_model-00002-of-00002.bin",
        "pytorch_model.bin.index.json",
        "special_tokens_map.json",
        "tokenizer.json",
        "tokenizer.model",
        "tokenizer_config.json"
    ]

    for file_name in mistral_7b_files:
        file_path = hf_hub_download(repo_id=model_id, filename=file_name, revision=model_revision)
        os.rename(file_path, os.path.join(save_path, file_name))
        print(f"Downloaded {file_name}")

    print("All files downloaded successfully.")


model_id = "mistralai/Mistral-7B-v0.1"
download_model_files(model_id)
