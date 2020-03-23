from PyQt5.QtWidgets import QDialog, QVBoxLayout, QAction

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt


class PlotGraph(QDialog):

    def __init__(self, data, parent=None):
        super(PlotGraph, self).__init__(parent)
        self.data = data
        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.plot()

        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        self.setWindowTitle('Je suis un graphe !!')

    def plot(self):
        """

        :return:
        """
        self.figure.clear()
        # create an axis
        ax = self.figure.add_subplot(111)
        # plot data
        ax.plot(self.data[0], self.data[1], '*-')
        # refresh canvas
        self.canvas.draw()


def launch_plot(data):
    main = PlotGraph(data)
    main.show()
