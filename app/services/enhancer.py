from app.utils.image_io import save_input_image
from app.ai.model import run_model

def enhance_image(file, filename):
    """
    Controls the full AI enhancement flow
    """

    # Save uploaded image
    input_path = save_input_image(file, filename)

    # Run AI model
    output_path = run_model(input_path)

    return output_path
