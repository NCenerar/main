#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from os import path
from threading import Lock
from PyQt4 import QtCore

import mutagen

#===============================================================================
# NiCeThreadProcessStrList
#===============================================================================
class NiCeThreadProcessStrList(QtCore.QThread):
	_itemProcessed = QtCore.pyqtSignal(str)
	def __init__(self, l):
		super(NiCeThreadProcessStrList, self).__init__()
		self._lock = Lock()
		self._interrupt = False
		self._pause = False
		self._list = l

	@property
	def itemProcessed(self):
		with (self._lock):
			return self._itemProcessed

	def isInterrupted(self):
		with (self._lock):
			return self._interrupt

	def isPaused(self):
		with (self._lock):
			return self._pause and not self._interrupt

	def interrupt(self):
		with (self._lock):
			self._interrupt = True

	def pause(self):
		with (self._lock):
			self._pause = True

	def resume(self):
		with (self._lock):
			self._pause = False

	def run(self):
		for item in self._list:
			while self.isPaused():
				QtCore.QThread.msleep(50)
			if self.isInterrupted():
				break
			else:
				self.itemProcessed.emit(self.processItem(item))

	def processItem(self, item):
		return "Nothing has been done with {0}.".format(item)

#===============================================================================
# NiCeThreadClearMetadata
#===============================================================================
class NiCeThreadClearMetadata(NiCeThreadProcessStrList):
	def processItem(self, item):
		try:
			if path.isfile(item):
				t = mutagen.File(item)
				t.delete()
				t.save()
				return "{0} metadata has been cleared.".format(item)
			else:
				return "{0} is not a file.".format(item)
		except Exception:
			return "{0} has raised an exception.".format(item)
