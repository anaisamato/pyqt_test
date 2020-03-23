from PyQt5.QtWidgets import QDialog, QVBoxLayout, QAction

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt


class PlotGraph(QDialog):

    def __init__(self, data, parent=None):
        """
        Init the tab and the figure
        :param data: data to plot
        """
        super(PlotGraph, self).__init__(parent)
        self.data = data
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        self.toolbar = NavigationToolbar(self.canvas, self)
        self.plot()

        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        self.setWindowTitle('Je suis un graphe !!')

    def plot(self):
        """
        Create the plot with data
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
