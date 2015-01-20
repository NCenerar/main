#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

PLUGIN_NAME = "Really Clear Metadata"
PLUGIN_AUTHOR = "Nicolas Cenerario"
PLUGIN_DESCRIPTION = "This plugin adds a context menu action to do just what it says: Really Clearing metadata from files. I notice that in some case, \
even if the clear metadata option is enable, some metadata are still present making some duplicates files seems different. \
Since I'm using MusicBrainz Picard to keep my music library clean, this is not acceptable as I want to be able to find and delete those duplicates ;)"
PLUGIN_VERSION = "0.1"
PLUGIN_API_VERSIONS = ["0.9.0", "0.10", "0.15"]

from PyQt4 import QtCore

from rcm_models import NiCeFileAction
from rcm_views import NiCeDialog_show
from rcm_controllers import NiCeThreadClearMetadata

#===============================================================================
# NiCeFileActionClearMetadata
#===============================================================================
class NiCeFileActionClearMetadata(NiCeFileAction):
	NAME = "Clear metadata"
	def callback(self, obj):
		dialog = NiCeDialog_show()
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

#===============================================================================
# Initializing
#===============================================================================
my_plugin_1 = NiCeFileActionClearMetadata()
