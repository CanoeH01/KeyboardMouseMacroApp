# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_macro.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QSizePolicy,
    QTreeWidget, QTreeWidgetItem, QWidget)

class Ui_formEdit(object):
    def setupUi(self, formEdit):
        if not formEdit.objectName():
            formEdit.setObjectName(u"formEdit")
        formEdit.resize(400, 300)
        self.gridLayout = QGridLayout(formEdit)
        self.gridLayout.setObjectName(u"gridLayout")
        self.treeMacroData = QTreeWidget(formEdit)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeMacroData.setHeaderItem(__qtreewidgetitem)
        self.treeMacroData.setObjectName(u"treeMacroData")

        self.gridLayout.addWidget(self.treeMacroData, 0, 0, 1, 1)


        self.retranslateUi(formEdit)

        QMetaObject.connectSlotsByName(formEdit)
    # setupUi

    def retranslateUi(self, formEdit):
        formEdit.setWindowTitle(QCoreApplication.translate("formEdit", u"Edit Macro", None))
    # retranslateUi

