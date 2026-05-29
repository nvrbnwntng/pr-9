from PIL import Image

image = Image.open("забыл.jpg")

new_width = image.width // 3
new_height = image.height // 3

size_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

size_image.save("новый_размер.png")
image = Image.open("новый_размер.png")

flip = image.transpose(Image.FLIP_LEFT_RIGHT)
flip.save('по_горизонтали.png')

flip_image = image.transpose(Image.FLIP_TOP_BOTTOM)
flip_image.save('по_вертикали.png')

print("Изображения сохранены")