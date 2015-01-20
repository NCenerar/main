#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from sys import argv, exit
from os import path
from glob import glob
from shutil import rmtree, copytree
from hashlib import sha256

from zipfile import ZipFile

from PyQt4 import QtCore, QtGui

from picard.file import File
from picard.cluster import Cluster, ClusterList

from mutagen import File as MFile

def get_cluster_list(patterns):
	cl = ClusterList()
	for pattern in patterns:
		c = Cluster(pattern)
		c.files = [File(f) for f in glob(pattern)]
		cl.append(c)
	return cl

def hashfile(afile, hasher, blocksize=65536):
	buf = afile.read(blocksize)
	while len(buf) > 0:
		hasher.update(buf)
		buf = afile.read(blocksize)
	return hasher.hexdigest()

###########
# TESTING #
###########
def test_clear_metadata(filename):
	t = MFile(filename)
	t.delete()
	t.save()

def test_print_sha256(filename):
	with open(filename) as fs:
		sha = hashfile(fs, sha256())
		print "{1} - {0}".format(filename, sha)

def test_rcm(cluster_list):
	myApp = QtGui.QApplication(argv)
	import rcm
	rcm.my_plugin_1.callback([cluster_list])

if __name__ == "__main__":
	print "Hello Python World!"

	src_zip = "./bugged.zip"
	src_dir = "./original/"
	dst_dir = "./last_test/"
	if path.isdir(src_dir):
		rmtree(src_dir)
	with ZipFile(src_zip) as zf:
		zf.extractall(src_dir)
	if path.isdir(dst_dir):
		rmtree(dst_dir)
	copytree(src_dir, dst_dir)

	cl = get_cluster_list(["{0}*Tagged*".format(dst_dir)])

	for f in cl.iterfiles():
		test_print_sha256(f.filename)

	test_rcm(cl)

	for f in cl.iterfiles():
		test_print_sha256(f.filename)

	print "Good Bye Python World!"
	exit(0)
