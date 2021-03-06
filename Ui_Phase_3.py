# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Slims\Desktop\Prog1700_source_code\project-countriesoftheworld-Fayaz046-main\Phase3.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.countriesListBox = QtWidgets.QListWidget(self.centralwidget)
        self.countriesListBox.setGeometry(QtCore.QRect(30, 40, 256, 511))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.countriesListBox.setFont(font)
        self.countriesListBox.setObjectName("countriesListBox")
        self.frameMain = QtWidgets.QFrame(self.centralwidget)
        self.frameMain.setGeometry(QtCore.QRect(330, 210, 431, 341))
        self.frameMain.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameMain.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameMain.setObjectName("frameMain")
        self.userEntry = QtWidgets.QLineEdit(self.frameMain)
        self.userEntry.setGeometry(QtCore.QRect(110, 60, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.userEntry.setFont(font)
        self.userEntry.setObjectName("userEntry")
        self.labelPopulation = QtWidgets.QLabel(self.frameMain)
        self.labelPopulation.setGeometry(QtCore.QRect(10, 60, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelPopulation.setFont(font)
        self.labelPopulation.setObjectName("labelPopulation")
        self.Update_Population_button = QtWidgets.QPushButton(self.frameMain)
        self.Update_Population_button.setGeometry(QtCore.QRect(250, 100, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Update_Population_button.setFont(font)
        self.Update_Population_button.setObjectName("Update_Population_button")
        self.totalareaToggle = QtWidgets.QComboBox(self.frameMain)
        self.totalareaToggle.setGeometry(QtCore.QRect(120, 190, 91, 22))
        self.totalareaToggle.setEditable(True)
        self.totalareaToggle.setObjectName("totalareaToggle")
        self.totalareaToggle.addItem("")
        self.totalareaToggle.addItem("")
        self.labelTotalArea = QtWidgets.QLabel(self.frameMain)
        self.labelTotalArea.setGeometry(QtCore.QRect(10, 190, 120, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelTotalArea.setFont(font)
        self.labelTotalArea.setObjectName("labelTotalArea")
        self.labelDensity = QtWidgets.QLabel(self.frameMain)
        self.labelDensity.setGeometry(QtCore.QRect(10, 230, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelDensity.setFont(font)
        self.labelDensity.setObjectName("labelDensity")
        self.labelPopulationPercentage = QtWidgets.QLabel(self.frameMain)
        self.labelPopulationPercentage.setGeometry(QtCore.QRect(10, 300, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelPopulationPercentage.setFont(font)
        self.labelPopulationPercentage.setObjectName("labelPopulationPercentage")
        self.labelPopulationNumber = QtWidgets.QLabel(self.frameMain)
        self.labelPopulationNumber.setGeometry(QtCore.QRect(220, 300, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelPopulationNumber.setFont(font)
        self.labelPopulationNumber.setText("")
        self.labelPopulationNumber.setObjectName("labelPopulationNumber")
        self.labelPOPPercentage = QtWidgets.QLabel(self.frameMain)
        self.labelPOPPercentage.setGeometry(QtCore.QRect(330, 305, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.labelPOPPercentage.setFont(font)
        self.labelPOPPercentage.setText("")
        self.labelPOPPercentage.setObjectName("labelPOPPercentage")
        self.totalArea = QtWidgets.QLabel(self.frameMain)
        self.totalArea.setGeometry(QtCore.QRect(325, 190, 111, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(11)
        self.totalArea.setFont(font)
        self.totalArea.setText("")
        self.totalArea.setObjectName("totalArea")
        self.labelChooseCountry = QtWidgets.QLabel(self.centralwidget)
        self.labelChooseCountry.setGeometry(QtCore.QRect(30, 20, 261, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelChooseCountry.setFont(font)
        self.labelChooseCountry.setObjectName("labelChooseCountry")
        self.labelCountryName = QtWidgets.QLabel(self.centralwidget)
        self.labelCountryName.setGeometry(QtCore.QRect(340, 30, 111, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(13)
        self.labelCountryName.setFont(font)
        self.labelCountryName.setText("")
        self.labelCountryName.setObjectName("labelCountryName")
        self.frameSecondary = QtWidgets.QFrame(self.centralwidget)
        self.frameSecondary.setGeometry(QtCore.QRect(340, 470, 431, 41))
        self.frameSecondary.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameSecondary.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameSecondary.setObjectName("frameSecondary")
        self.densityButtonSQMile = QtWidgets.QRadioButton(self.frameSecondary)
        self.densityButtonSQMile.setGeometry(QtCore.QRect(10, -2, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.densityButtonSQMile.setFont(font)
        self.densityButtonSQMile.setObjectName("densityButtonSQMile")
        self.densityButtonSQKM = QtWidgets.QRadioButton(self.frameSecondary)
        self.densityButtonSQKM.setGeometry(QtCore.QRect(10, 22, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.densityButtonSQKM.setFont(font)
        self.densityButtonSQKM.setObjectName("densityButtonSQKM")
        self.pDensitylabel = QtWidgets.QLabel(self.frameSecondary)
        self.pDensitylabel.setGeometry(QtCore.QRect(335, 10, 71, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(11)
        self.pDensitylabel.setFont(font)
        self.pDensitylabel.setText("")
        self.pDensitylabel.setObjectName("pDensitylabel")
        self.labelImages = QtWidgets.QLabel(self.centralwidget)
        self.labelImages.setGeometry(QtCore.QRect(360, 70, 460, 190))
        self.labelImages.setText("")
        self.labelImages.setObjectName("labelImages")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Load_countries_button = QtWidgets.QAction(MainWindow)
        self.Load_countries_button.setObjectName("Load_countries_button")
        self.Save_File_button = QtWidgets.QAction(MainWindow)
        self.Save_File_button.setEnabled(False)
        self.Save_File_button.setObjectName("Save_File_button")
        self.Exit_button = QtWidgets.QAction(MainWindow)
        self.Exit_button.setObjectName("Exit_button")
        self.menuFile.addAction(self.Load_countries_button)
        self.menuFile.addAction(self.Save_File_button)
        self.menuFile.addAction(self.Exit_button)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Countries of the World"))
        self.labelPopulation.setText(_translate("MainWindow", "Population:"))
        self.Update_Population_button.setText(_translate("MainWindow", "Update Population"))
        self.totalareaToggle.setCurrentText(_translate("MainWindow", "Sq. Miles"))
        self.totalareaToggle.setItemText(0, _translate("MainWindow", "Sq. Miles"))
        self.totalareaToggle.setItemText(1, _translate("MainWindow", "Sq. KM"))
        self.labelTotalArea.setText(_translate("MainWindow", "Total Area in"))
        self.labelDensity.setText(_translate("MainWindow", "Population Density"))
        self.labelPopulationPercentage.setText(_translate("MainWindow", "Percentage of World Population :"))
        self.labelChooseCountry.setText(_translate("MainWindow", "Choose a country from the list:"))
        self.densityButtonSQMile.setText(_translate("MainWindow", "Per Square Mile"))
        self.densityButtonSQKM.setText(_translate("MainWindow", "Per Square KM"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.Load_countries_button.setText(_translate("MainWindow", "Load From File"))
        self.Save_File_button.setText(_translate("MainWindow", "Save To File"))
        self.Exit_button.setText(_translate("MainWindow", "Exit"))
