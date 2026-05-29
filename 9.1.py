from PIL import Image

image = Image.open('забыл.jpg')

print(f"Width: {image.size}")
print(f"Format: {image.format}")
print(f"Color: {image.mode}")

image.show()