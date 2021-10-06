from autoencoder import change_dimension_and_add_to_dataset, run_main
import numpy as np
import cv2
from skimage import img_as_float, color, io, feature
from skimage.color import rgb2gray
from skimage.filters import sobel, scharr, roberts, prewitt, laplace
from PIL import Image, ImageFilter, ImageTk, ImageEnhance
from PIL.ImageFilter import FIND_EDGES, EDGE_ENHANCE, EDGE_ENHANCE_MORE
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

def Sobel_filter(url):
   im = rgb2gray(cv2.imread(url))
   filtered_im = sobel(im)
   return filtered_im

def Roberts_filter(url):
   im = rgb2gray(cv2.imread(url))
   filtered_im = roberts(im)
   return filtered_im

def Scharr_filter(url):
   im = rgb2gray(cv2.imread(url))
   filtered_im = scharr(im)
   return filtered_im

def Prewitt_filter(url):
   im = rgb2gray(cv2.imread(url))
   filtered_im = prewitt(im)
   return filtered_im

def Laplace_filter(url):
   im = rgb2gray(cv2.imread(url))
   filtered_im = laplace(im)
   return filtered_im

def Canny_filter(url, sigma):
   im = rgb2gray(cv2.imread(url))
   filtered_im = feature.canny(im, sigma)
   return filtered_im

def pillow_find_edges(url):
    im = Image.open(url)
    filtered_im = im.filter(FIND_EDGES)
    return filtered_im

def add_to_dataset(url_tuple, label_tuple):
    change_dimension_and_add_to_dataset(url_tuple, label_tuple)
    return None

image = Canny_filter('./autoencoder_4.png', 8)
f = plt.figure()
f.add_subplot(1,2, 1)
plt.imshow(image,cmap='gray')
f.add_subplot(1,2, 2)
plt.imshow(cv2.imread('./autoencoder_4.png'), cmap='gray')
plt.show(block=True)
