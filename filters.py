import numpy as np
import cv2
from skimage import img_as_float, color, io
from PIL import Image, ImageFilter, ImageTk
import pandas as pd
import matplotlib.pyplot as plt
size = 250, 250
def median_filter(url, filter_size):
    im = Image.open(url)
    im1 = im.filter(ImageFilter.MedianFilter(size=filter_size))
    photo = ImageTk.PhotoImage(im1)
    return photo

def check_grayscale(url):
    img = Image.open(url).convert('RGB')
    w, h = img.size
    for i in range(w):
        for j in range(h):
            r, g, b = img.getpixel((i,j))
            if r != g != b:
                return False
    return True

def bilateral_filter(url):
    img = cv2.imread(url)
    bilateral = cv2.bilateralFilter(img, 15, 75, 75)
    photo = ImageTk.PhotoImage(image=Image.fromarray(bilateral))
    return photo

def non_local_means_filter(url):
    if check_grayscale(url):
        img = cv2.imread(url)
        nlmeans = cv2.fastNlMeansDenoising(img, None, 20, 7, 21)
    else:
        img = cv2.imread(url)
        nlmeans = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
    photo = ImageTk.PhotoImage(image=Image.fromarray(nlmeans))
    return photo
def morphological_filter(url):
    return None
def fill_holes(image):  
    return None
