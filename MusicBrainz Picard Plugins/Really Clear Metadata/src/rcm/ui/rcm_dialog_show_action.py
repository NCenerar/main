# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/rcm/ui/rcm_dialog_show_action.ui'
#
# Created: Tue Jan 20 14:27:59 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_NiCeDialog_show(object):
    def setupUi(self, NiCeDialog_show):
        NiCeDialog_show.setObjectName(_fromUtf8("NiCeDialog_show"))
        NiCeDialog_show.resize(400, 100)
        self.vboxlayout = QtGui.QVBoxLayout(NiCeDialog_show)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.label = QtGui.QLabel(NiCeDialog_show)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.vboxlayout.addWidget(self.label)

        self.retranslateUi(NiCeDialog_show)
        QtCore.QMetaObject.connectSlotsByName(NiCeDialog_show)

    def retranslateUi(self, NiCeDialog_show):
        NiCeDialog_show.setWindowTitle(_translate("NiCeDialog_show", "Nicolas Cenerario Qt Dialog", None))
        self.label.setText(_translate("NiCeDialog_show", "TextLabel", None))

