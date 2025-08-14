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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QSizePolicy, QTreeWidget, QTreeWidgetItem, QWidget)

class Ui_formEdit(object):
    def setupUi(self, formEdit):
        if not formEdit.objectName():
            formEdit.setObjectName(u"formEdit")
        formEdit.resize(400, 300)
        self.gridLayout = QGridLayout(formEdit)
        self.gridLayout.setObjectName(u"gridLayout")
        self.treeMacroData = QTreeWidget(formEdit)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setTextAlignment(2, Qt.AlignCenter);
        __qtreewidgetitem.setTextAlignment(1, Qt.AlignCenter);
        __qtreewidgetitem.setTextAlignment(0, Qt.AlignCenter);
        self.treeMacroData.setHeaderItem(__qtreewidgetitem)
        self.treeMacroData.setObjectName(u"treeMacroData")
        self.treeMacroData.setStyleSheet(u"    QTreeWidget::item {\n"
"        padding-top: 3px;\n"
"		 padding-bottom: 3px;    \n"
"    }\n"
"")
        self.treeMacroData.setAnimated(True)
        self.treeMacroData.setColumnCount(3)
        self.treeMacroData.header().setVisible(True)

        self.gridLayout.addWidget(self.treeMacroData, 1, 0, 1, 1)

        self.lblMacroName = QLabel(formEdit)
        self.lblMacroName.setObjectName(u"lblMacroName")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.lblMacroName.setFont(font)

        self.gridLayout.addWidget(self.lblMacroName, 0, 0, 1, 1)


        self.retranslateUi(formEdit)

        QMetaObject.connectSlotsByName(formEdit)
    # setupUi

    def retranslateUi(self, formEdit):
        formEdit.setWindowTitle(QCoreApplication.translate("formEdit", u"Edit Macro", None))
        ___qtreewidgetitem = self.treeMacroData.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("formEdit", u"Details", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("formEdit", u"Action", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("formEdit", u"Step", None));
        self.lblMacroName.setText(QCoreApplication.translate("formEdit", u"[MacroName]", None))
    # retranslateUi

