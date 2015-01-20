#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

class Track(object):
    def __init__(self, track_id, album=None):
        self.album = album
        self.linked_files = []
        self.num_linked_files = 0
    def __repr__(self):
        return '<Track %s MetadataTitle>' % (self.id)
    def iterfiles(self, save=False):
        for f in self.linked_files:
            yield f