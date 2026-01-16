from app.ai.model import run_model

if __name__ == "__main__":
    input_image_path = "app/storage/input/test.png"
    output = run_model(input_image_path)

    print("✅ Done")
    print("Output saved at:", output)
