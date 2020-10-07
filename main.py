from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvas, NavigationToolbar2QT as NavigationToolbar
import numpy as np
from matplotlib.figure import Figure
import func_val_calc as fn_calc
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1094, 854)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_viz = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_viz.setGeometry(QtCore.QRect(480, 760, 93, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_viz.sizePolicy().hasHeightForWidth())
        self.pushButton_viz.setSizePolicy(sizePolicy)
        self.pushButton_viz.setObjectName("pushButton_viz")
        self.lineEdit_equation = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_equation.setGeometry(QtCore.QRect(90, 710, 911, 22))
        self.lineEdit_equation.setObjectName("lineEdit_equation")
        self.label_xmin = QtWidgets.QLabel(self.centralwidget)
        self.label_xmin.setGeometry(QtCore.QRect(260, 650, 55, 16))
        self.label_xmin.setObjectName("label_xmin")
        self.label_xmax = QtWidgets.QLabel(self.centralwidget)
        self.label_xmax.setGeometry(QtCore.QRect(400, 650, 55, 16))
        self.label_xmax.setObjectName("label_xmax")
        self.label_ymin = QtWidgets.QLabel(self.centralwidget)
        self.label_ymin.setGeometry(QtCore.QRect(680, 650, 55, 16))
        self.label_ymin.setObjectName("label_ymin")
        self.label_ymax = QtWidgets.QLabel(self.centralwidget)
        self.label_ymax.setGeometry(QtCore.QRect(820, 650, 55, 16))
        self.label_ymax.setObjectName("label_ymax")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(550, 650, 55, 16))
        self.label.setObjectName("label")
        self.lineEdit_xmin = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_xmin.setGeometry(QtCore.QRect(290, 650, 51, 22))
        self.lineEdit_xmin.setObjectName("lineEdit_xmin")
        self.lineEdit_xmax = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_xmax.setGeometry(QtCore.QRect(430, 650, 51, 22))
        self.lineEdit_xmax.setObjectName("lineEdit_xmax")
        self.lineEdit_xstep = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_xstep.setGeometry(QtCore.QRect(580, 650, 51, 22))
        self.lineEdit_xstep.setObjectName("lineEdit_xstep")
        self.lineEdit_ymin = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ymin.setGeometry(QtCore.QRect(710, 650, 51, 22))
        self.lineEdit_ymin.setObjectName("lineEdit_ymin")
        self.lineEdit_ymax = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ymax.setGeometry(QtCore.QRect(850, 650, 51, 22))
        self.lineEdit_ymax.setObjectName("lineEdit_ymax")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 1051, 611))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1094, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuFunctions = QtWidgets.QMenu(self.menubar)
        self.menuFunctions.setObjectName("menuFunctions")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionsin = QtWidgets.QAction(MainWindow)
        self.actionsin.setObjectName("actionsin")
        self.actioncos = QtWidgets.QAction(MainWindow)
        self.actioncos.setObjectName("actioncos")
        self.actiontan = QtWidgets.QAction(MainWindow)
        self.actiontan.setObjectName("actiontan")
        self.actionasin = QtWidgets.QAction(MainWindow)
        self.actionasin.setObjectName("actionasin")
        self.actionacos = QtWidgets.QAction(MainWindow)
        self.actionacos.setObjectName("actionacos")
        self.actionatan = QtWidgets.QAction(MainWindow)
        self.actionatan.setObjectName("actionatan")
        self.actione = QtWidgets.QAction(MainWindow)
        self.actione.setObjectName("actione")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actioncosh = QtWidgets.QAction(MainWindow)
        self.actioncosh.setObjectName("actioncosh")
        self.actiontanh = QtWidgets.QAction(MainWindow)
        self.actiontanh.setObjectName("actiontanh")
        self.actionasinh = QtWidgets.QAction(MainWindow)
        self.actionasinh.setObjectName("actionasinh")
        self.actionacosh = QtWidgets.QAction(MainWindow)
        self.actionacosh.setObjectName("actionacosh")
        self.actionatanh = QtWidgets.QAction(MainWindow)
        self.actionatanh.setObjectName("actionatanh")
        self.actionln = QtWidgets.QAction(MainWindow)
        self.actionln.setObjectName("actionln")
        self.actionlog = QtWidgets.QAction(MainWindow)
        self.actionlog.setObjectName("actionlog")
        self.actionexp = QtWidgets.QAction(MainWindow)
        self.actionexp.setObjectName("actionexp")
        self.actionsqrt = QtWidgets.QAction(MainWindow)
        self.actionsqrt.setObjectName("actionsqrt")
        self.actionabs = QtWidgets.QAction(MainWindow)
        self.actionabs.setObjectName("actionabs")
        self.actionDocs = QtWidgets.QAction(MainWindow)
        self.actionDocs.setObjectName("actionDocs")
        self.menuFile.addAction(self.actionExit)
        self.menuFunctions.addAction(self.actionsin)
        self.menuFunctions.addAction(self.actioncos)
        self.menuFunctions.addAction(self.actiontan)
        self.menuFunctions.addAction(self.actionasin)
        self.menuFunctions.addAction(self.actionacos)
        self.menuFunctions.addAction(self.actionatan)
        self.menuFunctions.addAction(self.actione)
        self.menuFunctions.addAction(self.actioncosh)
        self.menuFunctions.addAction(self.actiontanh)
        self.menuFunctions.addAction(self.actionasinh)
        self.menuFunctions.addAction(self.actionacosh)
        self.menuFunctions.addAction(self.actionatanh)
        self.menuFunctions.addAction(self.actionln)
        self.menuFunctions.addAction(self.actionlog)
        self.menuFunctions.addAction(self.actionexp)
        self.menuFunctions.addAction(self.actionsqrt)
        self.menuFunctions.addAction(self.actionabs)
        self.menuHelp.addAction(self.actionDocs)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuFunctions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_viz.setText(_translate("MainWindow", "Visualize"))
        self.label_xmin.setText(_translate("MainWindow", "x-min"))
        self.label_xmax.setText(_translate("MainWindow", "x-max"))
        self.label_ymin.setText(_translate("MainWindow", "y-min"))
        self.label_ymax.setText(_translate("MainWindow", "y-max"))
        self.label.setText(_translate("MainWindow", "x step"))
        self.lineEdit_xmin.setText(_translate("MainWindow", "-1"))
        self.lineEdit_xmax.setText(_translate("MainWindow", "1"))
        self.lineEdit_xstep.setText(_translate("MainWindow", "0.1"))
        self.lineEdit_ymin.setText(_translate("MainWindow", "-1"))
        self.lineEdit_ymax.setText(_translate("MainWindow", "1"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuFunctions.setTitle(_translate("MainWindow", "Functions"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionsin.setText(_translate("MainWindow", "sin"))
        self.actioncos.setText(_translate("MainWindow", "cos"))
        self.actiontan.setText(_translate("MainWindow", "tan"))
        self.actionasin.setText(_translate("MainWindow", "asin"))
        self.actionacos.setText(_translate("MainWindow", "acos"))
        self.actionatan.setText(_translate("MainWindow", "atan"))
        self.actione.setText(_translate("MainWindow", "sinh"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actioncosh.setText(_translate("MainWindow", "cosh"))
        self.actiontanh.setText(_translate("MainWindow", "tanh"))
        self.actionasinh.setText(_translate("MainWindow", "asinh"))
        self.actionacosh.setText(_translate("MainWindow", "acosh"))
        self.actionatanh.setText(_translate("MainWindow", "atanh"))
        self.actionln.setText(_translate("MainWindow", "ln"))
        self.actionlog.setText(_translate("MainWindow", "log"))
        self.actionexp.setText(_translate("MainWindow", "exp"))
        self.actionsqrt.setText(_translate("MainWindow", "sqrt"))
        self.actionabs.setText(_translate("MainWindow", "abs"))
        self.actionDocs.setText(_translate("MainWindow", "Docs"))

        self.pushButton_viz.clicked.connect(self.OnClick)
        self.count = 0

    def canvas(self, x, y):
        if self.count == 0:
            self.static_canvas = FigureCanvas(Figure(figsize=(5, 3)))
            self.verticalLayout.addWidget(self.static_canvas)
        else:
            self.verticalLayout.removeWidget(self.static_canvas)
            self.static_canvas = FigureCanvas(Figure(figsize=(5, 3)))
            self.verticalLayout.addWidget(self.static_canvas)

        self._static_ax = self.static_canvas.figure.subplots()
        self._static_ax.plot(x,y,".")
        self.static_canvas.draw()
        self.count+=1

    def OnClick(self):

        print('button clicked')
        try:
            xmin = float(self.lineEdit_xmin.text())
        except:
            self.error_handler('xmin can only be numeric.')
            return
        try:
            xmax = float(self.lineEdit_xmax.text())
        except:
            self.error_handler('xmax can only be numeric.')
            return
        try:
            xstep = float(self.lineEdit_xstep.text())
        except:
            self.error_handler('xstep can only be numeric.')
            return
        try:
            ymin = float(self.lineEdit_ymin.text())
        except:
            self.error_handler('ymin can only be numeric.')
            return
        try:
            ymax = float(self.lineEdit_ymax.text())
        except:
            self.error_handler('ymax can only be numeric.')
            return

        eq = self.lineEdit_equation.text()
        print(xmin)
        print(eq)

        try:
            x,y = fn_calc.func_val(eq, xmin, xmax, ymin, ymax, xstep)
        except:
            self.error_handler("Could not evaluate the function. Please try again.")
            return

        self.canvas(x,y)

    def error_handler(self, message):
        err = QMessageBox()
        err.setWindowTitle("Error")
        err.setText(message)
        err.exec_()
        return


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())





