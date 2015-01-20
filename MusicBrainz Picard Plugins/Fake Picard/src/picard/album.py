#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from PyQt4 import QtCore
from picard.cluster import Cluster

class Album(object):
    release_group_loaded = QtCore.pyqtSignal()
    def __init__(self, album_id, discid=None):
        self.tracks = []
        self.loaded = False
        self.load_task = None
        self.release_group = None
        self._files = 0
        self._requests = 0
        self._tracks_loaded = False
        self._discid = discid
        self._after_load_callbacks = []
        self.unmatched_files = Cluster(_("Unmatched Files"), special=True, related_album=self, hide_if_empty=True)
        self.errors = []
        self.status = None
    def __repr__(self):
        return '<Album %s MetadataAlbum>' % (self.id)
    def iterfiles(self, save=False):
        for track in self.tracks:
            for f in track.iterfiles():
                yield f
        if not save:
            for f in self.unmatched_files.iterfiles():
                yield f
