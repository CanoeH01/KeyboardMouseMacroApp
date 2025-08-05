# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QListView,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(264, 148)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lblRecording = QLabel(Form)
        self.lblRecording.setObjectName(u"lblRecording")

        self.gridLayout.addWidget(self.lblRecording, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 5, 2, 1, 1)

        self.btnRecord = QPushButton(Form)
        self.btnRecord.setObjectName(u"btnRecord")

        self.gridLayout.addWidget(self.btnRecord, 1, 0, 1, 1)

        self.btnReplay = QPushButton(Form)
        self.btnReplay.setObjectName(u"btnReplay")
        self.btnReplay.setEnabled(False)

        self.gridLayout.addWidget(self.btnReplay, 5, 0, 1, 1)

        self.btnSave = QPushButton(Form)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setEnabled(False)

        self.gridLayout.addWidget(self.btnSave, 6, 0, 1, 1)

        self.lstSavedMacros = QListView(Form)
        self.lstSavedMacros.setObjectName(u"lstSavedMacros")

        self.gridLayout.addWidget(self.lstSavedMacros, 6, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lblRecording.setText("")
        self.btnRecord.setText(QCoreApplication.translate("Form", u"Record", None))
        self.btnReplay.setText(QCoreApplication.translate("Form", u"Replay", None))
        self.btnSave.setText(QCoreApplication.translate("Form", u"Save", None))
    # retranslateUi

