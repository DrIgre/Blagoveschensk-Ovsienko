# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Перваяюишка.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)
import resourced_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(776, 506)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 80, 761, 41))
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 20, 361, 41))
        self.label_2.setFont(font)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 140, 151, 61))
        font1 = QFont()
        font1.setPointSize(40)
        self.label_3.setFont(font1)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(180, 130, 315, 41))
        self.label_4.setFont(font)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 210, 301, 41))
        self.label_5.setFont(font)
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(340, 210, 351, 41))
        self.label_6.setFont(font)
        self.back = QLabel(Form)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(0, 0, 831, 531))
        self.back.setStyleSheet(u"")
        self.back.setPixmap(QPixmap(u":/image/resourced/image/background.jpg"))
        self.back.setScaledContents(True)
        self.back.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0421\u0435\u0439\u0447\u0430\u0441 00:00. \u0412\u0447\u0435\u0440\u0430 \u0432 \u044d\u0442\u043e \u0432\u0440\u0435\u043c\u044f \u0431\u044b\u043b\u043e 0", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0413\u043e\u0440\u043e\u0434:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"0\u00b0", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u041f\u0430\u0441\u043c\u0443\u0440\u043d\u043e", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u0412\u0435\u0442\u0435\u0440:", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u0412\u043b\u0430\u0436\u043d\u043e\u0441\u0442\u044c:", None))
        self.back.setText("")
    # retranslateUi

