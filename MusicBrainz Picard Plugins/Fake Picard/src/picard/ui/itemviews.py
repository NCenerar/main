#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from PyQt4 import QtGui

class BaseAction(QtGui.QAction):
	NAME = "Unknown"
	MENU = []
	def __init__(self):
		QtGui.QAction.__init__(self, self.NAME, None)
		self.tagger = Tagger()

class Tagger(object):
	def remove_files(self, files):
		pass

def register_album_action(action):
	pass
def register_cluster_action(action):
	pass
def register_clusterlist_action(action):
	pass
def register_track_action(action):
	pass
def register_file_action(action):
	pass
