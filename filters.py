from autoencoder import change_dimension_and_add_to_dataset_and_run, run_main
import numpy as np
import cv2
from skimage import img_as_float, color, io
from PIL import Image, ImageFilter, ImageTk, ImageEnhance
import pandas as pd
import matplotlib.pyplot as plt
size = 250, 250
def median_filter(url, filter_size):
    basewidth = 150
    im = Image.open(url).convert('RGB')
    wpercent = (basewidth/float(im.size[0]))
    hsize = int((float(im.size[1])*float(wpercent)))
    im = im.resize((basewidth,hsize), Image.ANTIALIAS)
    im1 = im.filter(ImageFilter.MedianFilter(size=filter_size))
    return im1

def check_grayscale(url):
    basewidth = 150
    im = Image.open(url).convert('RGB')
    wpercent = (basewidth/float(im.size[0]))
    hsize = int((float(im.size[1])*float(wpercent)))
    im = im.resize((basewidth,hsize), Image.ANTIALIAS)
    w, h = im.size
    for i in range(w):
        for j in range(h):
            r, g, b = im.getpixel((i,j))
            if r != g != b:
                return False
    return True

def bilateral_filter(url):
    img = cv2.imread(url)
    bilateral = cv2.bilateralFilter(img, 15, 75, 75)
    photo = Image.fromarray(bilateral)
    return photo

def non_local_means_filter(url):
    if check_grayscale(url):
        img = cv2.imread(url)
        nlmeans = cv2.fastNlMeansDenoising(img, None, 20, 7, 21)
    else:
        img = cv2.imread(url)
        nlmeans = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
    photo = Image.fromarray(nlmeans)
    return photo

def add_images_to_dataset(url_tuple, labels):
    
    return None

def run_autoencoder(url_tuple, labels):
    change_dimension_and_add_to_dataset_and_run(url_tuple, labels)
    return None
    

run_autoencoder(('./dataset./MNIST./five.jpg', './dataset/MNIST/five.jpg', './dataset/MNIST/five.jpg'), (5, 5, 5))