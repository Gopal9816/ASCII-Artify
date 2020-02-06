# ASCII Art Generator

This program generates an ASCII art representation of a given image. Built as a part of Robert Heaton's PFAB series which can be found [here](https://robertheaton.com/2018/06/12/programming-projects-for-advanced-beginners-ascii-art/)

## Dependencies
* [Pillow](https://python-pillow.org)
* [numpy](https://numpy.org/)
* [colorama](https://pypi.org/project/colorama/)

## Usage
` python ascii.py filename [-h] [-i] [-c {average,minmax,luminosity}] ` <br/>

### positional arguments:
    filename    Image to be ASCII Artified
### optional arguments:
    -h, --help      Show this help message and exit
    -i, --invert    Inverts the color
    -c              Selects the method for converting RGB                      to 

