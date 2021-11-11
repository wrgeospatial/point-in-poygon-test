import matplotlib
import matplotlib.pyplot as plt

from collections import OrderedDict

matplotlib.use('TkAgg')

from functions import Plotter
from functions import open_poly_x
from functions import open_poly_y
from functions import open_input_x
from functions import open_input_y

def main():
    Plotter.add_polygon(0, open_poly_x(), open_poly_y())
    Plotter.add_point(0, open_input_x(), open_input_y())
    Plotter.show(0)

if __name__ == '__main__':
    main()



