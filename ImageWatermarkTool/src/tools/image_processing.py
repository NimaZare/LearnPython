import cv2

def add_opencv_text_watermark(input_image_path, output_image_path, watermark_text, font_scale, color, thickness, position):
    img = cv2.imread(input_image_path)
    
    (text_width, text_height), baseline = cv2.getTextSize(watermark_text, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)

    if position == "bottom_right":
        x = img.shape[1] - text_width - 10
        y = img.shape[0] - text_height - baseline - 10

    cv2.putText(img, watermark_text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, color, thickness, cv2.LINE_AA)
    cv2.imwrite(output_image_path, img)

    print(f"\n==> Watermarked image saved successfully\n\n")
