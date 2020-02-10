from PIL import Image
import numpy as np
import sys
import os
import argparse
import colorama
import time
import requests
import io

im_height = 200 #400
im_width = 128 #300

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
ascii_mask = " :co@"
#ascii_mask = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

def is_image(filename):
    if ".jpg" in filename:
        return True
    elif ".jpeg" in filename:
        return True
    elif ".png" in filename:
        return True
    elif ".gif" in filename:
        return True
    return False

def is_link(filename):
    if "http://" in filename or "https://" in filename:
        return True
    return False

def is_gif(filename):
    if ".gif" in filename:
        return True
    return False

def get_image(filename):
    if not is_image(filename):
        raise TypeError
    
    if is_link(filename):
        res = requests.get(filename)
        image = Image.open(io.BytesIO(res.content))
    elif not os.path.exists(filename):
        raise FileNotFoundError
    else:
        image = Image.open(filename)

    frames = []
    if is_gif(filename):
        try:
            while True:
                new_frame = image.copy()
                new_frame = new_frame.convert('RGB')
                new_frame.thumbnail((200,128),Image.ANTIALIAS)
                frames.append(new_frame)
                image.seek(image.tell()+1)
        except EOFError:
            return frames
    else:
        image = image.resize((im_height,im_width))
        frames.append(image)
    return frames

def rgb2brightness_avg(frames):
    width,height = frames[0].size
    
    res_frames = []

    for image in frames:
        res = np.ones((height,width),dtype=int)
        for y in range(0,height):
            for x in range(0,width):
                try:
                    r,g,b = image.getpixel((x,y))
                except:
                    r,g,b,a = image.getpixel((x,y))
                res[y][x] = (r+g+b)//3
        res_frames.append(res)
    
    return res_frames

def rgb2brightness_min_max(frames):
    width,height = frames[0].size
    
    res_frames = []

    for image in frames:
        res = np.ones((height,width),dtype=int)
        for y in range(0,height):
            for x in range(0,width):
                res[y][x] = (np.min(image.getpixel((x,y))) + np.max(image.getpixel((x,y))))//2
        res_frames.append(res)
    
    return res_frames

def rgb2brightness_luminosity(frames):
    width,height = frames[0].size
    
    res_frames = []
    
    for image in frames:
        res = np.ones((height,width),dtype=int)
        for y in range(0,height):
            for x in range(0,width):
                try:
                    r,g,b = image.getpixel((x,y))
                except:
                    r,g,b,a = image.getpixel((x,y))
                res[y][x] = (0.21*r + 0.72*g + 0.07*b)
        res_frames.append(res)
    
    return res_frames

def invert_brightness(frames):
    width,height = frames[0].size
    
    res_frames = []
    for image in frames:
        for i in range(0,n_rows):
            for j in range(0,n_cols):
                image[i][j] = 255-image[i][j]

def print_vals(frames):
    n_rows = frames[0].shape[0]
    n_cols = frames[0].shape[1]
    
    res_frames = []
    for image in frames:
        for i in range(0,n_rows):
            for j in range(0,n_cols):
                print(image[i][j])
    
def map2ascii(frames):
    n_rows = frames[0].shape[0]
    n_cols = frames[0].shape[1]
    
    res_frames = []

    output_levels = len(ascii_mask)-1

    for image in frames:
        for i in range(0,n_rows):
            for j in range(0,n_cols):
                image[i][j] = int((image[i][j]/255)*output_levels)

def printImg(frames):
    n_rows = frames[0].shape[0]
    n_cols = frames[0].shape[1]
    delay = 0.1

    for image in frames:
        print("\033[H\033[J")
        for i in range(0,n_rows):
            output = ""
            for j in range(0, n_cols):
                output += ascii_mask[image[i][j]]*2
            print(output_color+output)
        time.sleep(delay)
        


if __name__ == "__main__":
    colorama.init()
    args = parser.parse_args()

    try:
        frames = get_image(args.filename)
    except TypeError:
        print('Unsupported file format given')
    # print(len(frames))
        

    if args.conversion == "average":
        convt_frames = rgb2brightness_avg(frames)
    elif args.conversion == "minmax":
        convt_frames = rgb2brightness_min_max(frames)
    elif args.conversion == "luminosity":
        convt_frames = rgb2brightness_luminosity(frames)

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

    if args.invert:
        invert_brightness(convt_frames)

    map2ascii(convt_frames)
    printImg(convt_frames)
    
    
