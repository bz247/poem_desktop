### Ubuntu background: https://gist.github.com/mtrovo/1110370
### Create image: Gabor Szabo post on Code Maven
### Poem on github repo: https://github.com/chinese-poetry/chinese-poetry

import urllib.request
import json
import random
from PIL import Image, ImageDraw, ImageFont
import os
import numpy as np 

absolute_path = os.path.dirname(os.path.abspath(__file__))

def get_idiom():
    
    with urllib.request.urlopen("https://raw.githubusercontent.com/pwxcoo/chinese-xinhua/master/data/idiom.json") as url:
        ### Forked from https://github.com/chinese-poetry/chinese-poetry
        data = json.loads(url.read().decode())
        idiom = data[random.randint(0, len(data))]

        return idiom
        
def create_image(poem, img_path):
    
    img = Image.new('RGB', (2560, 1440), color=(0, 0, 0))
    d = ImageDraw.Draw(img)

    word = idiom['word']
    pinyin = idiom['pinyin']
    explanation = idiom['explanation']
    derivation = idiom['derivation']
    example = idiom['example']

    font = ImageFont.truetype(absolute_path+'/simsun.ttc', 32)
    vertical_pos = 100
    d.text((800, vertical_pos), pinyin, font=font, fill=(255, 255, 255))
    vertical_pos += 50
    d.text((800, vertical_pos), word, font=font, fill=(255, 255, 255))
    vertical_pos += 100

    for line in range(int(np.ceil(len(explanation)/20))):
        d.text((800, vertical_pos), explanation[20*line:min(20*(line+1), len(explanation))], font=font, fill=(255, 255, 255))
        vertical_pos += 80

    vertical_pos += 80
    for line in range(int(np.ceil(len(derivation)/20))):
        d.text((800, vertical_pos), derivation[20*line:min(20*(line+1), len(derivation))], font=font, fill=(255, 255, 255))
        vertical_pos += 80

    vertical_pos += 80
    for line in range(int(np.ceil(len(example)/20))):
        d.text((800, vertical_pos), example[20*line:min(20*(line+1), len(example))], font=font, fill=(255, 255, 255))
        vertical_pos += 80

    img.save(img_path)

if __name__ == '__main__':
    idiom = get_idiom()

    img_path = absolute_path + '/idiom.png'
    create_image(idiom, img_path)