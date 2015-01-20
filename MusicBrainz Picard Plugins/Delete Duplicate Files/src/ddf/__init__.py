#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

PLUGIN_NAME = "Delete Duplicate Files"
PLUGIN_AUTHOR = "Nicolas Cenerario"
PLUGIN_DESCRIPTION = "If you are like me, you have a lot of duplicate files on your hard drive. \
I'm doing so many backup that in the end, I get a lot of duplicates. \
But the time has come to organize my music library and I cannot let duplicates mess up my library. \
I want to tag and organize my music so that I can build a clean library. \
That's why I developed this plugin. \
After adding my files into MusicBrainz Picard, I have a context menu action that find and delete duplicate files."
PLUGIN_VERSION = "0.1"
PLUGIN_API_VERSIONS = ["0.9.0", "0.10", "0.15"]

from PyQt4 import QtCore

from ddf_models import NiCeFileAction
from ddf_views import NiCeSelectAndConfirmDialog
from ddf_controllers import NiCeThreadClearMetadata, NiCeThreadEmitFiles

#===============================================================================
# NiCeFileActionClearMetadata
#===============================================================================
class NiCeFileActionClearMetadata(NiCeFileAction):
	NAME = "Delete Duplicate Files"
	def callback_prev(self, obj):
		dialog = None  # NiCeDialog_show()
		@QtCore.pyqtSlot(str)
		def setTextIntoView(f):
			dialog.setText(dialog.tr("Clearing metadata: {0}".format(f)))
		@QtCore.pyqtSlot()
		def closeDialog():
			dialog.accept()
		thread_action = NiCeThreadClearMetadata([f.filename for o in obj for f in o.iterfiles()])
		@QtCore.pyqtSlot()
		def interruptThread():
			thread_action.interrupt()
		dialog.rejected.connect(interruptThread)
		thread_action.itemProcessed.connect(setTextIntoView)
		thread_action.finished.connect(closeDialog)
		dialog.show()
		thread_action.start()
		return dialog.exec_()

	def callback(self, obj):
		dialog = NiCeSelectAndConfirmDialog()
		dialog.setTitle(self.tr("<html><head/><body><p><span style='font-size:18pt; font-weight:600;'>Clear metadata from this files?</span></p></body></html>"))
		thread_fill = NiCeThreadEmitFiles([f.filename for o in obj for f in o.iterfiles()])
		dialog.rejected.connect(thread_fill.interrupt)

		@QtCore.pyqtSlot(str)
		def addFileIntoView(f):
			dialog.addItem(f)
			dialog.setText(dialog.tr("Adding file: {0}".format(f)))
		thread_fill.itemProcessed.connect(addFileIntoView)

		@QtCore.pyqtSlot()
		def startFillingThread():
			@QtCore.pyqtSlot()
			def pauseFillingThread():
				thread_fill.pause()
				dialog.connectOui(resumeFillingThread, self.tr("Resume"))
				dialog.connectNon(dialog.reject, self.tr("Close"))
			@QtCore.pyqtSlot()
			def resumeFillingThread():
				thread_fill.resume()
				dialog.connectOui()
				dialog.connectNon(pauseFillingThread, self.tr("Pause"))
			dialog.connectOui()
			dialog.connectNon(pauseFillingThread, self.tr("Pause"))
		@QtCore.pyqtSlot()
		def finishFillingThread():
			dialog.connectOui(startDeletingThread, self.tr("Clear metadata"))
			dialog.connectNon(dialog.reject, self.tr("Close"))
			dialog.setText("")
		thread_fill.started.connect(startFillingThread)
		thread_fill.finished.connect(finishFillingThread)

		@QtCore.pyqtSlot()
		def startDeletingThread():
			thread_delete = NiCeThreadClearMetadata([f.text() for f in dialog.iterModel() if f.checkState() == QtCore.Qt.Checked])
			@QtCore.pyqtSlot(str, int)
			def addInfoIntoView(f):
				print dialog.tr("Clearing metadata: {0}".format(f))
				dialog.setText(dialog.tr("Clearing metadata: {0}".format(f)))
			thread_delete.itemProcessed.connect(addInfoIntoView)
			@QtCore.pyqtSlot()
			def pauseDeletingThread():
				thread_delete.pause()
				dialog.connectOui(resumeDeletingThread, self.tr("Resume"))
				dialog.connectNon(dialog.reject, self.tr("Close"))
			@QtCore.pyqtSlot()
			def resumeDeletingThread():
				thread_delete.resume()
				dialog.connectOui()
				dialog.connectNon(pauseDeletingThread, self.tr("Pause"))
			@QtCore.pyqtSlot()
			def finishDeletingThread():
				dialog.connectOui(dialog.accept, self.tr("Close"))
				dialog.connectNon()
				# dialog.accept()
			thread_delete.finished.connect(finishDeletingThread)
			dialog.connectOui()
			dialog.connectNon(pauseDeletingThread, self.tr("Pause"))
			thread_delete.start()

		thread_fill.start()
		return dialog.exec_()

#===============================================================================
# Initializing
#===============================================================================
my_plugin_1 = NiCeFileActionClearMetadata()
