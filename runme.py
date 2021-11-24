message = 'hello, world'


print(message)

from mss import mss
from PIL import Image
mon = {'left': 0, 'top': 0, 'width': 1920, 'height': 1200}

with mss() as sct:
    screenShot = sct.grab(mon)
    img = Image.frombytes(
        'RGB', 
        (screenShot.width, screenShot.height), 
        screenShot.rgb, 
    )
    pixel_access = img.load()
    random_pixel = pixel_access[23, 45]

    print(random_pixel)
    
    #img.save('C:\\temp\\scheenshot.png')
