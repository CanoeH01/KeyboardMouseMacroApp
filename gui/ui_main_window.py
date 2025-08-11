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
    QLabel, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

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

        self.gridLayout.addWidget(self.tblSavedMacros, 1, 0, 1, 2)

        self.btnOptions = QPushButton(formMain)
        self.btnOptions.setObjectName(u"btnOptions")

        self.gridLayout.addWidget(self.btnOptions, 0, 2, 1, 1)

        self.btnRecordNewMacro = QPushButton(formMain)
        self.btnRecordNewMacro.setObjectName(u"btnRecordNewMacro")

        self.gridLayout.addWidget(self.btnRecordNewMacro, 0, 1, 1, 1)

        self.lblSavedMacros = QLabel(formMain)
        self.lblSavedMacros.setObjectName(u"lblSavedMacros")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.lblSavedMacros.setFont(font)

        self.gridLayout.addWidget(self.lblSavedMacros, 0, 0, 1, 1)

        self.btnPlayMacro = QPushButton(formMain)
        self.btnPlayMacro.setObjectName(u"btnPlayMacro")
        self.btnPlayMacro.setEnabled(False)

        self.gridLayout.addWidget(self.btnPlayMacro, 2, 0, 1, 1)

        self.btnDeleteMacro = QPushButton(formMain)
        self.btnDeleteMacro.setObjectName(u"btnDeleteMacro")
        self.btnDeleteMacro.setEnabled(False)

        self.gridLayout.addWidget(self.btnDeleteMacro, 2, 1, 1, 1)


        self.retranslateUi(formMain)

        QMetaObject.connectSlotsByName(formMain)
    # setupUi

    def retranslateUi(self, formMain):
        formMain.setWindowTitle(QCoreApplication.translate("formMain", u"Macro Manager", None))
        self.btnOptions.setText(QCoreApplication.translate("formMain", u"\u2699\ufe0fOptions", None))
        self.btnRecordNewMacro.setText(QCoreApplication.translate("formMain", u"Record New Macro", None))
        self.lblSavedMacros.setText(QCoreApplication.translate("formMain", u"Saved Macros", None))
        self.btnPlayMacro.setText(QCoreApplication.translate("formMain", u"Play", None))
        self.btnDeleteMacro.setText(QCoreApplication.translate("formMain", u"Delete", None))
    # retranslateUi

