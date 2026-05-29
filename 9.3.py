from PIL import Image, ImageFilter
import os

os.makedirs("image2", exist_ok=True)

filtr = input("Выберите фильтр: \n 1) Контур \n 2) Детализация \n 3) Поиск краев \n 4)Тиснение \n 5)Повышение резкости \n")
image = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]

for i in image:
    img = Image.open(f"image1/{i}")

    if filtr == "1":
        filtered = img.filter(ImageFilter.CONTOUR)
    elif filtr == "2":
        filtered = img.filter(ImageFilter.DETAIL)
    elif filtr == "3":
        filtered = img.filter(ImageFilter.FIND_EDGES)
    elif filtr == "4":
        filtered = img.filter(ImageFilter.EMBOSS)
    else:
        filtered = img.filter(ImageFilter.SHARPEN)

    filtered.save(f"image2/filtered_{i}")