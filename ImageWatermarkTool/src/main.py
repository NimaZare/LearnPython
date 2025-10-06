import os
import uuid
import tools.image_processing as imgp

def main():
    print("\n********** Image Watermark Tool **********\n\n")
    img_path = input("Please enter the path to the image: ").strip('"').strip()
    watermark_text = input("Please enter the watermark text: ").strip()

    os.makedirs("src/output", exist_ok=True)
    img_save_path = os.path.join("src/output", f"watermarked_{uuid.uuid4().hex[:8]}.jpg")
    imgp.add_opencv_text_watermark(img_path, img_save_path, watermark_text, 0.9, (255, 255, 255), 2, "bottom_right")


if __name__ == "__main__":
    main()
