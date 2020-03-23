import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp, QPushButton, QHBoxLayout, QWidget, QVBoxLayout, \
    QLabel, QLineEdit, QTableWidget, QTableWidgetItem
from inputFileDialog import InputLoadFile
from readFile import ReadFile
from plotGraph import launch_plot


class Principale(QMainWindow):
    def __init__(self):
        super().__init__()
        self.filename = ""
        self.setUI()

    def setUI(self):

        # First line : button load and label with filename
        hbox = QHBoxLayout()
        button_load = QPushButton('Load File')
        button_load.clicked.connect(self.on_button_clicked)
        self.label = QLabel("")
        hbox.addWidget(button_load)
        hbox.addWidget(self.label)
        hbox.addStretch(1)

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(hbox)
        self.vbox.addStretch(1)
        self.vbox.addStretch(1)

        w = QWidget()
        w.setLayout(self.vbox)
        self.setCentralWidget(w)

        exitAction = QAction('&Exit', self)
        exitAction.setShortcut('Ctrl-Q')
        # exitAction.setStatusTip("Quitter l'application")
        exitAction.triggered.connect(qApp.exit)

        self.barreOutils = self.addToolBar('Quitter')
        self.barreOutils.addAction(exitAction)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('On affiche des graphes !!')
        self.show()

    def on_button_clicked(self):
        self.filename = InputLoadFile().filename
        self.data = ReadFile(self.filename).data

        # Second line : Text fields with X and Y
        hboxCoord = QHBoxLayout()
        label_min_x = QLabel("Min X : ")
        label_max_x = QLabel("Max X : ")
        self.textbox_min_x = QLineEdit()
        self.textbox_max_x = QLineEdit()
        hboxCoord.addWidget(label_min_x)
        hboxCoord.addWidget(self.textbox_min_x)
        hboxCoord.addWidget(label_max_x)
        hboxCoord.addWidget(self.textbox_max_x)
        hboxCoord.addStretch(1)

        # Forth line : Button Plot
        hbox_plot = QHBoxLayout()
        button_plot = QPushButton('Plot')
        button_plot.clicked.connect(self.launch_plot_window)
        hbox_plot.addStretch(1)
        hbox_plot.addWidget(button_plot)
        hbox_plot.addStretch(1)

        hbox_label_table = QHBoxLayout()
        label_table = QLabel("Values : ")
        hbox_label_table.addWidget(label_table)

        hbox_table = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(2)
        tableWidget.setColumnCount(len(self.data[0]))
        hbox_table.addWidget(tableWidget)
        for i in range(len(self.data[0])):
            tableWidget.setItem(0, i, QTableWidgetItem(str(self.data[0][i])))
            tableWidget.setItem(1, i, QTableWidgetItem(str(self.data[1][i])))

        self.vbox.addLayout(hboxCoord)
        self.vbox.addLayout(hbox_label_table)
        self.vbox.addLayout(hbox_table)
        self.vbox.addLayout(hbox_plot)

        self.textbox_min_x.setText(str(min(self.data[0])))
        self.textbox_max_x.setText(str(max(self.data[0])))
        self.label.setText(self.filename)

    def launch_plot_window(self):
        launch_plot(self.data)


monApp = QApplication(sys.argv)
fenetre = Principale()
sys.exit(monApp.exec_())
