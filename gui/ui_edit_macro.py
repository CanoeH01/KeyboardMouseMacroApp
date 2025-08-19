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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QGridLayout,
    QHeaderView, QKeySequenceEdit, QLabel, QLineEdit,
    QRadioButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStackedWidget, QTreeWidget, QTreeWidgetItem, QWidget)

class Ui_formEdit(object):
    def setupUi(self, formEdit):
        if not formEdit.objectName():
            formEdit.setObjectName(u"formEdit")
        formEdit.resize(475, 300)
        self.gridLayout = QGridLayout(formEdit)
        self.gridLayout.setObjectName(u"gridLayout")
        self.treeMacroData = QTreeWidget(formEdit)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setTextAlignment(2, Qt.AlignCenter);
        __qtreewidgetitem.setTextAlignment(1, Qt.AlignCenter);
        __qtreewidgetitem.setTextAlignment(0, Qt.AlignCenter);
        self.treeMacroData.setHeaderItem(__qtreewidgetitem)
        self.treeMacroData.setObjectName(u"treeMacroData")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeMacroData.sizePolicy().hasHeightForWidth())
        self.treeMacroData.setSizePolicy(sizePolicy)
        self.treeMacroData.setStyleSheet(u"    QTreeWidget::item {\n"
"        padding-top: 3px;\n"
"		 padding-bottom: 3px;    \n"
"    }\n"
"")
        self.treeMacroData.setAnimated(True)
        self.treeMacroData.setColumnCount(3)
        self.treeMacroData.header().setVisible(True)

        self.gridLayout.addWidget(self.treeMacroData, 2, 0, 1, 2)

        self.lblMacroName = QLabel(formEdit)
        self.lblMacroName.setObjectName(u"lblMacroName")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.lblMacroName.setFont(font)

        self.gridLayout.addWidget(self.lblMacroName, 0, 0, 1, 1)

        self.stckEditor = QStackedWidget(formEdit)
        self.stckEditor.setObjectName(u"stckEditor")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(4)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stckEditor.sizePolicy().hasHeightForWidth())
        self.stckEditor.setSizePolicy(sizePolicy1)
        self.pgEmpty = QWidget()
        self.pgEmpty.setObjectName(u"pgEmpty")
        self.gridLayout_10 = QGridLayout(self.pgEmpty)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label = QLabel(self.pgEmpty)
        self.label.setObjectName(u"label")

        self.gridLayout_10.addWidget(self.label, 0, 0, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(117, 213, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_9, 1, 0, 1, 1)

        self.stckEditor.addWidget(self.pgEmpty)
        self.pgMouseMove = QWidget()
        self.pgMouseMove.setObjectName(u"pgMouseMove")
        self.gridLayout_7 = QGridLayout(self.pgMouseMove)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.numMoveY = QDoubleSpinBox(self.pgMouseMove)
        self.numMoveY.setObjectName(u"numMoveY")

        self.gridLayout_7.addWidget(self.numMoveY, 1, 1, 1, 1)

        self.lblMoveX = QLabel(self.pgMouseMove)
        self.lblMoveX.setObjectName(u"lblMoveX")

        self.gridLayout_7.addWidget(self.lblMoveX, 0, 0, 1, 1)

        self.numMoveX = QDoubleSpinBox(self.pgMouseMove)
        self.numMoveX.setObjectName(u"numMoveX")
        self.numMoveX.setWrapping(False)

        self.gridLayout_7.addWidget(self.numMoveX, 0, 1, 1, 1)

        self.lblMoveY = QLabel(self.pgMouseMove)
        self.lblMoveY.setObjectName(u"lblMoveY")

        self.gridLayout_7.addWidget(self.lblMoveY, 1, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_6, 2, 1, 1, 1)

        self.stckEditor.addWidget(self.pgMouseMove)
        self.pgMouseClick = QWidget()
        self.pgMouseClick.setObjectName(u"pgMouseClick")
        self.gridLayout_6 = QGridLayout(self.pgMouseClick)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_5, 5, 1, 1, 1)

        self.lblClickY = QLabel(self.pgMouseClick)
        self.lblClickY.setObjectName(u"lblClickY")

        self.gridLayout_6.addWidget(self.lblClickY, 1, 0, 1, 1)

        self.radioButton_2 = QRadioButton(self.pgMouseClick)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout_6.addWidget(self.radioButton_2, 3, 1, 1, 1)

        self.numClickX = QDoubleSpinBox(self.pgMouseClick)
        self.numClickX.setObjectName(u"numClickX")

        self.gridLayout_6.addWidget(self.numClickX, 0, 1, 1, 1)

        self.lblCLickX = QLabel(self.pgMouseClick)
        self.lblCLickX.setObjectName(u"lblCLickX")

        self.gridLayout_6.addWidget(self.lblCLickX, 0, 0, 1, 1)

        self.numClickY = QDoubleSpinBox(self.pgMouseClick)
        self.numClickY.setObjectName(u"numClickY")

        self.gridLayout_6.addWidget(self.numClickY, 1, 1, 1, 1)

        self.radioButton = QRadioButton(self.pgMouseClick)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout_6.addWidget(self.radioButton, 2, 1, 1, 1)

        self.stckEditor.addWidget(self.pgMouseClick)
        self.pgMouseScroll = QWidget()
        self.pgMouseScroll.setObjectName(u"pgMouseScroll")
        self.gridLayout_2 = QGridLayout(self.pgMouseScroll)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.radioButton_3 = QRadioButton(self.pgMouseScroll)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.gridLayout_2.addWidget(self.radioButton_3, 0, 1, 1, 1)

        self.radioButton_4 = QRadioButton(self.pgMouseScroll)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.gridLayout_2.addWidget(self.radioButton_4, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 3, 1, 1, 1)

        self.stckEditor.addWidget(self.pgMouseScroll)
        self.pgKeyPress = QWidget()
        self.pgKeyPress.setObjectName(u"pgKeyPress")
        self.gridLayout_3 = QGridLayout(self.pgKeyPress)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.seqKeyPressed = QKeySequenceEdit(self.pgKeyPress)
        self.seqKeyPressed.setObjectName(u"seqKeyPressed")
        self.seqKeyPressed.setClearButtonEnabled(False)

        self.gridLayout_3.addWidget(self.seqKeyPressed, 1, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.lblKeyPressed = QLabel(self.pgKeyPress)
        self.lblKeyPressed.setObjectName(u"lblKeyPressed")
        self.lblKeyPressed.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.lblKeyPressed, 0, 1, 1, 1)

        self.stckEditor.addWidget(self.pgKeyPress)
        self.pgKeyRelease = QWidget()
        self.pgKeyRelease.setObjectName(u"pgKeyRelease")
        self.gridLayout_4 = QGridLayout(self.pgKeyRelease)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lblKeyReleased = QLabel(self.pgKeyRelease)
        self.lblKeyReleased.setObjectName(u"lblKeyReleased")

        self.gridLayout_4.addWidget(self.lblKeyReleased, 0, 0, 1, 1)

        self.seqKeyReleased = QKeySequenceEdit(self.pgKeyRelease)
        self.seqKeyReleased.setObjectName(u"seqKeyReleased")
        self.seqKeyReleased.setClearButtonEnabled(False)

        self.gridLayout_4.addWidget(self.seqKeyReleased, 1, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 2, 0, 1, 1)

        self.stckEditor.addWidget(self.pgKeyRelease)
        self.pgIf = QWidget()
        self.pgIf.setObjectName(u"pgIf")
        self.gridLayout_5 = QGridLayout(self.pgIf)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_4, 5, 1, 1, 1)

        self.lblIf = QLabel(self.pgIf)
        self.lblIf.setObjectName(u"lblIf")

        self.gridLayout_5.addWidget(self.lblIf, 0, 1, 1, 1)

        self.cmbOperator = QComboBox(self.pgIf)
        self.cmbOperator.addItem("")
        self.cmbOperator.addItem("")
        self.cmbOperator.addItem("")
        self.cmbOperator.addItem("")
        self.cmbOperator.addItem("")
        self.cmbOperator.addItem("")
        self.cmbOperator.addItem("")
        self.cmbOperator.addItem("")
        self.cmbOperator.addItem("")
        self.cmbOperator.setObjectName(u"cmbOperator")

        self.gridLayout_5.addWidget(self.cmbOperator, 3, 1, 1, 1)

        self.cmbSelectObject = QComboBox(self.pgIf)
        self.cmbSelectObject.setObjectName(u"cmbSelectObject")

        self.gridLayout_5.addWidget(self.cmbSelectObject, 2, 1, 1, 1)

        self.lnConditionValue = QLineEdit(self.pgIf)
        self.lnConditionValue.setObjectName(u"lnConditionValue")

        self.gridLayout_5.addWidget(self.lnConditionValue, 4, 1, 1, 1)

        self.stckEditor.addWidget(self.pgIf)
        self.pgSetVariable = QWidget()
        self.pgSetVariable.setObjectName(u"pgSetVariable")
        self.gridLayout_8 = QGridLayout(self.pgSetVariable)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.lnVariableValue = QLineEdit(self.pgSetVariable)
        self.lnVariableValue.setObjectName(u"lnVariableValue")

        self.gridLayout_8.addWidget(self.lnVariableValue, 1, 0, 1, 1)

        self.lnVariableName = QLineEdit(self.pgSetVariable)
        self.lnVariableName.setObjectName(u"lnVariableName")

        self.gridLayout_8.addWidget(self.lnVariableName, 0, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_7, 2, 0, 1, 1)

        self.stckEditor.addWidget(self.pgSetVariable)
        self.pgIncrementVariable = QWidget()
        self.pgIncrementVariable.setObjectName(u"pgIncrementVariable")
        self.gridLayout_9 = QGridLayout(self.pgIncrementVariable)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.lblIncrementBy = QLabel(self.pgIncrementVariable)
        self.lblIncrementBy.setObjectName(u"lblIncrementBy")

        self.gridLayout_9.addWidget(self.lblIncrementBy, 0, 0, 1, 1)

        self.spnIncrementAmount = QSpinBox(self.pgIncrementVariable)
        self.spnIncrementAmount.setObjectName(u"spnIncrementAmount")

        self.gridLayout_9.addWidget(self.spnIncrementAmount, 1, 0, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_8, 2, 0, 1, 1)

        self.stckEditor.addWidget(self.pgIncrementVariable)

        self.gridLayout.addWidget(self.stckEditor, 2, 3, 1, 1)


        self.retranslateUi(formEdit)

        self.stckEditor.setCurrentIndex(0)
        self.cmbOperator.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(formEdit)
    # setupUi

    def retranslateUi(self, formEdit):
        formEdit.setWindowTitle(QCoreApplication.translate("formEdit", u"Edit Macro", None))
        ___qtreewidgetitem = self.treeMacroData.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("formEdit", u"Details", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("formEdit", u"Action", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("formEdit", u"Step", None));
        self.lblMacroName.setText(QCoreApplication.translate("formEdit", u"[MacroName]", None))
        self.label.setText(QCoreApplication.translate("formEdit", u" Step Options", None))
        self.lblMoveX.setText(QCoreApplication.translate("formEdit", u" x", None))
        self.lblMoveY.setText(QCoreApplication.translate("formEdit", u" y", None))
        self.lblClickY.setText(QCoreApplication.translate("formEdit", u" y", None))
        self.radioButton_2.setText(QCoreApplication.translate("formEdit", u"Right Click", None))
        self.lblCLickX.setText(QCoreApplication.translate("formEdit", u" x", None))
        self.radioButton.setText(QCoreApplication.translate("formEdit", u"Left Click", None))
        self.radioButton_3.setText(QCoreApplication.translate("formEdit", u"Up", None))
        self.radioButton_4.setText(QCoreApplication.translate("formEdit", u"Down", None))
        self.lblKeyPressed.setText(QCoreApplication.translate("formEdit", u" Key Pressed", None))
        self.lblKeyReleased.setText(QCoreApplication.translate("formEdit", u" Key Released", None))
        self.lblIf.setText(QCoreApplication.translate("formEdit", u" IF", None))
        self.cmbOperator.setItemText(0, QCoreApplication.translate("formEdit", u"==", None))
        self.cmbOperator.setItemText(1, QCoreApplication.translate("formEdit", u"!=", None))
        self.cmbOperator.setItemText(2, QCoreApplication.translate("formEdit", u">=", None))
        self.cmbOperator.setItemText(3, QCoreApplication.translate("formEdit", u">", None))
        self.cmbOperator.setItemText(4, QCoreApplication.translate("formEdit", u"<=", None))
        self.cmbOperator.setItemText(5, QCoreApplication.translate("formEdit", u"<", None))
        self.cmbOperator.setItemText(6, QCoreApplication.translate("formEdit", u"contains", None))
        self.cmbOperator.setItemText(7, QCoreApplication.translate("formEdit", u"!contains", None))
        self.cmbOperator.setItemText(8, "")

        self.cmbOperator.setPlaceholderText(QCoreApplication.translate("formEdit", u"comparison", None))
        self.cmbSelectObject.setPlaceholderText(QCoreApplication.translate("formEdit", u"object", None))
        self.lnConditionValue.setPlaceholderText(QCoreApplication.translate("formEdit", u"value", None))
        self.lnVariableValue.setPlaceholderText(QCoreApplication.translate("formEdit", u"value", None))
        self.lnVariableName.setPlaceholderText(QCoreApplication.translate("formEdit", u"name", None))
        self.lblIncrementBy.setText(QCoreApplication.translate("formEdit", u"Increment By", None))
    # retranslateUi

