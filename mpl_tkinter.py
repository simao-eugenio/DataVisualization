import tkinter as tk
import matplotlib
matplotlib.use('tkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (

    FigureCanvasTkAgg, 
    NavigationToolbar2TkAgg
)

class App(tk,tk):
    def __init__(self):
        super().__init__()
        self.title('TKinter Matplotlib Demo')

        # prepare data
        data = {

            'Python': 11.27,
            'C': 11.16,
            'Java': 10.46,
            'C++': 7.5,
            'C#': 5.26

        }

        languages = data.keys()
        popularity = data.values()

        # create a figure
        figure = Figure(figsize=(6,4), dpi=100)

        # create FigureCanvasTkAgg object
        figure_canvas = FigureCanvasTkAgg(figure, self)
