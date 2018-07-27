from PIL import Image, ImageDraw, ImageFont
import numpy as np


def construct_grid_image(data, name="sudoku.png", width=300, height=300, fontsize=12):
    img = Image.new('RGB', (width+1, height+1), color='white')

    d = ImageDraw.Draw(img)

    # Outline
    d.rectangle([(0,0), (width, height)], fill=None, outline='black' )

    # Boxes and numbers
    font_size = fontsize
    font = ImageFont.truetype('/Library/Fonts/arial.ttf', int(font_size))
    start_x, start_y = 0, 0
    n = 9
    for line in range(n):
        for col in range(n):

            # Boxes
            end_x, end_y = int(start_x+width/n), int(start_y+height/n)
            d.rectangle([(start_x, start_y), (end_x, end_y)], fill=None, outline = 'black')

            # Text
            center_x, center_y = (start_x+width/(2*n)), (start_y+height/(2*n)-font_size/2)
            text = str(int(data[line,col]))
            d.text((center_x, center_y), text, fill = 'black', font=font)

            start_x = end_x
        start_x = 0
        start_y += int(height/n)

    img.save(name)