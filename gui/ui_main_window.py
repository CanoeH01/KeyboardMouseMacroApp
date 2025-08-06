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
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_formMain(object):
    def setupUi(self, formMain):
        if not formMain.objectName():
            formMain.setObjectName(u"formMain")
        formMain.resize(400, 300)
        self.gridLayout = QGridLayout(formMain)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tblSavedMacros = QTableWidget(formMain)
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

        self.gridLayout.addWidget(self.tblSavedMacros, 1, 2, 1, 2)

        self.btnRecordNewMacro = QPushButton(formMain)
        self.btnRecordNewMacro.setObjectName(u"btnRecordNewMacro")

        self.gridLayout.addWidget(self.btnRecordNewMacro, 0, 3, 1, 1)


        self.retranslateUi(formMain)

        QMetaObject.connectSlotsByName(formMain)
    # setupUi

    def retranslateUi(self, formMain):
        formMain.setWindowTitle(QCoreApplication.translate("formMain", u"Form", None))
        self.btnRecordNewMacro.setText(QCoreApplication.translate("formMain", u"Record New Macro", None))
    # retranslateUi

