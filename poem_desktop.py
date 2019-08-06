### Ubuntu background: https://gist.github.com/mtrovo/1110370
### Create image: Gabor Szabo post on Code Maven
### Poem on github repo: chinese-poetry/chinese-poetry

import urllib.request
import json
import random
from PIL import Image, ImageDraw, ImageFont
import os

absolute_path = os.path.dirname(os.path.abspath(__file__))

def get_poem():
    
    with urllib.request.urlopen("https://raw.githubusercontent.com/bz247/chinese-poetry/master/json/poet.song.{}000.json".format(random.randint(0, 99))) as url:
        ### Forked from chinese-poetry/chinese-poetry
        data = json.loads(url.read().decode())
        poem = data[random.randint(0, len(data))]

        return poem
        
def create_image(poem, img_path):
    
    img = Image.new('RGB', (2560, 1440), color=(0, 0, 0))
    d = ImageDraw.Draw(img)

    author = poem['author']
    title = poem['title']
    paragraphs = poem['paragraphs']

    font = ImageFont.truetype(absolute_path+'/simsun.ttc', 32)
    d.text((1000, 100), title, font=font, fill=(255, 255, 255))
    d.text((1000, 200), author, font=font, fill=(255, 255, 255))
    for line in range(len(paragraphs)):
        d.text((1000, 400+100*line), paragraphs[line], font=font, fill=(255, 255, 255))

    img.save(img_path)

if __name__ == '__main__':
    poem = get_poem()

    img_path = absolute_path + '/poem.png'
    #img_path = '/home/bingyu/Documents/poem_desktop/poem.png'
    create_image(poem, img_path)