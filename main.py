from tkinter import *
from PIL import Image, ImageFont, ImageDraw
import time

filepath1 = ''
filepath2 = ''

def save():
    global filepath1, filepath2
    filepath1 = image_input.get()
    filepath2 = watermark_input.get()
    filepath3 = watermark_text_input.get()

    text_font = ImageFont.truetype("arial.ttf", 24)

    time.sleep(2)
    image_py = Image.open(filepath1)
    image_py = image_py.resize((512, 512))
    width = image_py.size[0]
    height = image_py.size[1]

    image_dog = Image.open(filepath2)
    adjust_x = image_dog.size[0]
    adjust_y = image_dog.size[1]/2

    coord_x = int(width/2 - adjust_x)
    coord_y = int(height/2 - adjust_y)

    text_coord_x = int(width / 2)
    text_coord_y = int(height / 2)

    image_py.paste(image_dog, (coord_x, coord_y))
    edit_image = ImageDraw.Draw(image_py)
    edit_image.text((text_coord_x, text_coord_y), filepath3, ("white"), font=text_font)
    image_py.show()



FILE1 = 'static/images/python-logo.png'
FILE2 = 'static/images/dog_pic.jpeg'

window = Tk()
window.title('Watermark Creator')
window.config(padx=25, pady=25)

warning = Label(text='**Warning: the image and watermark to be used should be sized to the preferred dimensions beforehand.\n'
                     'Watermark logos and text will be added to the center of the given image.**')
warning.grid(column=0, row=0, columnspan=2)
image = Label(text='Image filepath:')
image.grid(column=0, row=1)
watermark = Label(text='Watermark filepath:')
watermark.grid(column=0, row=2)
watermark_text = Label(text='Watermark text:')
watermark_text.grid(column=0, row=3)
create_watermark = Button(text='Create', command=save)
create_watermark.grid(column=0, row=4)

image_input = Entry(width=60)
image_input.grid(column=1, row=1)
watermark_input = Entry(width=60)
watermark_input.grid(column=1, row=2)
watermark_text_input = Entry(width=60)
watermark_text_input.grid(column=1, row=3)

window.mainloop()

