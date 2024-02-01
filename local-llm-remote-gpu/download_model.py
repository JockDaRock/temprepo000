from gpt4all import GPT4All
import os

def download_model(model_name):
    # Initialize the model
    model = GPT4All(model_name=model_name)

    # Trigger the download
    model.download_model(model_filename=model_name, model_path='./')

if __name__ == "__main__":
    # Specify the model name
    # model_name = 'orca-mini-3b-gguf2-q4_0.gguf'
    model_name = os.getenv('MODEL')

    # Download the model
    download_model(model_name)

    print(f"Model {model_name} downloaded successfully.")