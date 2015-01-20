#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui

from ui.rcm_dialog_show_action import Ui_NiCeDialog_show

class NiCeDialog_show(QtGui.QDialog):
	def __init__(self):
		super(NiCeDialog_show, self).__init__()
		self._ui = Ui_NiCeDialog_show()
		self._ui.setupUi(self)
	def setText(self, text):
		self._ui.label.setText(text)
