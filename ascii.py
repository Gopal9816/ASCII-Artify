from PIL import Image
from PIL import ImageFilter
import numpy as np
import sys
import argparse
import colorama

parser = argparse.ArgumentParser()
parser.add_argument('filename',
                    help='Image to be ASCII Artified')
parser.add_argument('-i',
                    '--invert',
                    action='store_true',
                    help='Inverts the colors')
parser.add_argument('-c',
                    '--conversion',
                    help='Select the method for converting RGB to brightness',
                    choices=['average','minmax','luminosity'],
                    default='average')
parser.add_argument('-C',
                    '--color',
                    help='Color in which the ascii art is to be printed',
                    choices=['red','green','blue','cyan','yellow','magenta'],
                    default='white')

output_color = colorama.Fore.WHITE

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

def invert_brightness(im_arr):
    n_rows = im_arr.shape[0]
    n_cols = im_arr.shape[1]
    for i in range(0,n_rows):
        for j in range(0,n_cols):
            im_arr[i][j] = 255-im_arr[i][j]

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
        print(output_color+output)


if __name__ == "__main__":
    colorama.init()
    args = parser.parse_args()
    img_ip = Image.open(args.filename)
    #print(img_ip.format,img_ip.size,img_ip.mode)

    img = img_ip.resize((400,300))
    #img = img.filter(ImageFilter.DETAIL)
    im_arr = np.array(img.getdata(),int).reshape(img.size[1],img.size[0],3)

    if args.conversion == "average":
        convt_im_array = rgb2brightness_avg(im_arr)
    elif args.conversion == "minmax":
        convt_im_array = rgb2brightness_min_max(im_arr)
    elif args.conversion == "luminosity":
        convt_im_array = rgb2brightness_luminosity(im_arr)

    if args.color == "red":
        output_color = colorama.Fore.RED
    elif args.color == "blue":
        output_color = colorama.Fore.BLUE
    elif args.color == "green":
        output_color = colorama.Fore.GREEN
    elif args.color == "cyan":
        output_color = colorama.Fore.CYAN
    elif args.color == "magenta":
        output_color = colorama.Fore.MAGENTA
    elif args.color == "yellow":
        output_color = colorama.Fore.YELLOW
    #print_vals(convt_im_array)

    if args.invert:
        invert_brightness(convt_im_array)

    map2ascii(convt_im_array)
    #print_vals(convt_im_array)
    printImg(convt_im_array)
    
    
