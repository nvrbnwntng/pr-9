from PIL import Image

watermark = Image.open("watermark.png").convert("RGBA")

image = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]

for i in image:
    back = Image.open(f"image1/{i}").convert("RGBA")
    combined = back.copy()
    position = (30, 30)
    combined.paste(watermark, position, watermark)
    combined_rgb = combined.convert("RGB")
    combined_rgb.save(f"image2_w{i}", quality=95)