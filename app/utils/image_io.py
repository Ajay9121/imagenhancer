import os
from app.config import Config

def save_input_image(file, filename):
    os.makedirs(Config.INPUT_DIR, exist_ok=True)
    input_path = os.path.join(Config.INPUT_DIR, filename)
    file.save(input_path)
    return input_path
