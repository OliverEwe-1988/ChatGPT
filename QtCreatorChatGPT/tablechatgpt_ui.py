# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Entwicklung\InfomotionChatGPT\QtCreatorChatGPT\tablechatgpt.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TableChatGPT(object):
    def setupUi(self, TableChatGPT):
        TableChatGPT.setObjectName("TableChatGPT")
        TableChatGPT.resize(740, 450)
        self.centralwidget = QtWidgets.QWidget(TableChatGPT)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("e:\\Entwicklung\\InfomotionChatGPT\\QtCreatorChatGPT\\../Bilder/HTWLogo.png"))
        self.label_8.setScaledContents(False)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("e:\\Entwicklung\\InfomotionChatGPT\\QtCreatorChatGPT\\../Bilder/desktop-logo_schwarz.svg"))
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout.addWidget(self.textEdit_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        TableChatGPT.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TableChatGPT)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 740, 22))
        self.menubar.setObjectName("menubar")
        TableChatGPT.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TableChatGPT)
        self.statusbar.setObjectName("statusbar")
        TableChatGPT.setStatusBar(self.statusbar)
        self.actionDirekt = QtWidgets.QAction(TableChatGPT)
        self.actionDirekt.setObjectName("actionDirekt")
        self.actionCode = QtWidgets.QAction(TableChatGPT)
        self.actionCode.setObjectName("actionCode")
        self.actionTabelle = QtWidgets.QAction(TableChatGPT)
        self.actionTabelle.setObjectName("actionTabelle")
        self.action1_Reihe = QtWidgets.QAction(TableChatGPT)
        self.action1_Reihe.setObjectName("action1_Reihe")
        self.actionProjektteam = QtWidgets.QAction(TableChatGPT)
        self.actionProjektteam.setObjectName("actionProjektteam")

        self.retranslateUi(TableChatGPT)
        QtCore.QMetaObject.connectSlotsByName(TableChatGPT)

    def retranslateUi(self, TableChatGPT):
        _translate = QtCore.QCoreApplication.translate
        TableChatGPT.setWindowTitle(_translate("TableChatGPT", "MainWindow"))
        self.label.setText(_translate("TableChatGPT", "Table ChatGPT"))
        self.label_2.setText(_translate("TableChatGPT", "Stell deine Frage an ChatGPT, die gesamte Tabelle wird mit übergeben"))
        self.pushButton.setText(_translate("TableChatGPT", "senden"))
        self.label_3.setText(_translate("TableChatGPT", "deine Ausgabe"))
        self.label_6.setText(_translate("TableChatGPT", "Kosten in Token: "))
        self.label_5.setText(_translate("TableChatGPT", "keine Kosten vorhanden"))
        self.actionDirekt.setText(_translate("TableChatGPT", "Direkt"))
        self.actionCode.setText(_translate("TableChatGPT", "Code"))
        self.actionTabelle.setText(_translate("TableChatGPT", "Tabelle"))
        self.action1_Reihe.setText(_translate("TableChatGPT", "1. Reihe"))
        self.actionProjektteam.setText(_translate("TableChatGPT", "Projektteam"))
