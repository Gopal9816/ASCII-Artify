# ASCII Art Generator 
*Note: Still in Progress*
*Update: Weebs Rejoice!!, the program can now also display your gifs in the terminal UwU*

This program generates an ASCII art representation. ASCII art uses ASCII characthers to represent pixels of an image. The image is printed as strings of characthers on the terminal. Built as a part of Robert Heaton's PFAB series which can be found [here](https://robertheaton.com/2018/06/12/programming-projects-for-advanced-beginners-ascii-art/) <br/>

Support for Animated GIFs was inspired by [yattsu's project](https://github.com/yattsu/image_to_ascii)

## Dependencies
* [Pillow](https://python-pillow.org)
* [numpy](https://numpy.org/)
* [colorama](https://pypi.org/project/colorama/)
* [requests](https://requests.readthedocs.io/en/master/)

## Usage
` python ascii.py filename [-h] [-i] [-c {average,minmax,luminosity}] [-C {red, blue, green, cyan, magenta, yellow}]` <br/>

### positional arguments:
    filename    Image/GIF to be ASCII Artified
### optional arguments:
    -h, --help      Show this help message and exit
    -i, --invert    Inverts the color
    -c              Selects the method for converting RGB to brightness value
    -C, --color     Selects the output color of the printed text

