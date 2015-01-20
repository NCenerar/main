#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os.path
from PyQt4 import QtCore

class File(QtCore.QObject):
    def __init__(self, filename):
        super(File, self).__init__()
        self.filename = filename
        self.base_filename = os.path.basename(filename)
    def __repr__(self):
        return '<File %r>' % self.base_filename
    def iterfiles(self, save=False):
        yield self