# import os
# import torch
# import numpy as np
# from PIL import Image
# from app.config import Config
#
# from basicsr.archs.rrdbnet_arch import RRDBNet
# from realesrgan import RealESRGANer
#
# def run_model(input_path: str) -> str:
#     # Absolute input path
#     input_path = os.path.abspath(input_path)
#
#     # 🔥 Anime model weights
#     model_path = os.path.abspath("weights/RealESRGAN_x4plus_anime_6B.pth")
#     if not os.path.exists(model_path):
#         raise FileNotFoundError("RealESRGAN_x4plus_anime_6B.pth not found")
#
#     # Device
#     device = "cuda" if torch.cuda.is_available() else "cpu"
#
#     # 🔥 Anime-specific architecture (MANDATORY)
#     model = RRDBNet(
#         num_in_ch=3,
#         num_out_ch=3,
#         num_feat=64,
#         num_block=6,      # IMPORTANT
#         num_grow_ch=32,
#         scale=4
#     )
#
#     # RealESRGAN runner
#     upsampler = RealESRGANer(
#         scale=4,
#         model_path=model_path,
#         model=model,
#         tile=0,           # use 256 if low RAM
#         tile_pad=10,
#         pre_pad=0,
#         half=(device == "cuda"),
#         device=device
#     )
#
#     # Load image
#     img = Image.open(input_path).convert("RGB")
#     img_np = np.array(img)
#
#     # Enhance
#     output, _ = upsampler.enhance(img_np, outscale=4)
#
#     # Save output
#     os.makedirs(Config.OUTPUT_DIR, exist_ok=True)
#     output_path = os.path.join(
#         Config.OUTPUT_DIR,
#         os.path.basename(input_path)
#     )
#
#     Image.fromarray(output).save(output_path, quality=95)
#
#     return output_path







import os
import torch
import numpy as np
from PIL import Image
from app.config import Config

from basicsr.archs.rrdbnet_arch import RRDBNet
from realesrgan import RealESRGANer

# -----------------------------
# 🔥 LOAD MODEL ONCE (IMPORTANT)
# -----------------------------

device = "cuda" if torch.cuda.is_available() else "cpu"

model_path = os.path.abspath("weights/RealESRGAN_x4plus.pth")
if not os.path.exists(model_path):
    raise FileNotFoundError("RealESRGAN_x4plus.pth not found")

model = RRDBNet(
    num_in_ch=3,
    num_out_ch=3,
    num_feat=64,
    num_block=23,
    num_grow_ch=32,
    scale=4
)

upsampler = RealESRGANer(
    scale=4,
    model_path=model_path,
    model=model,
    tile=256,              # ✅ VERY IMPORTANT
    tile_pad=10,
    pre_pad=0,
    half=(device == "cuda"),
    device=device
)

print("✅ Real-ESRGAN model loaded once")

# -----------------------------
# API FUNCTION (FAST)
# -----------------------------
def run_model(input_path: str) -> str:
    input_path = os.path.abspath(input_path)

    img = Image.open(input_path).convert("RGB")

    # 🔥 OPTIONAL: resize huge images
    if img.width > 2000:
        img = img.resize((img.width // 2, img.height // 2))

    img_np = np.array(img)

    output, _ = upsampler.enhance(img_np, outscale=4)

    os.makedirs(Config.OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(
        Config.OUTPUT_DIR,
        os.path.basename(input_path)
    )

    Image.fromarray(output).save(output_path, quality=95)
    return output_path

