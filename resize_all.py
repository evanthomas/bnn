#!/usr/bin/env python3

from PIL import Image
import os

base_dir = '/home/evan/neurosim/beedata'
img_dir = base_dir + '/fullsize'
resize_dir = base_dir + '/small'

def is_image(fn):
    _, ext = os.path.splitext(fn)

    return ext.upper() == '.JPG'


files = filter(is_image, os.listdir(img_dir))
for fn in files:
  img = Image.open(img_dir + "/" + fn)
  exif = img.info['exif']
  img = img.resize((1024, 768), Image.LANCZOS)
  img.save(resize_dir + '/' + fn, exif=exif)

