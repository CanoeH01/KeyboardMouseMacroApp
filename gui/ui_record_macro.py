# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'record_macro.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_formRecord(object):
    def setupUi(self, formRecord):
        if not formRecord.objectName():
            formRecord.setObjectName(u"formRecord")
        formRecord.resize(180, 100)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(formRecord.sizePolicy().hasHeightForWidth())
        formRecord.setSizePolicy(sizePolicy)
        formRecord.setMinimumSize(QSize(180, 100))
        formRecord.setMaximumSize(QSize(180, 100))
        self.gridLayout = QGridLayout(formRecord)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnRecord = QPushButton(formRecord)
        self.btnRecord.setObjectName(u"btnRecord")

        self.gridLayout.addWidget(self.btnRecord, 0, 0, 1, 2)

        self.btnReplay = QPushButton(formRecord)
        self.btnReplay.setObjectName(u"btnReplay")
        self.btnReplay.setEnabled(False)

        self.gridLayout.addWidget(self.btnReplay, 0, 2, 1, 1)

        self.btnSave = QPushButton(formRecord)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnSave.sizePolicy().hasHeightForWidth())
        self.btnSave.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.btnSave, 2, 0, 1, 3)

        self.lblStopRecording = QLabel(formRecord)
        self.lblStopRecording.setObjectName(u"lblStopRecording")

        self.gridLayout.addWidget(self.lblStopRecording, 3, 0, 1, 3)


        self.retranslateUi(formRecord)

        QMetaObject.connectSlotsByName(formRecord)
    # setupUi

    def retranslateUi(self, formRecord):
        formRecord.setWindowTitle(QCoreApplication.translate("formRecord", u"Create Macro", None))
        self.btnRecord.setText(QCoreApplication.translate("formRecord", u"Record", None))
        self.btnReplay.setText(QCoreApplication.translate("formRecord", u"Replay", None))
        self.btnSave.setText(QCoreApplication.translate("formRecord", u"Save", None))
        self.lblStopRecording.setText("")
    # retranslateUi

