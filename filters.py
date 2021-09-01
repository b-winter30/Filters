import numpy as np
from PIL import Image, ImageFilter, ImageTk
import pandas as pd

import matplotlib.pyplot as plt
size = 250, 250
def median_filter(url, filter_size):
    im = Image.open(url)
    im1 = im.filter(ImageFilter.MedianFilter(size=filter_size))
    photo = ImageTk.PhotoImage(im1)
    return photo

def bilateral_filter(url):
    return None
def non_local_means_filter(url):
    return None
def morphological_filter(url):
    return None
def fill_holes(image):  
    return None
