#!/usr/bin/python
# -*- coding: utf-8 -*-

from picard.file import File
from picard.track import Track
from picard.album import Album
from picard.cluster import Cluster, ClusterList
from picard.ui.itemviews import BaseAction, register_album_action, register_cluster_action, register_clusterlist_action, register_track_action, register_file_action

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
# NiCeFiles
#===============================================================================
class NiCeFiles(object):
	def __init__(self, obj):
		super(NiCeFiles, self).__init__()
		self._obj = obj
	def __iter__(self):
		if isinstance(self._obj, File):
			(yield self._obj)
		elif isinstance(self._obj, Track):
			for f in self._obj.linked_files:
				(yield f)
		elif isinstance(self._obj, Album):
			for track in self._obj.tracks:
				for f in track.linked_files:
					(yield f)
			for f in self._obj.unmatched_files.files:
				(yield f)
		elif isinstance(self._obj, Cluster):
			for f in self._obj.files:
				(yield f)
		elif isinstance(self._obj, ClusterList):
			for cluster in self._obj:
				for f in cluster.files:
					(yield f)
		elif isinstance(self._obj, basestring):
			pass
		else:
			try:
				iterator = iter(self._obj)
			except TypeError:
				pass
			else:
				for obj in iterator:
					for f in NiCeFiles(obj):
						(yield f)
