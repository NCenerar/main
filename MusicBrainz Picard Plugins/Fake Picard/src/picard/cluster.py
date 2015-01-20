#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from PyQt4 import QtCore

class Cluster(QtCore.QObject):
    def __init__(self, name, artist="", special=False, related_album=None, hide_if_empty=False):
        QtCore.QObject.__init__(self)
        self.item = None
        self.special = special
        self.hide_if_empty = hide_if_empty
        self.related_album = related_album
        self.files = []
        self.lookup_task = None
    def __repr__(self):
        return '<Cluster MetaDataAlbum>'
    def iterfiles(self, save=False):
        for f in self.files:
            yield f

class ClusterList(list):
    def __init__(self):
        super(ClusterList, self).__init__()
    def __hash__(self):
        return id(self)
    def iterfiles(self, save=False):
        for cluster in self:
            for f in cluster.iterfiles(save):
                yield f
