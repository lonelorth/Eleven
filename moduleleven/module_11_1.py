import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter




print('-----------------------------------------------------------------------')

class Panda:
    # загрузка данных
    data = pd.read_fwf(r'D:\python\moduleleven\Readme')

    # первые 5 строк данных
    print(data.head())

print('-----------------------------------------------------------------------')

class Numpy:
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # массив
    sum = np.sum(arr)   # суммируем
    flip = np.flip(arr) # переворачиваем массив

    print(arr)
    print(sum)
    print(flip)

print('-----------------------------------------------------------------------')

class Matplotlib:
    x = [5, 4, 3, 2, 1]         # задаем данные по осям
    y = [10, 20, 15, 25, 30]

    plt.plot(x, y)         # линейный график
    plt.xlabel('ось X')
    plt.ylabel('ось Y')
    plt.title('Пример линейного графика')
    plt.show()

print('-----------------------------------------------------------------------')

class Pillow:
    image = Image.open(r'D:\python\moduleleven\auto.jpg')
    resized_image = image.resize((800, 600))  # изменение размера
    resized_image.save('resized_image.jpg')


    blurred_image = image.filter(ImageFilter.BLUR)  # эффекты
    blurred_image.save('blurred_image.jpg')

    # другой формат
    image.save('converted_image.jpg')  # JPEG
    image.save('converted_image.gif')  # GIF
print('photo')
print('-----------------------------------------------------------------------')