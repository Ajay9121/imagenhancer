import os

class Config:
    # Base directory
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # Storage paths
    INPUT_DIR = os.path.join(BASE_DIR, "storage", "input")
    OUTPUT_DIR = os.path.join(BASE_DIR, "storage", "output")

    # Allowed image formats
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}

    # Max upload size (25 MB)
    MAX_CONTENT_LENGTH = 25 * 1024 * 1024

    # Flask settings
    DEBUG = True
