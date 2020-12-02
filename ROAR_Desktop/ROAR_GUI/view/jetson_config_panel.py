# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'model/jetson_config_panel.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_JetsonConfigWindow(object):
    def setupUi(self, JetsonConfigWindow):
        JetsonConfigWindow.setObjectName("JetsonConfigWindow")
        JetsonConfigWindow.resize(817, 699)
        self.centralwidget = QtWidgets.QWidget(JetsonConfigWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 771, 631))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setVerticalSpacing(5)
        self.formLayout.setObjectName("formLayout")
        self.horizontalLayout.addLayout(self.formLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_confirm = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_confirm.setObjectName("pushButton_confirm")
        self.verticalLayout_2.addWidget(self.pushButton_confirm)
        self.pushButton_reset = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.verticalLayout_2.addWidget(self.pushButton_reset)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        JetsonConfigWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(JetsonConfigWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 817, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        JetsonConfigWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(JetsonConfigWindow)
        self.statusbar.setObjectName("statusbar")
        JetsonConfigWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(JetsonConfigWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionSave = QtWidgets.QAction(JetsonConfigWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(JetsonConfigWindow)
        QtCore.QMetaObject.connectSlotsByName(JetsonConfigWindow)

    def retranslateUi(self, JetsonConfigWindow):
        _translate = QtCore.QCoreApplication.translate
        JetsonConfigWindow.setWindowTitle(_translate("JetsonConfigWindow", "MainWindow"))
        self.pushButton_confirm.setText(_translate("JetsonConfigWindow", "Confim"))
        self.pushButton_reset.setText(_translate("JetsonConfigWindow", "Reset"))
        self.menuFile.setTitle(_translate("JetsonConfigWindow", "File"))
        self.actionQuit.setText(_translate("JetsonConfigWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("JetsonConfigWindow", "Esc"))
        self.actionSave.setText(_translate("JetsonConfigWindow", "Save"))
        self.actionSave.setShortcut(_translate("JetsonConfigWindow", "Ctrl+S"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    JetsonConfigWindow = QtWidgets.QMainWindow()
    ui = Ui_JetsonConfigWindow()
    ui.setupUi(JetsonConfigWindow)
    JetsonConfigWindow.show()
    sys.exit(app.exec_())
