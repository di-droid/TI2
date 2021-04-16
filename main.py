from PyQt5 import QtCore, QtGui, QtWidgets
from elGamal import PublicKey, generate_keys, encryption, decryption
from message import string_to_list, string_to_cipher, list_to_string, cipher_to_string
from file import key_from_file, key_to_file, cipher_from_file, cipher_to_file


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 560)
        MainWindow.setMinimumSize(QtCore.QSize(900, 560))
        MainWindow.setMaximumSize(QtCore.QSize(900, 560))
        MainWindow.setStyleSheet("background-color: rgb(221, 218, 232);")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbPublic = QtWidgets.QLabel(self.centralwidget)
        self.lbPublic.setGeometry(QtCore.QRect(0, 0, 930, 40))
        self.lbPublic.setStyleSheet("font: 12pt \"Roboto\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(175, 164, 206);")
        self.lbPublic.setObjectName("lbPublic")
        self.lbP = QtWidgets.QLabel(self.centralwidget)
        self.lbP.setGeometry(QtCore.QRect(0, 40, 40, 40))
        self.lbP.setStyleSheet("font: 12pt \"Roboto\";\n"
                               "color: rgb(255, 255, 255);\n"
                               "background-color: rgb(169, 169, 169);")
        self.lbP.setObjectName("lbP")
        self.lbG = QtWidgets.QLabel(self.centralwidget)
        self.lbG.setGeometry(QtCore.QRect(0, 80, 40, 40))
        self.lbG.setStyleSheet("font: 12pt \"Roboto\";\n"
                               "color: rgb(255, 255, 255);\n"
                               "background-color: rgb(169, 169, 169);")
        self.lbG.setObjectName("lbG")
        self.lbY = QtWidgets.QLabel(self.centralwidget)
        self.lbY.setGeometry(QtCore.QRect(0, 120, 40, 40))
        self.lbY.setStyleSheet("font: 12pt \"Roboto\";\n"
                               "color: rgb(255, 255, 255);\n"
                               "background-color: rgb(169, 169, 169);")
        self.lbY.setObjectName("lbY")
        self.lbPKey = QtWidgets.QLabel(self.centralwidget)
        self.lbPKey.setGeometry(QtCore.QRect(40, 40, 860, 40))
        self.lbPKey.setStyleSheet("font: 12pt \"Roboto\";\n"
                                  "color: rgb(39, 71, 92);\n"
                                  "background-color: rgb(221, 218, 232);")
        self.lbPKey.setObjectName("lbPKey")
        self.lbGKey = QtWidgets.QLabel(self.centralwidget)
        self.lbGKey.setGeometry(QtCore.QRect(40, 80, 860, 40))
        self.lbGKey.setStyleSheet("font: 12pt \"Roboto\";\n"
                                  "color: rgb(39, 71, 92);\n"
                                  "background-color: rgb(221, 218, 232);")
        self.lbGKey.setObjectName("lbGKey")
        self.lbYKey = QtWidgets.QLabel(self.centralwidget)
        self.lbYKey.setGeometry(QtCore.QRect(40, 120, 860, 40))
        self.lbYKey.setStyleSheet("font: 12pt \"Roboto\";\n"
                                  "color: rgb(39, 71, 92);\n"
                                  "background-color: rgb(221, 218, 232);")
        self.lbYKey.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lbYKey.setWordWrap(False)
        self.lbYKey.setObjectName("lbYKey")
        self.firstBord = QtWidgets.QLabel(self.centralwidget)
        self.firstBord.setGeometry(QtCore.QRect(0, 39, 900, 2))
        self.firstBord.setStyleSheet("background-color: rgb();")
        self.firstBord.setText("")
        self.firstBord.setObjectName("firstBord")
        self.secondBord = QtWidgets.QLabel(self.centralwidget)
        self.secondBord.setGeometry(QtCore.QRect(39, 40, 2, 120))
        self.secondBord.setStyleSheet("background-color: rgb(219, 219, 211);")
        self.secondBord.setText("")
        self.secondBord.setObjectName("secondBord")
        self.thirdBord = QtWidgets.QLabel(self.centralwidget)
        self.thirdBord.setGeometry(QtCore.QRect(0, 79, 900, 2))
        self.thirdBord.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.thirdBord.setText("")
        self.thirdBord.setObjectName("thirdBord")
        self.forthBord = QtWidgets.QLabel(self.centralwidget)
        self.forthBord.setGeometry(QtCore.QRect(0, 119, 900, 2))
        self.forthBord.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.forthBord.setText("")
        self.forthBord.setObjectName("forthBord")
        self.lbFrom = QtWidgets.QLabel(self.centralwidget)
        self.lbFrom.setGeometry(QtCore.QRect(520, 5, 55, 30))
        self.lbFrom.setStyleSheet("font: 12pt \"Roboto\";\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "background-color: rgb(175, 164, 206);")
        self.lbFrom.setObjectName("lbFrom")
        self.backGenerate = QtWidgets.QLabel(self.centralwidget)
        self.backGenerate.setGeometry(QtCore.QRect(795, 5, 100, 30))
        self.backGenerate.setStyleSheet("background-color: rgb(169, 169, 169);")
        self.backGenerate.setText("")
        self.backGenerate.setObjectName("backGenerate")
        self.btnGenerate = QtWidgets.QPushButton(self.centralwidget)
        self.btnGenerate.setGeometry(QtCore.QRect(795, 5, 100, 30))
        self.btnGenerate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnGenerate.setStyleSheet("font: 12pt \"Roboto\";\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "background-color: rgb(169, 169, 169);")
        self.btnGenerate.setFlat(True)
        self.btnGenerate.setObjectName("btnGenerate")
        self.firstBite = QtWidgets.QLineEdit(self.centralwidget)
        self.firstBite.setAlignment(QtCore.Qt.AlignCenter)
        self.firstBite.setGeometry(QtCore.QRect(580, 5, 51, 30))
        self.firstBite.setStyleSheet("font: 12pt \"Roboto\";\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "background-color: rgb(175, 164, 206);")
        self.firstBite.setText("128")
        self.firstBite.setMaxLength(4)
        self.firstBite.setObjectName("firstBite")
        self.lbTo = QtWidgets.QLabel(self.centralwidget)
        self.lbTo.setGeometry(QtCore.QRect(641, 5, 20, 30))
        self.lbTo.setStyleSheet("font: 12pt \"Roboto\";\n"
                                "color: rgb(255, 255, 255);\n"
                                "background-color: rgb(175, 164, 206);")
        self.lbTo.setObjectName("lbTo")
        self.lastByte = QtWidgets.QLineEdit(self.centralwidget)
        self.lastByte.setAlignment(QtCore.Qt.AlignCenter)
        self.lastByte.setGeometry(QtCore.QRect(671, 5, 51, 30))
        self.lastByte.setStyleSheet("font: 12pt \"Roboto\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(175, 164, 206);")
        self.lastByte.setText("256")
        self.lastByte.setMaxLength(4)
        self.lastByte.setObjectName("lastByte")
        self.lbByte = QtWidgets.QLabel(self.centralwidget)
        self.lbByte.setGeometry(QtCore.QRect(732, 5, 50, 30))
        self.lbByte.setStyleSheet("font: 12pt \"Roboto\";\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "background-color: rgb(175, 164, 206);")
        self.lbByte.setObjectName("lbByte")
        self.lbPrivate = QtWidgets.QLabel(self.centralwidget)
        self.lbPrivate.setGeometry(QtCore.QRect(0, 160, 900, 40))
        self.lbPrivate.setStyleSheet("font: 12pt \"Roboto\";\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "background-color: rgb(175, 164, 206);")
        self.lbPrivate.setObjectName("lbPrivate")
        self.lbX = QtWidgets.QLabel(self.centralwidget)
        self.lbX.setGeometry(QtCore.QRect(0, 200, 40, 40))
        self.lbX.setStyleSheet("font: 12pt \"Roboto\";\n"
                               "color: rgb(255, 255, 255);\n"
                               "background-color: rgb(169, 169, 169);")
        self.lbX.setObjectName("lbX")
        self.lbXKey = QtWidgets.QLabel(self.centralwidget)
        self.lbXKey.setGeometry(QtCore.QRect(40, 200, 860, 40))
        self.lbXKey.setAutoFillBackground(False)
        self.lbXKey.setStyleSheet("font: 12pt \"Roboto\";\n"
                                  "color: rgb(39, 71, 92);\n"
                                  "background-color: rgb(221, 218, 232);")
        self.lbXKey.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbXKey.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lbXKey.setScaledContents(False)
        self.lbXKey.setWordWrap(False)
        self.lbXKey.setIndent(-1)
        self.lbXKey.setObjectName("lbXKey")
        self.lbDecrypted = QtWidgets.QLabel(self.centralwidget)
        self.lbDecrypted.setGeometry(QtCore.QRect(0, 240, 600, 40))
        self.lbDecrypted.setStyleSheet("font: 12pt \"Roboto\";\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "background-color: rgb(175, 164, 206);")
        self.lbDecrypted.setObjectName("lbDecrypted")
        self.decryptedEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.decryptedEdit.setGeometry(QtCore.QRect(0, 280, 600, 100))
        self.decryptedEdit.setAutoFillBackground(True)
        self.decryptedEdit.setStyleSheet("font: 12pt \"Roboto\";\n"
                                         "color: rgb(39, 71, 92);\n"
                                         "background-color: rgb(255, 255, 255);")
        self.decryptedEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.decryptedEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.decryptedEdit.setLineWidth(1)
        self.decryptedEdit.setAutoFormatting(QtWidgets.QTextEdit.AutoBulletList)
        self.decryptedEdit.setObjectName("decryptedEdit")
        self.lbEncrypted = QtWidgets.QLabel(self.centralwidget)
        self.lbEncrypted.setGeometry(QtCore.QRect(0, 380, 600, 40))
        self.lbEncrypted.setStyleSheet("font: 12pt \"Roboto\";\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "background-color: rgb(175, 164, 206);")
        self.lbEncrypted.setObjectName("lbEncrypted")
        self.encryptedEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.encryptedEdit.setGeometry(QtCore.QRect(0, 420, 600, 100))
        self.encryptedEdit.setAutoFillBackground(True)
        self.encryptedEdit.setStyleSheet("font: 12pt \"Roboto\";\n"
                                         "color: rgb(39, 71, 92);\n"
                                         "background-color: rgb(255, 255, 255);")
        self.encryptedEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.encryptedEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.encryptedEdit.setLineWidth(1)
        self.encryptedEdit.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.encryptedEdit.setObjectName("encryptedEdit")
        self.lbControl = QtWidgets.QLabel(self.centralwidget)
        self.lbControl.setGeometry(QtCore.QRect(601, 240, 299, 40))
        self.lbControl.setStyleSheet("font: 12pt \"Roboto\";\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "background-color: rgb(175, 164, 206);")
        self.lbControl.setObjectName("lbControl")
        self.lbContext = QtWidgets.QLabel(self.centralwidget)
        self.lbContext.setGeometry(QtCore.QRect(0, 520, 900, 40))
        self.lbContext.setStyleSheet("font: 12pt \"Roboto\";\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "background-color: rgb(175, 164, 206);")
        self.lbContext.setObjectName("lbContext")
        self.tenthBord = QtWidgets.QLabel(self.centralwidget)
        self.tenthBord.setGeometry(QtCore.QRect(0, 159, 900, 2))
        self.tenthBord.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tenthBord.setText("")
        self.tenthBord.setObjectName("tenthBord")
        self.fifthBord = QtWidgets.QLabel(self.centralwidget)
        self.fifthBord.setGeometry(QtCore.QRect(0, 199, 900, 2))
        self.fifthBord.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fifthBord.setText("")
        self.fifthBord.setObjectName("fifthBord")
        self.seventhBord = QtWidgets.QLabel(self.centralwidget)
        self.seventhBord.setGeometry(QtCore.QRect(0, 239, 900, 2))
        self.seventhBord.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.seventhBord.setText("")
        self.seventhBord.setObjectName("seventhBord")
        self.sixthBord = QtWidgets.QLabel(self.centralwidget)
        self.sixthBord.setGeometry(QtCore.QRect(39, 200, 2, 40))
        self.sixthBord.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sixthBord.setText("")
        self.sixthBord.setObjectName("sixthBord")
        self.ninthBord = QtWidgets.QLabel(self.centralwidget)
        self.ninthBord.setGeometry(QtCore.QRect(600, 240, 2, 280))
        self.ninthBord.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ninthBord.setText("")
        self.ninthBord.setObjectName("ninthBord")
        self.eighthBord = QtWidgets.QLabel(self.centralwidget)
        self.eighthBord.setGeometry(QtCore.QRect(0, 279, 900, 2))
        self.eighthBord.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.eighthBord.setText("")
        self.eighthBord.setObjectName("eighthBord")
        self.eleventhBord = QtWidgets.QLabel(self.centralwidget)
        self.eleventhBord.setGeometry(QtCore.QRect(0, 519, 900, 2))
        self.eleventhBord.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.eleventhBord.setText("")
        self.eleventhBord.setObjectName("eleventhBord")
        self.twelfthBord = QtWidgets.QLabel(self.centralwidget)
        self.twelfthBord.setGeometry(QtCore.QRect(0, 379, 600, 2))
        self.twelfthBord.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.twelfthBord.setText("")
        self.twelfthBord.setObjectName("twelfthBord")
        self.thirteenthBord = QtWidgets.QLabel(self.centralwidget)
        self.thirteenthBord.setGeometry(QtCore.QRect(0, 419, 600, 2))
        self.thirteenthBord.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.thirteenthBord.setText("")
        self.thirteenthBord.setObjectName("thirteenthBord")
        self.backEncrypt = QtWidgets.QLabel(self.centralwidget)
        self.backEncrypt.setGeometry(QtCore.QRect(610, 290, 135, 30))
        self.backEncrypt.setStyleSheet("background-color: rgb(169, 169, 169);")
        self.backEncrypt.setText("")
        self.backEncrypt.setObjectName("backEncrypt")
        self.backDecrypt = QtWidgets.QLabel(self.centralwidget)
        self.backDecrypt.setGeometry(QtCore.QRect(755, 290, 135, 30))
        self.backDecrypt.setStyleSheet("background-color: rgb(169, 169, 169);")
        self.backDecrypt.setText("")
        self.backDecrypt.setObjectName("backDecrypt")
        self.backTextTo = QtWidgets.QLabel(self.centralwidget)
        self.backTextTo.setGeometry(QtCore.QRect(610, 425, 280, 30))
        self.backTextTo.setStyleSheet("background-color: rgb(169, 169, 169);")
        self.backTextTo.setText("")
        self.backTextTo.setObjectName("backTextTo")
        self.backTextFrom = QtWidgets.QLabel(self.centralwidget)
        self.backTextFrom.setGeometry(QtCore.QRect(610, 465, 280, 30))
        self.backTextFrom.setStyleSheet("background-color: rgb(169, 169, 169);")
        self.backTextFrom.setText("")
        self.backTextFrom.setObjectName("backTextFrom")
        self.backKeyFrom = QtWidgets.QLabel(self.centralwidget)
        self.backKeyFrom.setGeometry(QtCore.QRect(610, 385, 280, 30))
        self.backKeyFrom.setStyleSheet("background-color: rgb(169, 169, 169);")
        self.backKeyFrom.setText("")
        self.backKeyFrom.setObjectName("backKeyFrom")
        self.backKeyTo = QtWidgets.QLabel(self.centralwidget)
        self.backKeyTo.setGeometry(QtCore.QRect(610, 345, 280, 30))
        self.backKeyTo.setStyleSheet("background-color: rgb(169, 169, 169);")
        self.backKeyTo.setText("")
        self.backKeyTo.setObjectName("backKeyTo")
        self.btnEncrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btnEncrypt.setGeometry(QtCore.QRect(610, 290, 135, 30))
        self.btnEncrypt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnEncrypt.setStyleSheet("font: 12pt \"Roboto\";\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(169, 169, 169);")
        self.btnEncrypt.setFlat(True)
        self.btnEncrypt.setObjectName("btnEncrypt")
        self.btnDecrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btnDecrypt.setGeometry(QtCore.QRect(750, 290, 135, 30))
        self.btnDecrypt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnDecrypt.setStyleSheet("font: 12pt \"Roboto\";\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(169, 169, 169);")
        self.btnDecrypt.setFlat(True)
        self.btnDecrypt.setObjectName("btnDecrypt")
        self.btnGetKey = QtWidgets.QPushButton(self.centralwidget)
        self.btnGetKey.setGeometry(QtCore.QRect(610, 345, 280, 30))
        self.btnGetKey.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnGetKey.setStyleSheet("font: 12pt \"Roboto\";\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "background-color: rgb(169, 169, 169);")
        self.btnGetKey.setFlat(True)
        self.btnGetKey.setObjectName("btnGetKey")
        self.btnGetText = QtWidgets.QPushButton(self.centralwidget)
        self.btnGetText.setGeometry(QtCore.QRect(610, 385, 280, 30))
        self.btnGetText.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnGetText.setStyleSheet("font: 12pt \"Roboto\";\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(169, 169, 169);")
        self.btnGetText.setFlat(True)
        self.btnGetText.setObjectName("btnGetText")
        self.btnSaveKey = QtWidgets.QPushButton(self.centralwidget)
        self.btnSaveKey.setGeometry(QtCore.QRect(610, 425, 280, 30))
        self.btnSaveKey.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSaveKey.setStyleSheet("font: 12pt \"Roboto\";\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(169, 169, 169);")
        self.btnSaveKey.setFlat(True)
        self.btnSaveKey.setObjectName("btnSaveKey")
        self.btnSaveText = QtWidgets.QPushButton(self.centralwidget)
        self.btnSaveText.setGeometry(QtCore.QRect(610, 465, 280, 30))
        self.btnSaveText.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSaveText.setStyleSheet("font: 12pt \"Roboto\";\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "background-color: rgb(169, 169, 169);")
        self.btnSaveText.setFlat(True)
        self.btnSaveText.setObjectName("btnSaveText")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.on_click()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ElGamal Cipher"))
        self.lbPublic.setText(_translate("MainWindow", " Public Key : "))
        self.lbP.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">P :</p></body></html>"))
        self.lbG.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">G :</p></body></html>"))
        self.lbY.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Y :</p></body></html>"))
        self.lbPKey.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.lbGKey.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.lbYKey.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.lbFrom.setText(_translate("MainWindow", "From"))
        self.btnGenerate.setText(_translate("MainWindow", "Generate"))
        self.lbTo.setText(_translate("MainWindow", "to"))
        self.lbByte.setText(_translate("MainWindow", "byte"))
        self.lbPrivate.setText(_translate("MainWindow", " Private Key : "))
        self.lbX.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">X :</p></body></html>"))
        self.lbXKey.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.lbDecrypted.setText(_translate("MainWindow", " Decrypted Text : "))
        self.decryptedEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'Roboto\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.lbEncrypted.setText(_translate("MainWindow", " Encrypted Text : "))
        self.encryptedEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'Roboto\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.lbControl.setText(_translate("MainWindow", " Control Menu : "))
        self.lbContext.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">© </span>Pugachova Diana - 951002  </p></body></html>"))
        self.btnEncrypt.setText(_translate("MainWindow", "Encrypt"))
        self.btnDecrypt.setText(_translate("MainWindow", "Decrypt"))
        self.btnGetKey.setText(_translate("MainWindow", "Get Key"))
        self.btnGetText.setText(_translate("MainWindow", "Get Text"))
        self.btnSaveKey.setText(_translate("MainWindow", "Save Key"))
        self.btnSaveText.setText(_translate("MainWindow", "Save Text"))

    public_key = PublicKey
    private_key = int

    def on_click(self):
        self.btnGenerate.clicked.connect(lambda: self.generate())
        self.btnEncrypt.clicked.connect(lambda: self.encrypt())
        self.btnDecrypt.clicked.connect(lambda: self.decrypt())
        self.btnSaveKey.clicked.connect(lambda: self.save_key())
        self.btnSaveText.clicked.connect(lambda: self.save_cipher())
        self.btnGetKey.clicked.connect(lambda: self.get_key())
        self.btnGetText.clicked.connect(lambda: self.get_cipher())

    def generate(self):
        first_byte = "".join(i for i in self.firstBite.text() if i.isdigit())
        last_byte = "".join(i for i in self.lastByte.text() if i.isdigit())

        if first_byte == '':
            first = 8
        else:
            first = int(first_byte)
            if first < 8:
                first = 8

        if last_byte == '':
            last = 8
        else:
            last = int(last_byte)
            if last < 8:
                last = 8

        if first > last:
            first, last = last, first
        self.firstBite.setText(str(first))
        self.lastByte.setText(str(last))

        self.public_key, self.private_key = generate_keys(first, last)

        if len(str(self.public_key.p)) > 63:
            self.lbPKey.setText(' ' + str(self.public_key.p)[:63] + '...')
        else:
            self.lbPKey.setText(' ' + str(self.public_key.p))
        if len(str(self.public_key.g)) > 63:
            self.lbGKey.setText(' ' + str(self.public_key.g)[:63] + '...')
        else:
            self.lbGKey.setText(' ' + str(self.public_key.g))
        if len(str(self.public_key.p)) > 63:
            self.lbYKey.setText(' ' + str(self.public_key.y)[:63] + '...')
        else:
            self.lbYKey.setText(' ' + str(self.public_key.y))
        if len(str(self.public_key.p)) > 63:
            self.lbXKey.setText(' ' + str(self.private_key)[:63] + '...')
        else:
            self.lbXKey.setText(' ' + str(self.private_key))

    def encrypt(self):
        decrypted_string = self.decryptedEdit.toPlainText()
        temp = string_to_list(decrypted_string)
        string = cipher_to_string(encryption(temp, self.public_key))
        self.encryptedEdit.setPlainText(string)

    def decrypt(self):
        encrypted_string = self.encryptedEdit.toPlainText()
        temp = string_to_cipher(encrypted_string)
        string = list_to_string(decryption(temp, self.public_key, self.private_key))
        self.decryptedEdit.setPlainText(string)

    def save_key(self):
        key_to_file(self.public_key, self.private_key)

    def save_cipher(self):
        cipher_to_file(self.encryptedEdit.toPlainText())

    def get_key(self):
        self.public_key, self.private_key = key_from_file()

        if len(str(self.public_key.p)) > 75:
            self.lbPKey.setText(' ' + str(self.public_key.p)[:75] + '...')
        else:
            self.lbPKey.setText(' ' + str(self.public_key.p))
        if len(str(self.public_key.g)) > 75:
            self.lbGKey.setText(' ' + str(self.public_key.g)[:75] + '...')
        else:
            self.lbGKey.setText(' ' + str(self.public_key.g))
        if len(str(self.public_key.p)) > 75:
            self.lbYKey.setText(' ' + str(self.public_key.y)[:75] + '...')
        else:
            self.lbYKey.setText(' ' + str(self.public_key.y))
        if len(str(self.public_key.p)) > 75:
            self.lbXKey.setText(' ' + str(self.private_key)[:75] + '...')
        else:
            self.lbXKey.setText(' ' + str(self.private_key))

    def get_cipher(self):
        self.encryptedEdit.setPlainText(cipher_from_file())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
