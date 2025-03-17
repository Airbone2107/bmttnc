import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "../platforms"
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1051, 442)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 0, 311, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(560, 90, 111, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 210, 111, 16))
        self.label_4.setObjectName("label_4")
        self.btn_encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_encrypt.setGeometry(QtCore.QRect(160, 310, 93, 28))
        self.btn_encrypt.setObjectName("btn_encrypt")
        self.btn_decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_decrypt.setGeometry(QtCore.QRect(380, 310, 93, 28))
        self.btn_decrypt.setObjectName("btn_decrypt")
        self.btn_gen_keys = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gen_keys.setGeometry(QtCore.QRect(640, 30, 93, 28))
        self.btn_gen_keys.setObjectName("btn_gen_keys")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(560, 210, 111, 16))
        self.label_5.setObjectName("label_5")
        self.btn_sign = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sign.setGeometry(QtCore.QRect(680, 310, 93, 28))
        self.btn_sign.setObjectName("btn_sign")
        self.btn_verify = QtWidgets.QPushButton(self.centralwidget)
        self.btn_verify.setGeometry(QtCore.QRect(860, 310, 93, 28))
        self.btn_verify.setObjectName("btn_verify")
        self.txt_cipher_text = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_cipher_text.setGeometry(QtCore.QRect(140, 210, 351, 91))
        self.txt_cipher_text.setObjectName("txt_cipher_text")
        self.txt_sign = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_sign.setGeometry(QtCore.QRect(650, 210, 351, 91))
        self.txt_sign.setObjectName("txt_sign")
        self.txt_plain_text = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_plain_text.setGeometry(QtCore.QRect(140, 90, 351, 91))
        self.txt_plain_text.setObjectName("txt_plain_text")
        self.txt_info = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_info.setGeometry(QtCore.QRect(650, 90, 351, 91))
        self.txt_info.setObjectName("txt_info")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1051, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "RSA CIPHER"))
        self.label_2.setText(_translate("MainWindow", "Plan Text:"))
        self.label_3.setText(_translate("MainWindow", "Information:"))
        self.label_4.setText(_translate("MainWindow", "Cipher Text:"))
        self.btn_encrypt.setText(_translate("MainWindow", "Encrypt"))
        self.btn_decrypt.setText(_translate("MainWindow", "Decrypt"))
        self.btn_gen_keys.setText(_translate("MainWindow", "Generate Keys"))
        self.label_5.setText(_translate("MainWindow", "Signature:"))
        self.btn_sign.setText(_translate("MainWindow", "Sign"))
        self.btn_verify.setText(_translate("MainWindow", "Verify"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
