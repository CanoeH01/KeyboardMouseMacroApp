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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(383, 221)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lblRecording = QLabel(Form)
        self.lblRecording.setObjectName(u"lblRecording")

        self.gridLayout.addWidget(self.lblRecording, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 6, 1, 1, 1)

        self.btnRecord = QPushButton(Form)
        self.btnRecord.setObjectName(u"btnRecord")

        self.gridLayout.addWidget(self.btnRecord, 1, 0, 1, 1)

        self.btnReplay = QPushButton(Form)
        self.btnReplay.setObjectName(u"btnReplay")
        self.btnReplay.setEnabled(False)

        self.gridLayout.addWidget(self.btnReplay, 6, 0, 1, 1)

        self.btnSave = QPushButton(Form)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setEnabled(False)

        self.gridLayout.addWidget(self.btnSave, 7, 0, 1, 1)

        self.tblSavedMacros = QTableWidget(Form)
        if (self.tblSavedMacros.columnCount() < 2):
            self.tblSavedMacros.setColumnCount(2)
        self.tblSavedMacros.setObjectName(u"tblSavedMacros")
        self.tblSavedMacros.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.tblSavedMacros.setAutoFillBackground(False)
        self.tblSavedMacros.setStyleSheet(u"")
        self.tblSavedMacros.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tblSavedMacros.setProperty(u"showDropIndicator", False)
        self.tblSavedMacros.setDragDropOverwriteMode(False)
        self.tblSavedMacros.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tblSavedMacros.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tblSavedMacros.setShowGrid(False)
        self.tblSavedMacros.setGridStyle(Qt.PenStyle.SolidLine)
        self.tblSavedMacros.setSortingEnabled(False)
        self.tblSavedMacros.setColumnCount(2)
        self.tblSavedMacros.horizontalHeader().setVisible(False)
        self.tblSavedMacros.horizontalHeader().setCascadingSectionResizes(False)
        self.tblSavedMacros.horizontalHeader().setDefaultSectionSize(100)
        self.tblSavedMacros.horizontalHeader().setHighlightSections(False)
        self.tblSavedMacros.horizontalHeader().setStretchLastSection(True)
        self.tblSavedMacros.verticalHeader().setVisible(False)
        self.tblSavedMacros.verticalHeader().setDefaultSectionSize(32)

        self.gridLayout.addWidget(self.tblSavedMacros, 7, 1, 1, 1)


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

