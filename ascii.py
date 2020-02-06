from PIL import Image
from PIL import ImageFilter
import numpy as np
import sys

def rgb2brightness_avg(im_arr):
    n_rows = im_arr.shape[0]
    n_cols = im_arr.shape[1]
    res = np.ones((n_rows,n_cols),dtype=int)
    for i in range(0,n_rows):
        for j in range(0,n_cols):
            res[i][j] = (im_arr[i][j][0] + im_arr[i][j][1] + im_arr[i][j][2])//3
    return res

def rgb2brightness_min_max(im_arr):
    n_rows = im_arr.shape[0]
    n_cols = im_arr.shape[1]
    res = np.ones((n_rows,n_cols),dtype=int)
    for i in range(0,n_rows):
        for j in range(0,n_cols):
            res[i][j] = (np.min(im_arr[i][j]) + np.max(im_arr[i][j]))//2
    return res

def rgb2brightness_luminosity(im_arr):
    n_rows = im_arr.shape[0]
    n_cols = im_arr.shape[1]
    res = np.ones((n_rows,n_cols),dtype=int)
    for i in range(0,n_rows):
        for j in range(0,n_cols):
            res[i][j] = (0.21*im_arr[i][j][0] + 0.72*im_arr[i][j][1] + 0.07*im_arr[i][j][2])
    return res



def print_vals(im_arr):
    n_rows = im_arr.shape[0]
    n_cols = im_arr.shape[1]
    for i in range(0,n_rows):
        for j in range(0,n_cols):
            print(im_arr[i][j])
    
def map2ascii(im_arr):
    n_rows = im_arr.shape[0]
    n_cols = im_arr.shape[1]

    for i in range(0,n_rows):
        for j in range(0,n_cols):
            im_arr[i][j] = int((im_arr[i][j]/255)*64)

def printImg(im_arr):
    n_rows = im_arr.shape[0]
    n_cols = im_arr.shape[1]
    ascii_mask = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

    for i in range(0,n_rows):
        output = ""
        for j in range(0, n_cols):
            output += ascii_mask[im_arr[i][j]]*2
        print(output)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Format: python ascii.py filename")
    filename = sys.argv[1]
    img_ip = Image.open(filename)
    print(img_ip.format,img_ip.size,img_ip.mode)

    img = img_ip.resize((400,300))
    #img = img.filter(ImageFilter.DETAIL)
    im_arr = np.array(img.getdata(),int).reshape(img.size[1],img.size[0],3)

    convt_im_array = rgb2brightness_avg(im_arr)
    #convt_im_array = rgb2brightness_min_max(im_arr)
    #convt_im_array = rgb2brightness_luminosity(im_arr)
    #print_vals(convt_im_array)
    map2ascii(convt_im_array)
    #print_vals(convt_im_array)
    printImg(convt_im_array)
    
    
