#!/usr/bin/python
# -*- coding: utf-8 -*-

from picard.ui.itemviews import BaseAction, register_album_action, register_cluster_action, register_clusterlist_action, register_track_action, register_file_action
from test.test_pep277 import filenames

#===============================================================================
# NiCeFileAction
#===============================================================================
class NiCeFileAction(BaseAction):
	def __init__(self):
		super(NiCeFileAction, self).__init__()
		register_file_action(self)
		register_track_action(self)
		register_album_action(self)
		register_cluster_action(self)
		register_clusterlist_action(self)
	def callback(self, obj):
		pass

#===============================================================================
# NiCeDuplicatesFinder
#===============================================================================
class NiCeDuplicatesFinder(object):
	def __init__(self):
		super(NiCeDuplicatesFinder, self).__init__()
	def scan_file(self, filename):
		pass