from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename
from app.services.enhancer import enhance_image

enhance_api = Blueprint("enhance_api", __name__)

def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower()
        in current_app.config["ALLOWED_EXTENSIONS"]
    )

@enhance_api.route("/enhance", methods=["POST"])
def enhance():
    if "image" not in request.files:
        return jsonify({"error": "No image file found"}), 400

    file = request.files["image"]

    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": "Unsupported file format"}), 400

    filename = secure_filename(file.filename)
    result_path = enhance_image(file, filename)

    return jsonify({
        "status": "success",
        "output_image": result_path
    }), 200
